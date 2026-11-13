# Experimentación local con Google Spanner

## 1. Descripción y objetivo

Este directorio reúne el programa y las capturas de una transferencia de prueba y de una interrupción controlada del emulador de Google Spanner. La transferencia permite observar una cancelación y una confirmación. La interrupción permite comprobar cómo cambia la respuesta del cliente al detener el contenedor, reiniciarlo y volver a preparar sus datos.

## 2. Entorno utilizado

| Componente | Configuración observada |
|---|---|
| Equipo y usuario | `bryan`, usuario `bryan` |
| Sistema operativo | Omarchy sobre Linux, según la salida de `sudo docker info` |
| Docker cliente y servidor | 29.9.2 |
| Emulador | Imagen `gcr.io/cloud-spanner-emulator/emulator`, contenedor `spanner-ta-ind-01` |
| Puertos publicados | `9010` para gRPC y `9020` para REST |
| Python | 3.14.8 |
| Biblioteca | `google-cloud-spanner` 3.72.0, instalada en un entorno virtual local |
| Proyecto de prueba | `ta-ind-01-local` |
| Instancia / base de datos | `spanner-bryan` / `transferencias-bryan` |

El identificador del proyecto es local para el emulador; el procedimiento no crea recursos facturables en Google Cloud. La imagen de Docker se obtuvo sin fijar un digest, por lo que una descarga futura puede usar otra versión. [Documentación del emulador](https://docs.cloud.google.com/spanner/docs/emulator).

## 3. Archivos y evidencias

| Archivo | Contenido |
|---|---|
| [`prueba_spanner.py`](prueba_spanner.py) | Programa con las etapas `preparar`, `consultar`, `cancelar` y `confirmar`. |
| [`ComprobarDocker1.png`](ComprobarDocker1.png) y [`ComprobarDocker2.png`](ComprobarDocker2.png) | Comprobación de Docker y acceso al servidor con `sudo`. |
| [`IniciarEmulador-ComprobacionDocker.png`](IniciarEmulador-ComprobacionDocker.png), [`IniciarEmulador-CorrerEmuladorDocker.png`](IniciarEmulador-CorrerEmuladorDocker.png), [`IniciarEmulador-UltimaImagen.png`](IniciarEmulador-UltimaImagen.png) y [`IniciarEmulador-ComprobacionEnLazyDocker.png`](IniciarEmulador-ComprobacionEnLazyDocker.png) | Descarga, inicio y comprobación visual del contenedor. |
| [`InstalacionBiblioteca-EntornoAislado.png`](InstalacionBiblioteca-EntornoAislado.png) y [`ExportacionYComprobacion-EntornoAislado.png`](ExportacionYComprobacion-EntornoAislado.png) | Instalación e importación de la biblioteca cliente. |
| [`PreparacionEntorno.png`](PreparacionEntorno.png) | Creación de la instancia, base, tabla y saldos iniciales; también conserva un primer intento con una ruta incorrecta. |
| [`EjecucionConsulta.png`](EjecucionConsulta.png) | Consulta de los saldos iniciales. |
| [`EjecucionCancelacion.png`](EjecucionCancelacion.png) | Cancelación deliberada y comprobación posterior. |
| [`EjecucionConfirmar.png`](EjecucionConfirmar.png) | Commit y comprobación de los saldos finales. |

Las capturas muestran la terminal del estudiante, su usuario, el nombre del equipo y la fecha y hora. Se conservan como imágenes originales; este documento describe lo que se ve en ellas.

## 4. Preparación del emulador

### 4.1. Comprobación de Docker

En Linux se ejecutaron `docker --version` y `docker info`. El cliente estaba disponible, pero la conexión inicial al socket de Docker devolvió un error de permisos. `sudo docker info` sí mostró el servidor activo, versión 29.9.2, inicialmente sin imágenes ni contenedores. Véanse [`ComprobarDocker1.png`](ComprobarDocker1.png) y [`ComprobarDocker2.png`](ComprobarDocker2.png).

En una reproducción, verificar primero:

```bash
docker --version
sudo docker info
```

### 4.2. Descarga e inicio

Se utilizó la [imagen oficial indicada por Google](https://docs.cloud.google.com/spanner/docs/emulator):

```bash
sudo docker pull gcr.io/cloud-spanner-emulator/emulator
sudo docker run -d --name spanner-ta-ind-01 \
  -p 9010:9010 -p 9020:9020 \
  gcr.io/cloud-spanner-emulator/emulator
sudo docker ps
```

**Resultado observado:** `sudo docker ps` mostró el contenedor `spanner-ta-ind-01` en estado `Up`, con los puertos 9010 y 9020 publicados. Las capturas de inicio están listadas en la sección 3. Si se repite la práctica en el mismo equipo y el contenedor ya existe, comprobar su estado antes de intentar crear otro con el mismo nombre.

## 5. Biblioteca Python y conexión local

Se creó un entorno virtual y se instaló la [biblioteca cliente de Spanner para Python](https://pypi.org/project/google-cloud-spanner/):

```bash
python -m venv /tmp/spanner-ta-ind-01-venv
source /tmp/spanner-ta-ind-01-venv/bin/activate
python -m pip install google-cloud-spanner
export SPANNER_EMULATOR_HOST=localhost:9010
python -c "import google.cloud.spanner; print('Biblioteca de Spanner disponible')"
```

**Resultado observado:** la importación devolvió `Biblioteca de Spanner disponible`. La variable `SPANNER_EMULATOR_HOST` dirige la biblioteca al emulador local por gRPC. El programa también comprueba esa variable antes de conectar, para evitar ejecutar la práctica por accidente contra un servicio remoto. La variable debe volver a exportarse en cada terminal nueva. [Configuración oficial del cliente para el emulador](https://docs.cloud.google.com/spanner/docs/emulator#use-the-client-libraries-with-the-emulator).

## 6. Preparación de los datos

Los comandos siguientes se ejecutan **desde la carpeta de Bryan en el repositorio**, con el entorno virtual activado y `SPANNER_EMULATOR_HOST=localhost:9010`.

```bash
whoami
hostname
date '+%Y-%m-%d %H:%M:%S %Z'
python experimento/prueba_spanner.py preparar
```

El programa crea la instancia `spanner-bryan`, la base `transferencias-bryan` y la tabla `Cuentas(CuentaId, Titular, Saldo)`. Inserta dos filas: `Bryan` con saldo 100 y `Destino de prueba` con saldo 50. Si la base ya existe, `preparar` no borra ni duplica los datos.

**Resultado observado:** se imprimieron los saldos 100 y 50, con un total de 150. La primera ejecución se intentó desde `/home/bryan` y Python no encontró `experimento/prueba_spanner.py`; al cambiar a la carpeta correcta se completó la preparación. Véase [`PreparacionEntorno.png`](PreparacionEntorno.png).

## 7. Procedimiento de la prueba

Antes de cada captura se mostraron `whoami`, `hostname` y `date` para conservar evidencia del entorno y momento de ejecución.

### 7.1. Consulta inicial

```bash
python experimento/prueba_spanner.py consultar
```

**Resultado observado:** cuenta 1 = 100, cuenta 2 = 50 y total = 150. Véase [`EjecucionConsulta.png`](EjecucionConsulta.png).

### 7.2. Cancelación antes del commit

```bash
python experimento/prueba_spanner.py cancelar
```

El programa lee los dos saldos, prepara cambios a 90 y 60 dentro de una transacción y provoca una excepción deliberada **antes del commit**. La biblioteca ejecuta el rollback y el programa vuelve a consultar los datos.

**Resultado observado:** apareció el mensaje de cancelación y los saldos permanecieron en 100 y 50; el total siguió en 150. Véase [`EjecucionCancelacion.png`](EjecucionCancelacion.png).

### 7.3. Confirmación de la transferencia

```bash
python experimento/prueba_spanner.py confirmar
```

Con los saldos iniciales intactos, el programa vuelve a preparar los dos cambios y permite el commit. Tiene una comprobación que impide repetir esta etapa si los saldos ya no son 100 y 50.

**Resultado observado:** el programa indicó `Commit completado`; la cuenta 1 quedó en 90 y la cuenta 2 en 60. El total continuó en 150. Véase [`EjecucionConfirmar.png`](EjecucionConfirmar.png).

| Momento | Cuenta 1 | Cuenta 2 | Total | Evidencia |
|---|---:|---:|---:|---|
| Antes de la prueba | 100 | 50 | 150 | `EjecucionConsulta.png` |
| Después de cancelar | 100 | 50 | 150 | `EjecucionCancelacion.png` |
| Después de confirmar | 90 | 60 | 150 | `EjecucionConfirmar.png` |

## 8. Interrupción y recuperación del emulador

La prueba se ejecutó el 13 de noviembre de 2026 desde la carpeta del estudiante. Se utilizó la misma consulta en cada etapa y se registró la respuesta del cliente.

### Estado previo y detención

```bash
source /tmp/spanner-ta-ind-01-venv/bin/activate
export SPANNER_EMULATOR_HOST=localhost:9010
sudo docker ps
python experimento/prueba_spanner.py consultar
sudo docker stop spanner-ta-ind-01
sudo docker ps -a
timeout 15s python experimento/prueba_spanner.py consultar
printf 'Código de salida: %s\n' "$?"
```

### Reinicio y preparación de datos

```bash
sudo docker start spanner-ta-ind-01
sudo docker ps
timeout 15s python experimento/prueba_spanner.py consultar
printf 'Código de salida: %s\n' "$?"
```

Después de registrar la respuesta del emulador recién iniciado, se recrearon los datos:

```bash
source /tmp/spanner-ta-ind-01-venv/bin/activate
export SPANNER_EMULATOR_HOST=localhost:9010
python experimento/prueba_spanner.py preparar
python experimento/prueba_spanner.py consultar
```

| Etapa | Resultado observado | Captura |
|---|---|---|
| Antes de detener el emulador | La consulta devolvió 90 y 60. | [Consulta de referencia](ComprobacionInicialAntesExperimento.png) |
| Contenedor detenido | El comando alcanzó el límite externo de 15 segundos y salió con código 124. | [Contenedor detenido](DetencionEmulador-ProbarConsulta.png) |
| Después del reinicio | El contenedor estaba activo y la consulta devolvió `Instance not found`. Python salió con código 1. | [Respuesta gRPC](ReinicioRecuperacion-Parte1.png) y [salida de Python](ReinicioRecuperacion-Parte2.png) |
| Después de preparar los datos | El programa creó la instancia y la tabla. La consulta devolvió los saldos iniciales de 100 y 50. | [Preparación y consulta correctas](ComprobacionFalloYRecuperacionEmulador.png) |

## 9. Interpretación y alcance

La interrupción fue visible desde el cliente en dos formas. Con el contenedor detenido, la consulta quedó sin completar dentro del límite fijado. Después del reinicio, el servidor respondió indicando que la instancia anterior no existía. Para volver a consultar hubo que crear una instancia y cargar datos iniciales. Los saldos de 100 y 50 corresponden a esa nueva carga. El alcance de esta prueba es la comunicación entre el cliente y el emulador local, cuyo estado se guarda en memoria. [Documentación oficial del emulador](https://docs.cloud.google.com/spanner/docs/emulator).

## 10. Problemas encontrados y solución

| Problema observado | Solución aplicada |
|---|---|
| `docker info` no pudo acceder al socket sin permisos. | Se utilizó `sudo docker` para iniciar y comprobar el contenedor. |
| Python buscó el programa en `/home/bryan/experimento/`. | Se cambió a la carpeta del estudiante y se repitió `preparar`. |
| Al intentar preparar los datos después del reinicio, Python devolvió `ModuleNotFoundError: No module named 'google'`. [Captura del intento](VolverPreparacionDatos.png). | Se activó el entorno virtual, se exportó `SPANNER_EMULATOR_HOST` y se repitieron `preparar` y `consultar`. |

Para reproducir la secuencia completa, ejecutar primero los pasos de la transferencia de la sección 7 y después los de la sección 8. Al detener el emulador para esta prueba se perderán sus datos en memoria.
