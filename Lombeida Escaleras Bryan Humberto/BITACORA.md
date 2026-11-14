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

**Tiempo dedicado:** 3 horas.


## Sesión 7: 13 de noviembre de 2026

**Actividades realizadas**

- Se comprobó que el emulador estaba activo y que la consulta devolvía los saldos de 90 y 60. Luego se detuvo el contenedor y se repitió la consulta con un límite de 15 segundos. El comando `timeout` terminó con el código 124.
- Se reinició el contenedor y se volvió a consultar. El emulador respondió `Instance not found`. Después de recrear la instancia, la base y la tabla, se comprobó que la consulta devolvía los saldos de la nueva carga, 100 y 50.
- Se guardaron las capturas, se documentaron los comandos y resultados en `experimento/README-Experimento.md` y se incorporó al informe la subsección «Interrupción y recuperación del emulador». Se recompiló el PDF y se comprobó que incluyera las cuatro capturas.

**Problemas encontrados:** La instancia anterior dejó de estar disponible tras el reinicio. En el primer intento de recrearla, Python devolvió `ModuleNotFoundError` porque el entorno virtual no estaba activo.

**Solución:** Se activó el entorno virtual, se configuró la conexión local y se ejecutaron de nuevo `preparar` y `consultar`. En el informe se explicó que el emulador pierde su estado en memoria al reiniciarse y que la consulta volvió a funcionar tras cargar los datos iniciales.

**Tiempo dedicado:** 1 hora.

## Sesión 8: 13 de noviembre de 2026

**Actividades realizadas**

- Se comparó Google Spanner multirregional con DynamoDB Global Tables en modo MREC mediante una tabla de siete criterios de la Unidad 1. La discusión también explicó las diferencias con el modo MRSC y respaldó las afirmaciones con citas numéricas.
- Se incorporó al Anexo B la captura de lectura de Lima y colaboradores. En el análisis se citó su estudio sobre el costo y la latencia de distintas estrategias de lectura en sistemas con réplicas en varias regiones.
- Se recompiló el PDF y se comprobó que la tabla apareciera antes de la discusión y que la captura de Lima estuviera en el Anexo B.
- Se redactó la postura crítica de Spanner en `main.tex`. Se analizaron las fortalezas de las transacciones y la replicación, los compromisos de latencia y disponibilidad asociados al quórum, y los escenarios en los que DynamoDB con MREC puede ser más adecuado.

**Problemas encontrados:** En la primera compilación, LaTeX colocó la tabla después de la discusión. Para redactar la postura crítica se necesitaba precisar qué garantías corresponden al servicio de producción y qué observaciones proceden del emulador.

**Solución:** Se ajustó la ubicación de la tabla en `main.tex` y se volvió a compilar el informe para verificar el orden. Se respaldaron las valoraciones con las fuentes ya citadas y se explicó el alcance de los resultados del emulador.

**Tiempo dedicado:** 1 hora y 30 minutos.


## Sesión 9: 13 de noviembre de 2026

**Actividades realizadas**

- Se incorporó a Arquitectura del sistema el diagrama digital de una escritura en Spanner. Se explicó su evolución desde el boceto del Anexo A y se verificó que el XML editable correspondiera al PNG.
- Se redactaron dos ejemplos personales. La demora al matricularse en el SGA de la UTEQ se relacionó con la latencia percibida y los errores de envío en WhatsApp con la visibilidad de los fallos y los reintentos.
- Se completó la introducción con el problema que resuelve Spanner, sus usuarios, su escala y el motivo de elección. Se ajustaron las conclusiones a los resultados del experimento y a la comparación con DynamoDB.
- Se redactó un resumen.

**Problemas encontrados:** Era necesario explicar los cambios del diagrama respecto del boceto y relacionar los casos del SGA y de WhatsApp con la unidad a partir de lo observado como usuario. También se debía verificar la escala de Spanner y ajustar el resumen a la extensión solicitada.

**Solución:** Se describieron los cambios visibles entre ambos diagramas y se redactaron los ejemplos desde la experiencia personal. Se añadió una fuente de Google Cloud para las cifras de escala, se vincularon las conclusiones con los resultados observados y se comprobó el número de palabras del resumen.

**Tiempo dedicado:** 2 horas.

## Sesión 10: 13 de noviembre de 2026

**Actividades realizadas**

- Se completó el README individual con el archivo principal, el compilador, las dependencias y el orden de compilación. Se enlazó la documentación del experimento y se dejó un espacio para el video de sustentación.
- Se revisó la declaración de uso de inteligencia artificial para indicar la herramienta, el modelo, las tareas en las que se utilizó y cómo se verificaron las afirmaciones y los resultados.
- Se recompiló el informe y se comprobó la presencia de la declaración en el PDF.
- Se hizo una reestructuracion del main.tex para tener un formato mas de acorde al formato IEEE.

**Problemas encontrados:** La carpeta necesitaba instrucciones de compilación y el enlace del video aún estaba pendiente. La declaración de IA requería precisar cómo se verificó el trabajo.

**Solución:** Se documentó la secuencia de pdfLaTeX y Biber, se dejó identificado el espacio para el video y se indicaron las fuentes, las salidas de terminal y las capturas utilizadas para verificar el informe.

**Tiempo dedicado:** 1 hora.


## Sesión 11: 13 de noviembre de 2026

**Actividades realizadas**

- Se grabó y procesó el video de sustentación individual de la práctica experimental con Google Spanner y Docker.
- En el video se explicó la arquitectura del entorno de pruebas, la consulta de saldos iniciales por gRPC, la detención del contenedor con comprobación de pérdida de disponibilidad por timeout (código 124).
- Se publicó el video en YouTube y se actualizó `README.MD` con el enlace directo: `https://youtu.be/BIcxJ_XgQCg`.

**Problema encontrado:** Ordenar la explicación técnica para cumplir con el tiempo mínimo requerido de 3 minutosy maximo 5 minutos abordando detalladamente cada comando y su fundamento en sistemas distribuidos.

**Solución:** Se grago varias veces el paso a paso guiado por las cuatro figuras del experimento presentes en el informe, alcanzando la duración requerida y conectando los eventos observados con el modelo cliente-servidor gRPC y el teorema CAP.

**Tiempo dedicado:** 30 minutos.
