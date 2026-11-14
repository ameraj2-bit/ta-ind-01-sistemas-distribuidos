# TA-IND-01 — Informe individual de Silva Triviño John Jairo
 
Asignatura: Sistemas Distribuidos (Unidad 1). Universidad Técnica Estatal de Quevedo.
 
Sistema analizado: HDFS (Apache Hadoop Distributed File System), comparado con Ceph.
 
## Video de sustentación
 
Enlace: https://youtu.be/15nJaGZGK3E
 
## Contenido de esta carpeta
 
- `informe/main.tex` y `informe/referencias.bib`: informe en LaTeX y bibliografía.
- `informe/informe.pdf`: PDF compilado.
- `informe/VERIFICACION-referencias.md`: lista de comprobación de cada referencia.
- `figuras/`: boceto a mano de la arquitectura (Anexo A).
- `capturas-lectura/`: capturas de lectura anotadas de las fuentes y de verificación de DOI (Anexo B).
- `experimento/`: `docker-compose.yml`, `config`, guion, comandos y salidas (`resultados.md`) y capturas propias (`capturas/`).
- `BITACORA.md`: bitácora de trabajo con entradas fechadas.
## Instrucciones de compilación
 
- **Compilador:** pdfLaTeX con biber.
- **Archivo principal:** `informe/main.tex`. Ejecutar los comandos desde la carpeta `informe/` (el informe carga las imágenes con rutas relativas a las carpetas hermanas `figuras/`, `capturas-lectura/` y `experimento/`).
- **Dependencias:** TeX Live o MiKTeX con `babel` (español), `graphicx`, `booktabs`, `tabularx`, `float`, `xcolor`, `tikz`, `csquotes`, `hyperref` y `biblatex` con `biber`.
```bash
cd informe
pdflatex main.tex
biber main
pdflatex main.tex
pdflatex main.tex
```
 
## Cómo reproducir el experimento
 
Con Docker instalado, desde la carpeta `experimento/`:
 
```bash
docker compose up -d
docker exec namenode hdfs dfsadmin -report
```
 
Los demás comandos y sus salidas están en `experimento/resultados.md`.
