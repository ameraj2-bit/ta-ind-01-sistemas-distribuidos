# Resultados del experimento: caída de un DataNode en HDFS

Autor: Silva Triviño John Jairo. Máquina: DESKTOP-H4C4SME, usuario `desktop-h4c4sme\usuario`. Fecha: 12 y 13 de noviembre de 2026.

Entorno: `docker compose` con 1 NameNode y 4 DataNodes (imagen `apache/hadoop:3`), factor de replicación 3. Archivo `docker-compose.yml` y `config` en esta carpeta. Todos los DataNodes comparten el disco de mi computador (limitación: no se simulan fallos de disco reales).

Las horas locales son UTC-5. El log del NameNode está en UTC.

## Línea de tiempo (datos observados)

| Hora local | Hora UTC | Evento |
|---|---|---|
| 23:20:03 | 04:20:03 | `dfsadmin -report`: 4 DataNodes vivos, 0 bloques |
| 23:24:35 | 04:24:37 | `fsck /datos.bin`: 3 bloques, cada uno con 3 réplicas |
| 23:28:51 | 04:28:51 | `docker stop datanode4` |
| 23:31:12 | 04:31:12 | Monitoreo: aún `Live datanodes (4)`, `Under replicated blocks: 0` |
| 23:42:53 | 04:42:53 | Log del NameNode: `removeDeadDatanode: lost heartbeat from 172.21.0.4` |
| 23:52:47 | 04:52:47 | Monitoreo: `Dead datanodes (1)`, `Live datanodes (3)`, `Under replicated blocks: 0` |
| 00:03 | 05:03:15 | `fsck`: 3 DataNodes, bloques con 3 réplicas sin `172.21.0.4` |
| 00:04:21 | 05:04:21 | Lectura con el nodo caído: real 1,853 s |
| 00:10:45 | 05:10:45 | Log: `Removing a node ... 172.21.0.4` (el nodo se vuelve a registrar; [confirmar con "Adding a new node"]) |
| 00:13:47-56 | 05:13 | Lecturas con 4 DataNodes: 1,690 s, 1,901 s, 2,107 s |
| 00:15:04 | 05:15:04 | `Live datanodes (4)`, `Under replicated blocks: 0` |

Tiempo entre apagar el nodo y su declaración como muerto: 04:42:53 - 04:28:51 = **14 min 02 s**.

## Comandos y salidas

### 1. Informe inicial del clúster

    whoami; hostname; Get-Date; docker exec namenode hdfs dfsadmin -report

[Pegar aquí la salida completa que ya tengo del informe de las 23:20, con `Live datanodes (4)`.]

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

Observación: a las 23:31 el NameNode seguía mostrando 4 DataNodes vivos; entre 23:52 y 23:59 mostraba `Dead datanodes (1)` y `Under replicated blocks: 0`.

### 6. Log del NameNode

    docker logs namenode 2>&1 | Select-String "lost heartbeat|Removing a node"

Salida relevante:

    2026-11-13 04:42:53 INFO StateChange:880 - BLOCK* removeDeadDatanode: lost heartbeat from 172.21.0.4:9866, removeBlocksFromBlockMap true
    2026-11-13 04:42:53 INFO NetworkTopology:229 - Removing a node: /default-rack/172.21.0.4:9866
    2026-11-13 05:10:45 INFO NetworkTopology:229 - Removing a node: /default-rack/172.21.0.4:9866

### 7. Bloques después de la caída (re-replicación)

    whoami; hostname; Get-Date; docker exec namenode hdfs fsck /datos.bin -files -blocks -locations

[Pegar aquí la salida completa del fsck de las 00:03.] Resultado visible: `Number of data-nodes: 3`, `Status: HEALTHY`, `Under-replicated blocks: 0`, `Average block replication: 3.0`. Los bloques 1 y 2 están en 172.21.0.3, .5 y .6 (ya sin .4).

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

    whoami; hostname; Get-Date; docker exec namenode hdfs dfsadmin -report | Select-String "Live datanodes|Dead datanodes|Under replicated|Over-replicated"

Salida (00:15:04): `Under replicated blocks: 0`, `Live datanodes (4)`.

## Interpretación (escribir con mis palabras)

- Detección: [¿cuánto tardó y por qué creo que tardó eso? Comparar con el valor por defecto de la documentación.]
- Tolerancia a fallos y transparencia: [¿qué concepto de la Unidad 1 ilustra la lectura con el nodo caído?]
- Re-replicación: [¿qué muestra el fsck antes y después?]
- Limitaciones: [muestreo cada 60 s, un solo disco, pocas lecturas, una sola repetición.]
- Mi hipótesis frente a lo observado: [¿se cumplió? ¿qué me sorprendió?]
