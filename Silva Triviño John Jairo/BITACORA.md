# Bitácora de trabajo — Silva Triviño John Jairo

## 2026-11-12 (tarde)

- **Qué hice:** Estudié con ayuda de Claude la arquitectura de Apache Cassandra (anillo de nodos, replicación, coordinador, niveles de consistencia, ruta de escritura, gossip) y preparé por escrito el guion de mi boceto, con mis propias respuestas a preguntas de comprobación. [Ajusta o añade lo que realmente hiciste.]
- **Problema encontrado:** Al revisar los mensajes del curso vi que otros compañeros ya habían registrado Cassandra, como sistema principal y como sistema de comparación, y que MongoDB también estaba tomado.
- **Cómo lo resolví:** Cambié el sistema para no repetir el de otros estudiantes. Elegí HDFS como sistema principal, comparado con Ceph, y comprobé que ninguno de los dos estaba en la lista de sistemas ya registrados. Actualicé el README de mi carpeta y el principal.
- **Uso de herramientas:** Usé Claude (Anthropic) para entender los requisitos, estudiar la arquitectura de Cassandra, proponer HDFS con Ceph como alternativa y preparar los textos de arranque del repositorio. Las entradas de esta bitácora las escribo yo.
- **Tiempo dedicado:** 2:35h
- **Siguiente paso:** Estudiar la arquitectura de HDFS, hacer a mano el boceto de su arquitectura y levantar un clúster con un NameNode y 3 DataNodes en Docker.

## 2026-11-12 (noche)

- **Qué hice:** Estudié la arquitectura de HDFS (NameNode, DataNodes, bloques, replicación, latidos, lectura y escritura) y la comparé con Ceph. Contesté preguntas de comprobación y dibujé a mano el boceto de la arquitectura con 1 NameNode y 3 DataNodes, con mi nombre y la fecha. Después preparé el entorno con Docker: levanté un clúster de 1 NameNode y 4 DataNodes con `docker compose`, comprobé con `dfsadmin -report` que había 4 DataNodes vivos, creé un archivo de 300 MB, lo subí a HDFS y revisé con `fsck` cómo se repartieron sus 3 bloques y sus réplicas. Apagué `datanode4` a las 23:28:51 y monitoreé la reacción del NameNode.
- **Problema encontrado:** Mi monitoreo con `Select-String` imprimía objetos largos y era difícil de leer. Además, no medí una lectura de línea base antes de apagar el nodo.
- **Cómo lo resolví:** Cambié el comando para imprimir solo la línea de texto con `ForEach-Object`. La línea base la medí después de recuperar el nodo, con los 4 DataNodes arriba, y lo dejé anotado en los resultados.
- **Uso de herramientas:** Usé Claude (Anthropic) para estudiar HDFS, para que me explicara los archivos `docker-compose.yml` y `config` y me diera el guion de comandos del experimento. Los comandos los ejecuté yo en mi computador y las capturas son de mi pantalla.
- **Tiempo dedicado:** 1 h 40 min
- **Siguiente paso:** Recuperar el nodo, terminar `resultados.md` con mi interpretación, subir las capturas y empezar a buscar y verificar las referencias.

## 2026-11-13 (madrugada)

- **Qué hice:** Seguí el monitoreo hasta ver `Dead datanodes (1)`. Con el log del NameNode obtuve la hora exacta en que lo declaró muerto: 04:42:53 UTC (23:42:53), unos 14 minutos y 2 segundos después de apagarlo. Comprobé con `fsck` que los bloques volvieron a tener 3 réplicas en los otros nodos, leí el archivo completo con el nodo caído (1,853 s) y recuperé `datanode4`, con 4 nodos vivos otra vez. Medí tres lecturas con 4 nodos (1,690 s, 1,901 s y 2,107 s).
- **Problema encontrado:** Esperaba que el NameNode lo marcara como muerto en unos 10 minutos y medio, que es el valor por defecto que leí, pero tardó 14 minutos. Tampoco alcancé a ver bloques sub-replicados porque mi monitoreo miraba cada 60 segundos.
- **Cómo lo resolví:** Anoté el tiempo medido tal cual lo observé y dejé pendiente buscar la explicación en la documentación de Hadoop. La limitación del muestreo la anoto en el informe.
- **Uso de herramientas:** Claude me ayudó a interpretar las salidas de los comandos y a armar la estructura de `resultados.md`. La interpretación final la escribo yo.
- **Tiempo dedicado:** 40 min
- **Siguiente paso:** Subir los archivos al repositorio, escribir mi interpretación y buscar las fuentes.

## 2026-11-13 (tarde y noche)

- **Qué hice:** Busqué y verifiqué las referencias del informe: abrí cada DOI y comparé autores, año, título, revista, volumen y páginas con el `.bib`. Hice las capturas de lectura anotadas de los artículos de Peters (p. 2), Saadoon (p. 3) y Ahmed (p. 172). Subí al repositorio las capturas, las referencias y el borrador del informe en LaTeX, completé `resultados.md` con mi interpretación del experimento y compilé el PDF en Overleaf. Después completé las secciones que faltaban: transparencias de distribución, escala del sistema y clasificación PACELC.
- **Problema encontrado:** Subí por error `resultados.md` a la carpeta `informe/` en lugar de a `experimento/`. Además, el `main.tex` del repositorio quedó con una versión anterior a la del `informe.pdf`, por lo que el PDF no habría podido regenerarse al clonar. También vi que la fuente de Dhulavvagol aparecía como 2023 en la página del editor y como 2022 en otra base de datos.
- **Cómo lo resolví:** Moví `resultados.md` a su carpeta y borré el duplicado. Subí el `main.tex` actualizado y comprobé que coincidía con el PDF. Para Dhulavvagol usé 2023, que es el dato del editor y del DOI.
- **Uso de herramientas:** Usé Claude (Anthropic) para buscar fuentes candidatas, redactar un borrador del informe en LaTeX y dibujar en TikZ el diagrama de la arquitectura a partir de mi boceto, y para revisar mi interpretación y señalarme afirmaciones sin respaldo. Verifiqué yo las referencias en las páginas de los editores y las capturas de lectura son de los PDF que leí.
- **Tiempo dedicado:** 2 h 40 min
- **Siguiente paso:** Grabar y subir el video de sustentación y revisar el informe completo.

## 2026-11-14

- **Qué hice:** Preparé el guion del video, lo ensayé y grabé el video de sustentación con mi rostro y mi voz. Lo subí a YouTube como no listado y agregué el enlace al `README.md`.
- **Problema encontrado:** No alcancé a ejecutar `hdfs getconf` para comprobar los valores de heartbeat de mi clúster.
- **Cómo lo resolví:** Dejé esa limitación escrita en el informe y en el video: no puedo explicar con certeza por qué la detección tardó 14 min 02 s.
- **Uso de herramientas:** Usé Claude para ordenar el guion del video y las indicaciones de pantalla. El video lo grabé yo.
- **Tiempo dedicado:** 1 h 05 min
- **Siguiente paso:** Revisar el informe completo y practicar la explicación oral del experimento.
