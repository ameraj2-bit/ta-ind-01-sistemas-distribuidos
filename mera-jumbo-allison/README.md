# TA-IND-01: Análisis crítico de un sistema distribuido real

Informe individual de la asignatura Sistemas Distribuidos (Unidad 1).
Universidad Técnica Estatal de Quevedo, Facultad de Ciencias de la Computación.

- **Estudiante:** Mera Jumbo Allison
- **Sistema analizado:** HashiCorp Consul (comparado con etcd)
- **Actividad:** TA-IND-01

## Video de sustentación

Enlace (YouTube, no listado): (https://youtu.be/aIJka9A2_KM)

## Contenido de esta carpeta

- `informe/`: informe en LaTeX.
  - `main.tex`: archivo principal.
  - `referencias.bib`: bibliografía (formato IEEE con biblatex).
  - `informe.pdf`: PDF compilado.
  - `figuras/`: diagrama de arquitectura y esquema inicial a mano (Anexo A).
  - `capturas/`: capturas del experimento y de lectura de las fuentes (Anexo B).
- `experimento/`: comandos usados (`comandos.md`), `docker-compose.yml` del clúster de Consul y la transcripción de la consola en `resultados/`.
- `BITACORA.md`: bitácora de trabajo con entradas fechadas.

## Instrucciones de compilación

- **Compilador:** pdfLaTeX, con biber para la bibliografía.
- **Archivo principal:** `informe/main.tex`
- **Dependencias:** distribución TeX Live o MiKTeX con los paquetes `babel` (español), `geometry`, `graphicx`, `booktabs`, `tabularx`, `array`, `caption`, `float`, `xcolor`, `fvextra`, `biblatex` (con biber) y `hyperref`.

Desde la raíz del repositorio clonado, ejecutar en este orden:

```bash
cd mera-jumbo-allison/informe
pdflatex main.tex
biber main
pdflatex main.tex
pdflatex main.tex
```

El resultado es `main.pdf`. En el repositorio se incluye una copia como `informe.pdf`.

También se puede compilar en Overleaf: subir la carpeta `informe/` completa, elegir pdfLaTeX como compilador y compilar `main.tex`.

## Reproducir el experimento

Requiere Docker. Los comandos y las salidas obtenidas están en `experimento/comandos.md` y en `experimento/resultados/`.
