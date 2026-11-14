# Bitácora de trabajo — TA-IND-01

## 2026-11-11
- **Qué hice:** Creé el repositorio público, invité a los colaboradores y empecé a armar la estructura de carpetas.
- **Problema:** La actividad aparece como "Grupal" en el SGA, pero el documento dice "Individual".
- **Cómo lo resolví:** Seguí lo indicado por el docente y armé el repo para trabajo en grupo.
- **Tiempo dedicado:** 5 min

## 2026-11-12
- **Qué hice:** Creé una carpeta individual con su README y moví los archivos (bitácora, main.tex, referencias.bib y las carpetas del experimento y del informe).
- **Problema:** El main.tex quedó en una ruta equivocada porque, al editar desde dentro de una carpeta, GitHub suma la ruta nueva a la actual.
- **Cómo lo resolví:** Con ../ al inicio del nombre subí hasta la raíz y escribí la ruta completa.
- **Tiempo dedicado:** 30 min
- 
## 2026-11-12 (noche)
- **Qué hice:** Verifiqué Docker con `hello-world`, levanté un clúster de 3 servidores de Consul con Docker Compose y ejecuté el experimento: detuve al líder, lo maté de forma abrupta, dejé el clúster sin quórum y lo recuperé. Guardé 12 capturas y la transcripción de PowerShell, y las subí al repo junto con el `docker-compose.yml` y el `comandos.md`.
- **Problemas:** El primer `docker compose up` dijo "empty compose file" porque el archivo había quedado vacío. Además, al matar al líder, `consul1` apareció como `left` y no como `failed`.
- **Cómo lo resolví:** Creé el compose desde PowerShell y verifiqué con `Get-Content`. Para el `left` revisé la configuración de Autopilot y los logs de consul2, y ahí vi el `RemoveServer` de consul1.
- **Tiempo dedicado:** 2 horas


## 2026-11-13
- **Qué hice:** Hice el diagrama final de la arquitectura en draw.io y lo subí al repositorio; busqué y verifiqué las referencias (abrí cada DOI, comprobé en SCImago la indexación de las revistas y comparé el BibTeX con la página de cada artículo); y redacté el informe en LaTeX con las secciones de introducción, arquitectura, análisis, experimentación, ejemplos, comparación, postura crítica y conclusiones.
- **Problema:** El PNG del diagrama se exportó con fondo oscuro y no se leía sobre una página blanca; además, varias referencias no tenían el BibTeX completo, además hubo retrasos en la realización de la actividad por problemas eléctricos.
- **Cómo lo resolví:** Volví a exportar el diagrama en modo claro y revisé campo por campo cada referencia contra su página antes de pegarla en el archivo .bib.
- **Tiempo dedicado:** 6 horas
