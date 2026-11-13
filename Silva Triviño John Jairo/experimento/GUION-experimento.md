# Guion del experimento: caída de un DataNode en HDFS

Objetivo: observar la tolerancia a fallos de HDFS (replicación de bloques, detección de un DataNode caído y re-replicación).

Regla: ejecuta cada comando tú, copia la salida real y anota tu interpretación. Nada de este archivo son resultados.

## 0. Antes de empezar (en cada captura debe verse tu usuario y la hora)

    whoami; hostname; date

## 1. Levantar el clúster

    docker compose up -d
    docker compose ps

Captura 1: los 5 contenedores en ejecución.

## 2. Comprobar los DataNodes vivos

    docker exec namenode hdfs dfsadmin -report

Captura 2: debe decir 4 DataNodes vivos (live). También puedes abrir http://localhost:9870.

## 3. Subir un archivo grande (3 bloques de 128 MB aprox.)

    docker exec namenode bash -c "dd if=/dev/urandom of=/tmp/datos.bin bs=1M count=300"
    docker exec namenode hdfs dfs -put /tmp/datos.bin /datos.bin
    docker exec namenode hdfs fsck /datos.bin -files -blocks -locations

Captura 3: cada bloque con 3 réplicas y en qué DataNodes están.

## 4. Medir una lectura antes de la falla

    docker exec namenode bash -c "time hdfs dfs -cat /datos.bin > /dev/null"

Anota el tiempo real que salió.

## 5. Provocar la falla

    date
    docker stop datanode3     # elige el que tenga bloques según el fsck

Anota la hora exacta en que lo detuviste.

## 6. Observar cómo reacciona (repite cada minuto, anota la hora)

    docker exec namenode hdfs dfsadmin -report
    docker exec namenode hdfs fsck /datos.bin -files -blocks -locations

Anota: cuánto tardó el NameNode en marcarlo como muerto (el valor por defecto es largo), cuándo aparecen bloques sub-replicados y cuándo vuelven a tener 3 copias.

Captura 4: el momento en que el nodo figura como muerto o los bloques sub-replicados.

## 7. Leer el archivo con el nodo caído

    docker exec namenode bash -c "time hdfs dfs -cat /datos.bin > /dev/null"

¿Se puede leer? ¿Cambió el tiempo?

## 8. Recuperación

    docker start datanode3
    docker exec namenode hdfs dfsadmin -report

## 9. Interpretación (escríbela tú, con tus palabras)

- ¿Qué concepto de la Unidad 1 ilustra cada observación (tolerancia a fallos, transparencia de fallos y de replicación, CAP)?
- ¿Se cumplió mi hipótesis? ¿Qué me sorprendió?
