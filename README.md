# TA-IND-01 — Análisis crítico de un sistema distribuido real

Informe académico de la asignatura Sistemas Distribuidos (Unidad 1).
Universidad Técnica Estatal de Quevedo, Facultad de Ciencias de la Computación.

Este repositorio reúne el trabajo de los cuatro integrantes del grupo. **Cada integrante tiene su propia carpeta**, con su informe en LaTeX, su bibliografía, sus capturas, su experimento, su bitácora y su video. Cada carpeta se compila de forma independiente.

## Integrantes y carpetas

| Integrante | Carpeta | Sistema analizado |
|---|---|---|
| Emanuel Pino Juliana Romina | `(completar nombre de la carpeta)/` | (completar) |
| Lombeida Escaleras Bryan Humberto | `Lombeida Escaleras Bryan Humberto/` | (completar) |
| Mera Jumbo Allison Michelle | `mera-jumbo-allison/` | Apache Kafka (comparado con RabbitMQ)  |
| Silva Triviño John Jairo | `Silva Triviño John Jairo/` | Apache Cassandra (comparado con MongoDB) |

## Qué contiene cada carpeta

- `main.tex` y `referencias.bib`: informe en LaTeX y bibliografía.
- `figuras/` y `capturas/`: diagramas y capturas propias del integrante.
- `experimento/`: comandos usados y resultados del experimento.
- `BITACORA.md`: bitácora con entradas fechadas.
- `README.md`: enlace al video de sustentación e instrucciones de compilación de ese informe.
- PDF compilado del informe.

## Video de sustentación

Cada integrante publica el enlace de su video en el `README.md` de su carpeta.

## Instrucciones de compilación

- **Compilador:** pdfLaTeX con biber para la bibliografía.
- **Archivo principal:** `main.tex` dentro de la carpeta de cada integrante (ver su README, porque algunas carpetas lo tienen dentro de `informe/`).
- **Dependencias:** distribución TeX Live (o MiKTeX) con los paquetes `babel` (español), `graphicx`, `booktabs`, `hyperref` y `biblatex`.

Desde la carpeta del integrante, ejecutar en este orden:

```bash
pdflatex main.tex
biber main
pdflatex main.tex
pdflatex main.tex
```
