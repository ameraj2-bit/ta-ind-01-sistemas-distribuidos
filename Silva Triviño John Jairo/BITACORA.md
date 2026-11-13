# Bitácora de trabajo — Silva Triviño John Jairo

## 2026-11-12

- **Qué hice (tarde):** Estudié con ayuda de Claude la arquitectura de Apache Cassandra (anillo de nodos, replicación, coordinador, niveles de consistencia, ruta de escritura, gossip) y preparé por escrito el guion de mi boceto, con mis propias respuestas a preguntas de comprobación. [Ajusta o añade lo que realmente hiciste.]
- **Problema encontrado:** Al revisar los mensajes del curso vi que otros compañeros ya habían registrado Cassandra, como sistema principal y como sistema de comparación, y que MongoDB también estaba tomado.
- **Cómo lo resolví:** Cambié el sistema para no repetir el de otros estudiantes. Elegí HDFS como sistema principal, comparado con Ceph, y comprobé que ninguno de los dos estaba en la lista de sistemas ya registrados. Actualicé el README de mi carpeta y el principal.
- **Uso de herramientas:** Usé Claude (Anthropic) para entender los requisitos, estudiar la arquitectura de Cassandra, proponer HDFS con Ceph como alternativa y preparar los textos de arranque del repositorio. Las entradas de esta bitácora las escribo yo.
- **Tiempo dedicado:** 2:35h
- **Siguiente paso:** Estudiar la arquitectura de HDFS, hacer a mano el boceto de su arquitectura y levantar un clúster con un NameNode y 3 DataNodes en Docker.
