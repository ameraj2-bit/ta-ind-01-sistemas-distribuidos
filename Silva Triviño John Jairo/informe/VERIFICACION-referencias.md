# Verificación de referencias

Verificadas por Silva Triviño John Jairo el 13/11/2026: abrí cada DOI o URL y comparé autores, año, título, revista, volumen, número y páginas con `referencias.bib`. Todas coinciden. Las capturas de verificación están en `capturas-lectura/`.

| Clave | DOI / URL | Datos comprobados | Resultado |
|---|---|---|---|
| Peters2021 | https://doi.org/10.1007/s41781-021-00071-1 | Peters y van der Ster; *Computing and Software for Big Science*, vol. 5, art. 25; 2021 | Coincide |
| Saadoon2022 | https://doi.org/10.1016/j.asej.2021.06.024 | Seis autores; *Ain Shams Engineering Journal*, vol. 13, nº 2, art. 101538; 2022 | Coincide |
| Ahmed2023 | https://doi.org/10.32620/reks.2023.2.14 | Cinco autores; *Radioelectronic and Computer Systems*, nº 2(106), pp. 171–179; 2023 | Coincide |
| Dhulavvagol2023 | https://doi.org/10.1016/j.procs.2023.01.254 | Dhulavvagol y Totad; *Procedia Computer Science*, vol. 218, pp. 2830–2841 | Coincide. La página del editor indica 2023 y el formato de cita de otra base indica 2022; se usa 2023 (editor y DOI) |
| Li2023 | https://doi.org/10.1007/s10586-022-03764-3 | Li y Wang; *Cluster Computing*, vol. 26, nº 2, pp. 1125–1146; 2023 | Coincide |
| Alange2023 | https://doi.org/10.1007/s10586-023-03992-1 | Alange y Sagar; *Cluster Computing*, vol. 26, nº 6, pp. 3381–3388; 2023 | Coincide |
| LinkedIn2021 | https://engineering.linkedin.com/blog/2021/the-exabyte-club--linkedin-s-journey-of-scaling-the-hadoop-distr | Shvachko, Liang y Dzinamarira; 27 may. 2021 | Coincide |
| LinkedIn2020 | https://engineering.linkedin.com/blog/2020/learnings-from-a-recent-hadoop-incident | Ramu y Rajamani; 6 ago. 2020 (incidente real) | Coincide |
| HadoopHDFSDesign | https://hadoop.apache.org/docs/r3.3.0/hadoop-project-dist/hadoop-hdfs/HdfsDesign | Documentación de Apache Hadoop 3.3.0 | Coincide |
| CephArchitecture | https://docs.ceph.com/en/reef/architecture/ | Documentación de Ceph, release Reef | Coincide |

## Qué respalda cada fuente
- **Ahmed2023:** define CAP y PACELC (consistencia frente a latencia). No menciona HDFS; la clasificación de HDFS es razonamiento propio apoyado en la documentación de Hadoop.
- **Saadoon2022:** el enfoque de latidos, usado en HDFS, YARN y Storm (p. 3 del PDF).
- **Peters2021:** replicación o codificación por borrado, y CRUSH reparte por dominios de fallo (p. 2).
- **Dhulavvagol2023:** el NameNode no escala; federación.
- **Li2023:** en Ceph la elección de nodos se basa en capacidad; desbalance en sistemas heterogéneos.
- **Alange2023:** flujo de lectura de HDFS: el cliente pide metadatos al NameNode y luego contacta a los DataNodes.
- **LinkedIn2021:** escala de HDFS en LinkedIn (1 EB, 10 000 nodos, 500 PB, ~1000 millones de objetos en un NameNode, montículo de 380 GB).
- **LinkedIn2020:** incidente real: ~2 % de máquinas reinstaladas por error, ~0,02 % de bloques perdidos, 10 % de flujos fallidos. No fue una caída del NameNode.
