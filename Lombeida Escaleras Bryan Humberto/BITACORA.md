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
