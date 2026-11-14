# TA-IND-01 — Análisis crítico de Redis y comparación con Valkey

## Datos del trabajo

- **Actividad:** TA-IND-01
- **Tema principal:** Redis
- **Sistema de comparación:** Valkey

## Objetivo general

Analizar críticamente Redis Cluster y compararlo con Valkey, examinando su arquitectura, replicación, consistencia y tolerancia a fallos. Relacionar la documentación y las fuentes académicas con un experimento de Redis Cluster de seis nodos.

## Descripción

El informe contiene el análisis de arquitectura, CAP y PACELC, la comparación documental con Valkey y las pruebas de Redis Cluster. El experimento usa Redis 7.4 con tres primarios y tres réplicas. Las cinco capturas de terminal documentan el estado, la distribución de claves y las pruebas de failover y recuperación. La comparación con Valkey es teórica: no se realizaron pruebas equivalentes con ese sistema.

La bibliografía reúne 21 referencias, seis publicadas entre 2021 y 2026. Los anexos incluyen tres capturas académicas; la verificación bibliográfica y sus enlaces están en [evidencias/fuentes/verificacion_bibliografica.md](evidencias/fuentes/verificacion_bibliografica.md). Las secciones de resumen, transparencias, modelos de comunicación y declaración de uso de IA ya contienen texto. Los pendientes de entrega se indican al final de este archivo.

## Estructura

```text
Emanuel Pino Juliana Romina/
├── README.md
├── BITACORA.md
├── informe/
│   ├── main.tex
│   ├── referencias.bib
│   └── main.pdf                 # Informe compilado
├── diagramas/
│   ├── arquitectura_redis.drawio # Diagrama editable
│   └── arquitectura_redis.pdf    # Diagrama utilizado por el informe
├── evidencias/
│   ├── capturas/                # Cinco capturas del experimento
│   └── fuentes/                # Tres PNG académicas y su verificación
└── experimento/
    ├── docker-compose.yml
    └── README.md                # Procedimiento detallado
```

## Ejecutar el experimento con Docker

Requiere Docker Desktop iniciado, contenedores Linux y Docker Compose v2. Desde esta carpeta individual, abre PowerShell y ejecuta:

```powershell
Set-Location ./experimento
docker compose version
docker compose config --services
docker compose up -d
docker compose ps
```

La configuración define los servicios `redis-1` a `redis-6`, con un volumen por nodo y una red del proyecto `redis-cluster-experimento`. No publica puertos en el host; los comandos se ejecutan dentro de los contenedores.

**Solo en la primera ejecución, con nodos sin datos ni configuración previa**, crea el clúster y confirma con `yes` la distribución propuesta:

```powershell
docker compose exec redis-1 redis-cli --cluster create redis-1:6379 redis-2:6379 redis-3:6379 redis-4:6379 redis-5:6379 redis-6:6379 --cluster-replicas 1
```

Si reutilizas los volúmenes, omite la creación y comprueba el estado. Antes de escribir datos, verifica `cluster_state:ok` y la cobertura de los 16 384 slots:

```powershell
docker compose exec redis-1 redis-cli CLUSTER INFO
docker compose exec redis-1 redis-cli CLUSTER NODES
docker compose exec redis-1 redis-cli --cluster check redis-1:6379
docker compose exec redis-1 redis-cli -c SET estudiante Juliana
docker compose exec redis-2 redis-cli -c GET estudiante
docker compose exec redis-1 redis-cli CLUSTER KEYSLOT estudiante
```

El comando `SET` debe responder `OK` y el `GET` posterior debe devolver `Juliana`. Contrasta la ranura y los roles con las salidas de tu ejecución; los roles pueden cambiar tras un failover. Para cerrar conservando los datos:

```powershell
docker compose down
```

No añadas `-v`: eliminaría los volúmenes. Consulta [experimento/README.md](experimento/README.md) para el procedimiento y las precauciones de reutilización.

## Diagrama y correspondencia con el experimento

El [diagrama](diagramas/arquitectura_redis.pdf) contiene tres primarios y tres réplicas, una por primario, de acuerdo con la topología solicitada por Compose y `--cluster-replicas 1`. Los rótulos «Primario 1–3» y «Réplica 1–3» son esquemáticos: no asignan permanentemente esos roles a los servicios `redis-1` a `redis-6`. Usa `CLUSTER NODES` para conocer la relación concreta en cada ejecución.

Los rangos ilustrados cubren 0–5460, 5461–10922 y 10923–16383. Las líneas del bus son representativas, como indica la leyenda; no dibujan todas las conexiones entre los seis nodos.

## Compilar el informe

El archivo principal es `informe/main.tex`. Se necesita una distribución LaTeX con pdfLaTeX y Biber compatibles entre sí (por ejemplo, MiKTeX o TeX Live), la clase `article` y estos paquetes del preámbulo: `inputenc`, `fontenc`, `babel` con soporte de español, `csquotes`, `graphicx`, `lscape`, `array`, `tabularx`, `biblatex` y `hyperref`. El estilo IEEE requiere `biblatex-ieee`; conviene disponer también de los patrones de separación silábica para español.

Las imágenes y `referencias.bib` deben conservar las rutas relativas del repositorio. Desde esta carpeta individual, ejecuta la secuencia **pdfLaTeX → Biber → pdfLaTeX → pdfLaTeX**:

```powershell
Set-Location ./informe
pdflatex -interaction=nonstopmode -halt-on-error main.tex
biber main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

El PDF actualizado y validado tiene 19 páginas. La compilación utilizó configuración local de MiKTeX por restricciones del entorno; esa caché no se versiona. Conserva en Git el PDF entregable y las fuentes, sin los archivos auxiliares de LaTeX.

## Pendientes

- **Informe:** realizar la revisión final del contenido y contrastarlo con la rúbrica original.
- **Evidencias académicas:** añadir los resaltados o anotaciones gráficos exigidos; las tres capturas actuales se acompañan de explicaciones en el informe.

## Video de sustentación: Redis Cluster y comparación con Valkey

[Ver video de sustentación en Google Drive](https://drive.google.com/drive/folders/1U7m1mCY4ImmxXPOMoHQ_06rKP3Zucsgf?usp=sharing)
