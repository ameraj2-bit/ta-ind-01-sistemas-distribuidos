# Verificación bibliográfica

Consulta: 13 de noviembre de 2026. Se conservaron las referencias anteriores y se añadieron tres artículos. Hay seis artículos publicados entre 2021 y 2026; las fechas de consulta de la documentación web no se cuentan como publicación.

## Artículos añadidos

| Clave | Metadatos comprobados | Evidencia de indexación |
|---|---|---|
| `kokocinski2023correctness` | Maciej Kokociński, Tadeusz Kobus y Paweł T. Wojciechowski. On the correctness of highly available systems in the presence of failures. Journal of Parallel and Distributed Computing, 180, artículo 104707 (2023). DOI: 10.1016/j.jpdc.2023.04.008. | La ficha de la revista en PUBDB de DESY identifica cobertura en Scopus y SCIE. Es evidencia institucional de cobertura de la revista, no una consulta directa al registro individual de Scopus. |
| `sabaghian2023replication` | Khatereh Sabaghian, Keyhan Khamforoosh y Abdulbaghi Ghaderzadeh. Data Replication and Placement Strategies in Distributed Systems: A State of the Art Survey. Wireless Personal Communications, 129(4), 2419–2453 (2023). DOI: 10.1007/s11277-023-10240-7. | EBSCO recupera el artículo como publicación académica revisada por pares. Springer declara Scopus y SCIE para la revista. |
| `datta2022consistency` | Anwitaman Datta y Frederique Oggier. Concurrency Control and Consistency Over Erasure Coded Data. IEEE Access, 10, 118617–118638 (2022). DOI: 10.1109/ACCESS.2022.3219875. | El repositorio de Birmingham exporta el identificador SCOPUS:85141616347 y enlaza al registro de Scopus. El acceso directo a Scopus no fue posible desde la herramienta. |

Los tres son artículos de revistas con evidencia de indexación. Se distingue la evidencia del artículo de la cobertura de su revista; no se deduce indexación a partir del DOI ni se asignan cuartiles.

## Enlaces conservados

- Kokociński: https://www.sciencedirect.com/science/article/abs/pii/S0743731523000709
- PDF de los autores: https://www.cs.put.poznan.pl/pawelw/pdf/jpdc23-journal.pdf
- Cobertura de JPDC en PUBDB/DESY: https://bib-pubdb1.desy.de/record/8529
- Sabaghian, ficha editorial: https://link.springer.com/article/10.1007/s11277-023-10240-7
- Registro EBSCO del artículo: https://openurl.ebsco.com/contentitem/gcd%3A162895329?crl=f&id=ebsco%3Agcd%3A162895329&jrnl=09296212&sid=ebsco%3Aplink%3Acrawler-gcd
- Cobertura de Wireless Personal Communications: https://link.springer.com/journal/11277 (apartado Abstracted and indexed in).
- Datta, metadatos y exportación con identificador Scopus: https://research.birmingham.ac.uk/en/publications/concurrency-control-and-consistency-over-erasure-coded-data/
- Registro individual enlazado: https://www.scopus.com/pages/publications/85141616347

## Referencias anteriores

- Fruth y Scherzinger (2024): se añadió `eid = {241}`; se conservan las páginas internas 1–26. DBLP lo identifica como artículo de revista, con paginación 241:1–241:26: https://dblp.uni-trier.de/rec/journals/pacmmod/FruthS24.html
- Abadi (2012): se completó Daniel J. Abadi conforme al PDF del autor: https://www.cs.umd.edu/~abadi/papers/abadi-pacelc.pdf
- Shi (2024) y Kausar (2022) completan, junto con Fruth y los tres artículos añadidos, las seis publicaciones recientes. No se utilizan para acreditar los tres artículos indexados porque sigue pendiente verificar su cobertura en la base exigida.
- No se agregaron años de publicación a las páginas oficiales sin fecha.

## Validación del informe

- Secuencia completada: pdfLaTeX, Biber 2.21, pdfLaTeX, pdfLaTeX.
- Biber procesó 21 claves y generó `main.bbl` sin advertencias ni errores bibliográficos.
- El registro final de LaTeX no contiene citas o referencias indefinidas ni solicitudes de repetir LaTeX o Biber.
- Resultado: `informe/main.pdf`, 18 páginas tras integrar las tres capturas académicas en los anexos.
- Se añadió la traducción española de la etiqueta de número de artículo para imprimir los campos `eid`.
- La compilación utilizó configuración y caché locales en `informe/.miktex`, porque la configuración predeterminada de MiKTeX intentaba escribir fuera de la carpeta autorizada. No se actualizó la instalación global.
- Persisten avisos del entorno de MiKTeX y de separación silábica española, La versión PDF del diagrama y los desbordamientos de títulos se corrigieron al integrar los anexos. No son errores de resolución de citas.
