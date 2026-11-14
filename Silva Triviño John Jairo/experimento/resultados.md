# Resultados del experimento: caída de un DataNode en HDFS

Autor: Silva Triviño John Jairo. Máquina: DESKTOP-H4C4SME, usuario `desktop-h4c4sme\usuario`. Fecha: 12 y 13 de noviembre de 2026.

Entorno: `docker compose` con 1 NameNode y 4 DataNodes (imagen `apache/hadoop:3`), factor de replicación 3. Archivo `docker-compose.yml` y `config` en esta carpeta. Todos los DataNodes comparten el disco de mi computador (limitación: no se simulan fallos de disco reales).

Las horas locales son UTC-5. El log del NameNode está en UTC.

## Línea de tiempo (datos observados)

| Hora local | Hora UTC | Evento |
|---|---|---|
| 23:21:38 | 04:21:38 | `dfsadmin -report`: 4 DataNodes vivos, `Under replicated blocks: 0` (captura-04) |
| 23:24:35 | 04:24:37 | `fsck /datos.bin`: 3 bloques, cada uno con 3 réplicas |
| 23:28:51 | 04:28:51 | `docker stop datanode4` |
| 23:31:12 | 04:31:12 | Monitoreo: aún `Live datanodes (4)`, `Under replicated blocks: 0` |
| 23:42:53 | 04:42:53 | Log del NameNode: `removeDeadDatanode: lost heartbeat from 172.21.0.4` (captura-10) |
| 23:52:47 | 04:52:47 | Monitoreo: `Dead datanodes (1)`, `Live datanodes (3)`, `Under replicated blocks: 0` (captura-08) |
| 00:03:15 | 05:03:15 | `fsck`: 3 DataNodes, bloques con 3 réplicas sin `172.21.0.4` (captura-09) |
| 00:04:21 | 05:04:21 | Lectura con el nodo caído: real 1,853 s (captura-09) |
| 00:10:42 | 05:10:42 | `docker start datanode4` (captura-11) |
| 00:11:10 | 05:11:10 | `Live datanodes (4)`, `Under replicated blocks: 0` (captura-11) |
| 00:13:47-56 | 05:13 | Lecturas con 4 DataNodes: 1,690 s, 1,901 s, 2,107 s |

Tiempo entre apagar el nodo y su declaración como muerto: 04:42:53 - 04:28:51 = **14 min 02 s**.

## Comandos y salidas

### 1. Informe inicial del clúster

    whoami; hostname; Get-Date; docker exec namenode hdfs dfsadmin -report | Select-String "Live datanodes|Hostname|Last contact|Under replicated"

Salida (captura-04, líneas útiles):

    jueves, 12 de noviembre de 2026 23:21:38
    Under replicated blocks: 0
    Live datanodes (4):
    Hostname: datanode2
    Last contact: Fri Nov 13 04:21:39 UTC 2026
    Hostname: datanode4

Los otros dos `Hostname` quedaron fuera de la captura-04.

### 2. Crear y subir un archivo de 300 MB

    docker exec namenode bash -c "dd if=/dev/urandom of=/tmp/datos.bin bs=1M count=300"
    docker exec namenode hdfs dfs -put /tmp/datos.bin /datos.bin

Salida: `300+0 records in`, `300+0 records out`, `314572800 bytes (315 MB) copied, 0.641603 s, 490 MB/s`.

### 3. Dónde quedaron los bloques (antes de la falla)

    whoami; hostname; Get-Date; docker exec namenode hdfs fsck /datos.bin -files -blocks -locations

Resultado: 3 bloques (134217728 B, 134217728 B y 46137344 B), `Live_repl=3` en cada uno, `Status: HEALTHY`, `Number of racks: 1`.

| Bloque | Réplicas en |
|---|---|
| 0 | datanode1, datanode4, datanode3 |
| 1 | datanode4, datanode3, datanode2 |
| 2 | datanode2, datanode4, datanode3 |

(172.21.0.3 = datanode2, .4 = datanode4, .5 = datanode3, .6 = datanode1)

### 4. Provocar la falla

    whoami; hostname; Get-Date; docker stop datanode4

Salida: hora 23:28:51, `datanode4`.

### 5. Monitoreo cada minuto

    while ($true) { Get-Date; docker exec namenode hdfs dfsadmin -report | Select-String "Live datanodes|Dead datanodes|Under replicated" | ForEach-Object { $_.Line.Trim() }; Start-Sleep 60 }

Observación: a las 23:31 el NameNode seguía mostrando 4 DataNodes vivos; entre 23:52 y 23:59 mostraba `Dead datanodes (1)`, `Live datanodes (3)` y `Under replicated blocks: 0` (captura-08).

### 6. Log del NameNode

    docker logs namenode 2>&1 | Select-String "lost heartbeat|Removing a node"

Salida relevante (captura-10, ejecutada a las 00:09:43):

    2026-11-13 04:42:53 INFO StateChange:880 - BLOCK* removeDeadDatanode: lost heartbeat from 172.21.0.4:9866, removeBlocksFromBlockMap true
    2026-11-13 04:42:53 INFO NetworkTopology:229 - Removing a node: /default-rack/172.21.0.4:9866


### 7. Bloques después de la caída (re-replicación)

    whoami; hostname; Get-Date; docker exec namenode hdfs fsck /datos.bin -files -blocks -locations

Salida (captura-09; la línea del bloque 0 queda fuera de la captura):

    1. ...blk_1073741826_1002 len=134217728 Live_repl=3 [172.21.0.3:9866, 172.21.0.5:9866, 172.21.0.6:9866]
    2. ...blk_1073741827_1003 len=46137344 Live_repl=3 [172.21.0.3:9866, 172.21.0.5:9866, 172.21.0.6:9866]
    Status: HEALTHY
     Number of data-nodes:  3
     Number of racks:       1
     Total blocks (validated):      3 (avg. block size 104857600 B)
     Under-replicated blocks:       0 (0.0 %)
     Default replication factor:    3
     Average block replication:     3.0
     Missing blocks:                0
     Missing replicas:              0 (0.0 %)
    FSCK ended at Fri Nov 13 05:03:15 UTC 2026 in 1 milliseconds

Los bloques 1 y 2 pasaron de tener una réplica en 172.21.0.4 (datanode4) a estar en 172.21.0.3, .5 y .6 (datanode2, datanode3 y datanode1).

### 8. Lecturas del archivo completo

    whoami; hostname; Get-Date; docker exec namenode bash -c "time hdfs dfs -cat /datos.bin > /dev/null"

| Situación | Hora | real |
|---|---|---|
| Nodo caído (3 DataNodes vivos) | 00:04:21 | 1,853 s |
| 4 DataNodes vivos | 00:13:47 | 1,690 s |
| 4 DataNodes vivos | 00:13:51 | 1,901 s |
| 4 DataNodes vivos | 00:13:56 | 2,107 s |

Promedio con 4 DataNodes: 1,899 s.

### 9. Estado tras recuperar el nodo

    whoami; hostname; Get-Date; docker start datanode4
    whoami; hostname; Get-Date; docker exec namenode hdfs dfsadmin -report | Select-String "Live datanodes|Dead datanodes|Under replicated|Over-replicated"

Salida (captura-11, 00:11:10): `Under replicated blocks: 0`, `Live datanodes (4)`.

## Interpretación

### 1. Detección de fallos

El experimento permitió observar que la detección de fallos en HDFS no es inmediata. Después de ejecutar `docker stop datanode4` a las 23:28:51, el NameNode continuó considerando que los cuatro DataNodes estaban activos. Esto se comprobó a las 23:31:12, cuando el informe todavía mostraba `Live datanodes (4)`.

Posteriormente, a las 23:42:53 hora local (04:42:53 UTC), el registro del NameNode mostró el mensaje `lost heartbeat from 172.21.0.4:9866`, indicando que había dejado de recibir los mensajes de actividad del DataNode. La diferencia entre el momento de apagar el contenedor y el momento en que fue declarado muerto fue de **14 minutos y 2 segundos**.

Esto demuestra que HDFS utiliza un mecanismo de detección basado en heartbeats. Los DataNodes envían periódicamente señales al NameNode para informar que continúan funcionando. Cuando estas señales dejan de recibirse durante el tiempo establecido, el NameNode considera que el nodo ha fallado y actualiza el estado del clúster.

Según el código de Hadoop, un nodo se declara muerto tras `2 × recheck-interval + 10 × heartbeat.interval`. Con los valores por defecto (300 000 ms y 3 s) eso son 10 min 30 s, y como la comprobación solo se ejecuta una vez por cada `recheck-interval` (5 min), la detección puede ocurrir entre 10 min 30 s y 15 min 30 s después de la falla. Los 14 min 02 s observados caen en ese rango. No verifiqué los valores configurados en mi clúster con `hdfs getconf`, así que esta explicación supone que se usan los valores por defecto de la imagen `apache/hadoop:3`.

El tiempo observado también permite comprender que existe un compromiso entre la rapidez de detección y la tolerancia a interrupciones temporales de comunicación. Un tiempo de espera mayor evita declarar muerto un nodo por una demora momentánea, pero prolonga el tiempo durante el cual el sistema puede desconocer una falla real.

### 2. Tolerancia a fallos y transparencia de distribución

Uno de los resultados más importantes fue que el archivo `/datos.bin`, de 300 MB, continuó disponible después de apagar `datanode4`. Aunque el clúster pasó de cuatro a tres DataNodes activos, fue posible realizar una lectura completa del archivo, obteniendo un tiempo de 1,853 segundos.

Esta observación demuestra tolerancia a fallos a nivel de almacenamiento: la pérdida de un DataNode no provocó la pérdida del archivo porque sus bloques estaban distribuidos y replicados en diferentes nodos.

También se relaciona con la transparencia de fallos, ya que el cliente pudo solicitar el contenido del archivo utilizando la misma ruta de HDFS, sin tener que indicar manualmente en qué DataNode se encontraba cada bloque. HDFS gestionó internamente la ubicación de las réplicas disponibles.

Sin embargo, es importante aclarar que el experimento no demuestra que cualquier cantidad de fallos pueda ser soportada. La protección observada corresponde a la caída de un DataNode dentro de un clúster con factor de replicación 3 y cuatro nodos disponibles.

### 3. Re-replicación y recuperación automática

Antes de provocar la falla, los tres bloques del archivo tenían tres réplicas cada uno. En las ubicaciones registradas se observó que `datanode4` almacenaba una copia de cada bloque.

Después de detectar su desaparición, el NameNode identificó las réplicas que debían recuperarse y coordinó la distribución de nuevas copias entre los DataNodes restantes.

La comprobación realizada mediante `hdfs fsck` a las 00:03:15 mostró:

- Tres DataNodes disponibles.
- Factor de replicación configurado en 3.
- Promedio de replicación de 3,0.
- Cero bloques subreplicados.
- Cero bloques perdidos.
- Estado general `HEALTHY`.

En los bloques 1 y 2 se pudo comprobar directamente que las tres ubicaciones correspondían a los DataNodes que continuaban activos. Para el bloque 0, la captura no muestra sus ubicaciones individuales, aunque el resumen de `fsck` confirma que el archivo tenía sus tres bloques con el nivel de replicación esperado.

Este resultado evidencia que HDFS no depende exclusivamente de mantener una copia en un nodo específico. Puede recuperar el nivel de redundancia utilizando otros nodos disponibles, sin necesidad de que el usuario vuelva a cargar el archivo.

### 4. Comparación de tiempos de lectura

Se realizaron cuatro mediciones de lectura del archivo completo: una con tres DataNodes activos y tres con cuatro DataNodes activos.

| Situación | Tiempo de lectura |
|---|---:|
| Tres DataNodes activos | 1,853 s |
| Cuatro DataNodes activos | 1,690 s |
| Cuatro DataNodes activos | 1,901 s |
| Cuatro DataNodes activos | 2,107 s |

El promedio de las tres lecturas realizadas con cuatro DataNodes fue de **1,899 segundos**.

La lectura realizada con tres DataNodes tardó 1,853 segundos, una diferencia de apenas 0,046 segundos respecto al promedio anterior.

En esta prueba no se observó una degradación importante del tiempo de lectura cuando un DataNode estaba apagado. Sin embargo, no se puede afirmar que la caída no afecte al rendimiento en todos los escenarios, porque solamente se realizaron cuatro mediciones y no se contó con una medición de referencia anterior a la falla.

Además, las lecturas se realizaron después de que el sistema había recuperado el nivel de replicación. Por esta razón, los resultados muestran que el archivo seguía siendo accesible con tres DataNodes, pero no permiten medir directamente el rendimiento durante el proceso inicial de detección y recuperación.

### 5. Limitaciones del experimento

Durante el desarrollo de la prueba se identificaron las siguientes limitaciones:

- Los cuatro DataNodes compartían el disco físico del mismo computador. Por lo tanto, el experimento simuló la caída de un proceso o contenedor, pero no una falla independiente de almacenamiento.
- El monitoreo se realizó cada 60 segundos, por lo que no fue posible identificar con precisión el instante en que comenzó la re-replicación.
- Solamente se realizó una repetición del experimento, por lo que los resultados no representan una evaluación estadística del comportamiento de HDFS.
- No se midió el tiempo de lectura antes de provocar la falla.
- No se realizaron lecturas durante el intervalo en que el DataNode estaba apagado, pero todavía no había sido declarado muerto por el NameNode.
- No se provocaron fallos simultáneos de varios DataNodes.
- No se evaluó el comportamiento ante la caída del NameNode.

Estas limitaciones deben considerarse al interpretar los resultados, ya que el entorno Docker permite reproducir determinados comportamientos de un sistema distribuido, pero no representa completamente las condiciones de un clúster físico de producción.

### 6. Hipótesis inicial y resultados observados

Antes de realizar el experimento, esperaba que al apagar uno de los cuatro DataNodes el sistema detectara su ausencia y que, debido al factor de replicación 3, el archivo continuara disponible desde los otros nodos.

El resultado coincidió con esa expectativa: el NameNode detectó la pérdida del DataNode mediante los heartbeats y el archivo pudo leerse sin necesidad de volver a subirlo.

Lo que más llamó mi atención fue el tiempo que tardó el NameNode en declarar muerto al nodo. Inicialmente podía parecer que el contenedor se había apagado correctamente y que el sistema debía reconocerlo inmediatamente, pero las observaciones demostraron que existe un intervalo de detección.

También fue importante comprobar que, después de la falla, el sistema pudo conservar el factor de replicación configurado. Esto permitió entender que la tolerancia a fallos no consiste únicamente en seguir funcionando cuando un nodo desaparece, sino también en recuperar la redundancia de los datos para mantener la protección ante posibles fallos posteriores.

En conclusión, el experimento permitió comprobar de manera práctica cómo HDFS utiliza la replicación, los heartbeats y la coordinación del NameNode para mantener la disponibilidad de los archivos ante la pérdida de un DataNode.
