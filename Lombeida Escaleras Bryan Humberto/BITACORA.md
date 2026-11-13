# Bitácora de trabajo — TA-IND-01 - de Bryan Lombeida

## Sesión 1:  11 — 12 de noviembre de 2026

**Actividades realizadas**

- Se selecciono y se definio el caso de estudio: Google Spanner, Amazon DynamoDB los cuales seran los sistemas distribuidos que se compararan.
- Se verificaron los DOI `10.14778/3685800.3685833` y `10.5120/ijca2021921219`, y se incorporaron como entradas BibLaTeX de artículo y libro, respectivamente.
- Se preparó una estructura inicial de trece secciones en `main.tex`, con citas de muestra conectadas a la bibliografía.

**Problema encontrado:** Buscar referencias para ubicar en `referencias.bib` que estaban vacíos, al igual de agregar una estructura inicial en `main.tex` para la redactar el informe.

**Solución:** se añadieron las referencias verificadas y una estructura inicial del informe.

**Tiempo dedicado:** 1 hora y 30 minutos.


## Sesión 2: 12 de noviembre de 2026

**Actividades realizadas**

- Se busco los articulos o referencia que respalden la informacion para Google Spanner y Amazon DynamoDB, distinguiendo artículos de revista, trabajos de conferencia, documentación técnica y un reporte de incidente.
- Se actualizó `referencias.bib`: se retiraron dos entradas que no convenían para la bibliografía final y se incorporaron tres artículos recientes, dos trabajos USENIX, documentación oficial y el incidente de Spanner del 4 de julio de 2023.
- Se actualizó el README.md general con la descripcion de los sistemas a comparar

**Problema encontrado:** Algunas fuentes eran anteriores al límite de cinco años, trataban otros sistemas o podían llevar a generalizar resultados que no corresponden a Spanner. También se necesitaba separar las fuentes útiles para el análisis del requisito específico de tres artículos de revista indexada.

**Solución:** se conservaron las fuentes pertinentes para los temas de transparencias, CAP/PACELC, comunicación y tolerancia a fallos; las fuentes descartadas se retiraron del `.bib`.

**Tiempo dedicado:** 5 horas.

# Sesión 3: 12 de noviembre de 2026

**Actividades realizadas**
- Se añadieron capturas de los artículos *Efficient Causal Access in Geo-Replicated Storage Systems*, *Fast Commitment for Geo-Distributed Transactions via Decentralized Co-coordinators* y *HoliPaxos: Towards More Predictable Performance in State Machine Replication*, con los fragmentos citados subrayados para facilitar su comprobación.
- Se corrigieron en `referencias.bib` los enlaces de dos trabajos de USENIX para que apunten directamente a sus PDF y se añadió el ISBN faltante de uno de ellos.

**Problema encontrado:** Faltaban evidencias visuales de los fragmentos citados; dos referencias no enlazaban directamente a los PDF y una carecía de ISBN.

**Solución:** Se agregaron las tres capturas con los fragmentos subrayados y se corrigieron los enlaces y el ISBN en `referencias.bib`.

**Tiempo dedicado:** 1 hora.

## Sesión 4: 13 de noviembre de 2026

**Actividades realizadas**

- Se preparó una guía de la arquitectura de una escritura en Spanner y se elaboró el bosquejo inicial a mano, fotografiado como `figuras/Anexo-A.jpeg`, con nombre y fecha visibles.
- Se agregó la redacción de las siete transparencias de distribución y se incorporaron los párrafos revisados a `main.tex`, con citas de documentación oficial mediante BibLaTeX.

**Problema encontrado:** La primera compilación no pudo generar una fuente tipográfica porque TeX intentó escribir su caché fuera de una carpeta con permiso. 

**Solución:** Se compiló en un directorio temporal con una caché de TeX escribible y se copió únicamente el PDF resultante a esta carpeta. El contenido de la carátula queda pendiente de revisión.

**Tiempo dedicado:** 2 horas.

## Sesión 5: 13 de noviembre de 2026

**Actividades realizadas**

- Se desarrollaron en `main.tex` los apartados de CAP y PACELC, modelos de comunicación y tolerancia a fallos de Google Spanner, con citas y una distinción entre las capacidades documentadas de Spanner y los resultados de otros artículos.
- Se incorporó el bosquejo a mano de una escritura en Spanner como Anexo A y se ubicaron dos capturas de lectura anotadas en el Anexo B, con sus respectivas descripciones y citas. Se preparó el anexo de capturas en orientación horizontal para facilitar su lectura.

**Problema encontrado:** Las capturas necesitaban espacio suficiente para leerse y era necesario evitar atribuir a Spanner mecanismos o resultados estudiados en otros sistemas.

**Solución:** Se dispusieron las capturas del Anexo B en páginas horizontales y se precisó en el texto qué afirmaciones corresponden a Spanner y cuáles se usan solo como apoyo conceptual. La captura de *Efficient Causal Access* queda pendiente de ubicar cuando se cite ese artículo en el análisis comparativo.

**Tiempo dedicado:** 3 horas.

## Sesión 6: 13 de noviembre de 2026

**Actividades realizadas**

- Se comprobó Docker y se inició el emulador oficial de Google Spanner en el contenedor `spanner-ta-ind-01`, con los puertos locales 9010 y 9020. Se instaló la biblioteca `google-cloud-spanner` en un entorno virtual de Python y se verificó su importación.
- Se ejecutó `experimento/prueba_spanner.py` por etapas. La preparación creó la instancia, la base y dos cuentas con saldos iniciales de 100 y 50; la consulta confirmó un total de 150.
- Se canceló deliberadamente una transferencia antes del commit y se comprobó que los saldos permanecieron en 100 y 50. Luego se confirmó la transferencia y se observaron saldos de 90 y 60, con el total todavía en 150.
- Se guardaron capturas originales de la instalación, preparación, consulta, cancelación y confirmación en `experimento/`. Se documentaron los comandos, resultados y límites de la prueba en `experimento/README-Experimento.md`.

**Problemas encontrados:** `docker info` no pudo acceder al servidor sin permisos; además, el primer intento de ejecutar el programa desde `/home/bryan` falló porque la ruta relativa `experimento/prueba_spanner.py` no existía allí.

**Solución:** Se utilizó `sudo` para los comandos de Docker y se cambió a la carpeta de trabajo de Bryan antes de ejecutar el programa. Se distinguió expresamente la prueba local de transacciones de una prueba de replicación o tolerancia a fallos del servicio de producción.

**Tiempo dedicado:** 4 horas.
