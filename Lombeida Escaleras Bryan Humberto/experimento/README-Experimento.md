# Experimentación local con Google Spanner

## 1. Descripción y objetivo

Este directorio contiene el programa y las capturas originales de una prueba realizada con el **emulador oficial de Spanner** para la actividad TA-IND-01. El caso utiliza dos cuentas de prueba y una transferencia de 10 unidades. Se observa qué ocurre cuando la transacción se cancela antes de confirmarse y cuando se confirma correctamente.

El objetivo es comprobar, en este entorno local, que una cancelación deja ambos saldos como estaban y que una confirmación aplica los dos cambios. La prueba se relaciona con las transacciones y la coordinación de operaciones sobre datos compartidos. **No es una prueba de replicación, consenso, particiones de red, tolerancia a la caída de una réplica ni rendimiento de Spanner en producción.** [Google documenta estas diferencias del emulador](https://docs.cloud.google.com/spanner/docs/emulator#limitations).

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

## 8. Interpretación y alcance

En esta ejecución local, la cancelación dejó ambos registros con sus valores iniciales y el commit aplicó los dos cambios. Eso es coherente con la atomicidad de una transacción: el conjunto de operaciones se confirma o se revierte como unidad. La conservación del total de 150 permite comprobar además que la transferencia del caso de prueba no creó ni eliminó saldo.

El resultado **no demuestra** que una réplica sobrevivió a una caída, que se alcanzó un quórum Paxos ni que se mantuvo disponibilidad durante una partición. El emulador conserva datos solo en memoria, pierde el estado al reiniciarse y no reproduce el rendimiento ni la escalabilidad de producción. Además, sus transacciones de lectura y escritura bloquean la base completa hasta terminar; por eso no debe utilizarse para inferir el comportamiento de concurrencia de un despliegue real. [Limitaciones oficiales del emulador](https://docs.cloud.google.com/spanner/docs/emulator#limitations).

## 9. Problemas encontrados y solución

| Problema observado | Solución aplicada |
|---|---|
| `docker info` no pudo acceder al socket sin permisos. | Se utilizó `sudo docker info` y `sudo docker` para iniciar y comprobar el contenedor. |
| Python buscó el programa en `/home/bryan/experimento/`. | Se cambió a la carpeta de Bryan dentro del repositorio y se repitió `preparar`. |

## 10. Reproducción y precauciones

1. Comprobar que el contenedor esté activo con `sudo docker ps`.
2. Activar el entorno virtual y exportar `SPANNER_EMULATOR_HOST=localhost:9010`.
3. Situarse en la carpeta de Bryan y ejecutar, en orden, `preparar`, `consultar`, `cancelar` y `confirmar`.
4. Conservar las salidas y capturas originales de una nueva ejecución por separado de las evidencias históricas.

`confirmar` está pensado para ejecutarse una sola vez sobre los saldos iniciales. Reiniciar el emulador elimina **todos** sus datos, esquema y configuración; después de un reinicio se necesitará ejecutar `preparar` de nuevo. No se deben atribuir los resultados de esta prueba local a un clúster distribuido de producción. [Documentación oficial](https://docs.cloud.google.com/spanner/docs/emulator).
