# TA-IND-01 — Análisis crítico de un sistema distribuido real

Informe académico de la asignatura Sistemas Distribuidos (Unidad 1).
Universidad Técnica Estatal de Quevedo, Facultad de Ciencias de la Computación.

## Video de sustentación

Enlace: (pendiente)

## Estructura del repositorio

- `informe/`: código fuente LaTeX (`main.tex`), bibliografía (`referencias.bib`), figuras y capturas.
- `experimento/`: comandos usados y resultados obtenidos.
- `BITACORA.md`: bitácora de trabajo con entradas fechadas.
- `informe.pdf`: PDF compilado del informe.

## Instrucciones de compilación

- **Compilador:** pdfLaTeX con biber para la bibliografía.
- **Archivo principal:** `informe/main.tex`
- **Dependencias:** distribución TeX Live (o MiKTeX) con los paquetes `babel` (español), `graphicx`, `booktabs`, `hyperref` y `biblatex`.

Desde la carpeta `informe/`, ejecutar en este orden:

```bash
pdflatex main.tex
biber main
pdflatex main.tex
pdflatex main.tex
```
