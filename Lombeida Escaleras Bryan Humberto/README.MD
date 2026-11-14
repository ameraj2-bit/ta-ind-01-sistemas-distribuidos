# TA-IND-01 · Análisis crítico de Google Spanner

Informe académico individual de **Bryan Humberto Lombeida Escaleras** para la asignatura Aplicaciones Distribuidas. El trabajo analiza la arquitectura y el comportamiento de Google Spanner, lo compara con Amazon DynamoDB y documenta una prueba con el emulador local de Spanner.

## Video de sustentación

- **Enlace del video en YouTube:** [https://youtu.be/BIcxJ_XgQCg](https://youtu.be/BIcxJ_XgQCg)
- **Descripción:** Video de sustentación individual explicando la arquitectura de la prueba experimental con el emulador de Google Spanner en Docker, la consulta de datos iniciales vía gRPC, la detención del contenedor y detección de fallos por timeout, y el posterior reinicio y recuperación del servicio.

## Compilación del informe

- **Archivo principal:** [main.tex](main.tex).
- **Compilador:** pdfLaTeX o XeLaTeX. Biber procesa las citas y genera la bibliografía.
- **Formato:** A4, una columna, tipografía de estilo Times de 11 pt y márgenes de 2,54 cm. Las citas y la bibliografía usan el estilo IEEE.
- **Dependencias:** una distribución de LaTeX con la clase `article`, pdfLaTeX y Biber. El informe usa `biblatex`, `biblatex-ieee`, `inputenc`, `fontenc`, `babel` con español e inglés, `csquotes`, `graphicx`, `booktabs`, `hyperref`, `mathptmx`, `geometry`, `microtype`, `setspace`, `titlesec`, `fancyhdr`, `float`, `tabularx`, `array`, `caption`, `pdflscape`, `xcolor` y `xurl`. También se requiere `iftex`.
  - **Fuentes y paquetes del sistema:**
    - En **Arch Linux**: requiere los paquetes `texlive-fontsrecommended` (provee las fuentes y métricas de Times/PSNFSS como `ptmr8t` necesarias para `mathptmx`) y `texlive-bibtexextra` (provee `biblatex-ieee`). Si se utiliza XeLaTeX, se requiere además `texlive-xetex`.
    - En **Ubuntu / Debian**: requiere `texlive-latex-extra`, `texlive-fonts-recommended`, `texlive-bibtex-extra` y `biber` (y `texlive-xetex` si se usa XeLaTeX).
    - En **Windows**:
      - Con **MiKTeX**: no es necesario instalar las dependencias manualmente. Durante la instalación, active la opción *“Install missing packages on-the-fly: Yes”*. Al compilar por primera vez, MiKTeX detecta y descarga automáticamente `mathptmx`, `biblatex-ieee`, `csquotes` y cualquier paquete faltante.
      - Con **TeX Live (Windows)**: se recomienda seleccionar el esquema completo (*scheme-full*) durante el instalador (`install-tl-windows.exe`), el cual incluye todas las fuentes, motores (`pdflatex`, `xelatex`), paquetes y `biber` listos para usar sin instalaciones adicionales.
  - Con pdfLaTeX se usan `mathptmx` y las métricas y fuentes Times de PSNFSS (`texlive-fontsrecommended`). Con XeLaTeX se usan `fontspec` y las fuentes Nimbus Roman, Nimbus Sans y Nimbus Mono PS (URW Base35), además de las fuentes base de la distribución (Latin Modern y Zapf Dingbats).
- **Archivos del proyecto:** conserve `ieee-config.sty`, `referencias.bib` y las carpetas de imágenes en su ubicación dentro del repositorio para que LaTeX encuentre los recursos.

Abra una terminal en esta carpeta y ejecute los comandos en el orden indicado:

```bash
pdflatex main.tex
biber main
pdflatex main.tex
pdflatex main.tex
```

Si la instalación de pdfLaTeX no dispone de las fuentes Times, use XeLaTeX con sus dependencias instaladas:

```bash
xelatex main.tex
biber main
xelatex main.tex
xelatex main.tex
```

El resultado es `main.pdf`. Las dos últimas pasadas actualizan las referencias cruzadas y los números de las citas.

## Experimento

El [README del experimento](experimento/README-Experimento.md) incluye los requisitos, los comandos para reproducir la prueba, los resultados observados y los enlaces a las capturas originales.
