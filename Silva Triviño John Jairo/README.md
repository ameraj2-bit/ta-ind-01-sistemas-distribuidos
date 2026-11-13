# TA-IND-01 — Informe individual de Silva Triviño John Jairo

Asignatura: Sistemas Distribuidos (Unidad 1). Universidad Técnica Estatal de Quevedo.

Sistema analizado: HDFS (Apache Hadoop Distributed File System), comparado con Ceph.

## Video de sustentación

Enlace: (pendiente)

## Contenido de esta carpeta

- `main.tex` y `referencias.bib`: informe en LaTeX y bibliografía.
- `figuras/` y `capturas/`: diagramas y capturas propias.
- `experimento/`: comandos usados y resultados del experimento.
- `BITACORA.md`: bitácora de trabajo con entradas fechadas.
- `informe.pdf`: PDF compilado.

## Instrucciones de compilación

- **Compilador:** pdfLaTeX con biber.
- **Archivo principal:** `main.tex` (ejecutar los comandos desde esta carpeta).
- **Dependencias:** TeX Live o MiKTeX con `babel` (español), `graphicx`, `booktabs`, `hyperref` y `biblatex`.

```bash
pdflatex main.tex
biber main
pdflatex main.tex
pdflatex main.tex
```
