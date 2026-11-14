# Verificación de referencias (hacerla TÚ, una por una)

Yo leí los datos en la página del editor. El requisito pide que el DOI lleve a los mismos datos, así que abre cada enlace y compara.

| Clave | DOI / URL | Qué comprobar |
|---|---|---|
| Peters2021 | https://doi.org/10.1007/s41781-021-00071-1 | Autores Peters y van der Ster; vol. 5, nº 1, art. 25; 2021 |
| Saadoon2022 | https://doi.org/10.1016/j.asej.2021.06.024 | 6 autores; Ain Shams Eng. J., vol. 13, art. 101538; 2022 |
| Ahmed2023 | https://doi.org/10.32620/reks.2023.2.14 | 5 autores; Radioelectronic and Computer Systems, nº 2(106), pp. 171–179; 2023 |
| Dhulavvagol2023 | https://doi.org/10.1016/j.procs.2023.01.254 | Dhulavvagol y Totad; Procedia CS vol. 218, pp. 2830–2841; 2023. **Yo NO pude abrir la página del editor**: los datos vienen de un catálogo de biblioteca. Si no coincide, quítala. |
| Li2023 | https://doi.org/10.1007/s10586-022-03764-3 | Zhike Li y Yong Wang; Cluster Computing, vol. 26, nº 2, pp. 1125–1146; 2023 (en línea oct. 2022) |
| Alange2023 | https://doi.org/10.1007/s10586-023-03992-1 | Neeta Alange y P. Vidya Sagar; Cluster Computing, vol. 26, nº 6, pp. 3381–3388; 2023 |
| HadoopHDFSDesign | URL del .bib | Abre la versión actual (stable) y cita esa; la que verifiqué es 3.3.0 (2020) |
| CephArchitecture | URL del .bib | Anota la página donde leíste cada cita |
| LinkedIn2020 | URL del .bib | Incidente real (ago. 2020, fuera de los 5 años; se usa como evidencia de incidente) |

## Qué respalda cada fuente (no afirmes más que esto)
- Ahmed2023: define CAP y PACELC (consistencia vs. latencia). **No menciona HDFS.** La clasificación de HDFS (orientado a consistencia) es tu razonamiento a partir de la documentación de Hadoop (un solo escritor, NameNode árbitro de metadatos), no una afirmación de ese artículo.
- Saadoon2022: HDFS usa heartbeats y un tiempo de espera estático; el artículo dice que eso retrasa la detección. Es la explicación a citar para tus 14 min, como contexto y no como causa probada.
- Peters2021: CephFS/RADOS, CRUSH y dominios de fallo; es un estudio de rendimiento y costo, no de inyección de fallos.
- Dhulavvagol2023: NameNode, federación y cuello de botella de metadatos.
- Incidente LinkedIn: ~2 % de las máquinas reinstaladas por error; ~0,02 % de bloques perdidos; 10 % de los flujos fallaron. No fue una caída del NameNode.

## Capturas de lectura (Anexo B), 3 como mínimo
Una por cada artículo de revista que cites con idea concreta: pantalla del PDF con la frase que usas resaltada y el número de página visible. Las haces tú.
