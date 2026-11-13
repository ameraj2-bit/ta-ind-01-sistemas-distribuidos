# Experimento: tolerancia a fallos y quórum en Consul

Sistema: HashiCorp Consul 1.20.6 (imagen `hashicorp/consul:1.20`), clúster de 3 servidores en Docker.
Fecha: 12 de noviembre de 2026. Máquina: DESKTOP-BSCEF4D, usuario `desktop-bscef4d\pc`.
Entorno: Windows, PowerShell 5.1, Docker 29.9.3, Docker Desktop 4.99.0.

## Objetivo

Observar qué ocurre en un clúster Raft de 3 nodos cuando el líder se detiene, cuando se mata de forma abrupta y cuando se pierde la mayoría.

## Preparación (antes de la transcripción)

```powershell
whoami
hostname
Get-Date
docker --version
docker run hello-world
mkdir $HOME\consul-experimento
cd $HOME\consul-experimento
docker compose up -d
docker ps
docker exec consul1 consul members
docker exec consul1 consul operator raft list-peers
```

El archivo `docker-compose.yml` define consul1, consul2 y consul3 como servidores con `-bootstrap-expect=3`.

## Pruebas (registradas en `resultados/resultado-experimento.txt`)

### A. Línea base
```powershell
docker exec consul1 consul kv put prueba/clave "valor-antes-de-la-falla"
docker exec consul1 consul kv get prueba/clave
docker exec consul1 consul operator raft list-peers
```
Observado: líder consul2, commit index 98 en los tres nodos.

### B. Detención ordenada del líder
```powershell
docker stop consul2
docker exec consul1 consul operator raft list-peers
docker exec consul1 consul kv put prueba/clave "valor-despues-de-la-falla"
docker exec consul1 consul members
docker logs consul2 --tail 15
```
Observado: nuevo líder consul1; el dato anterior se conservó; la escritura con 2 de 3 nodos funcionó; consul2 apareció como `left`.

### C. Reincorporación de consul2
```powershell
docker start consul2
docker exec consul1 consul members
docker exec consul1 consul operator raft list-peers
```
Observado: los tres nodos `alive`, consul2 follower, commit index 195.

### D. Muerte abrupta del líder
```powershell
docker kill consul1
docker exec consul2 consul members
docker exec consul2 consul operator raft list-peers
docker exec consul2 consul operator autopilot get-config
docker logs consul2 2>&1 | Select-String -Pattern "updating configuration|RemoveServer|autopilot"
docker inspect consul1 --format '{{.State.FinishedAt}}'
```
Observado: nuevo líder consul2; consul1 apareció como `left` y salió de la lista de Raft; `CleanupDeadServers = true`; el log muestra `RemoveServer` de consul1.
Horas en UTC: consul1 terminó a las 02:26:34.235; el log de consul2 registra `reconciliation now enabled` a las 02:26:43.265 y la retirada de consul1 a las 02:26:44.642.

### E. Reincorporación de consul1
```powershell
docker start consul1
docker exec consul2 consul members
docker exec consul2 consul operator raft list-peers
```
Observado: consul1 volvió solo como follower; commit index 321; las direcciones IP de consul1 y consul3 cambiaron respecto a antes, con los mismos ID de Raft.

### F. Pérdida del quórum
```powershell
docker kill consul1 consul3
docker exec consul2 consul operator raft list-peers
docker exec consul2 consul kv put prueba/clave "valor-sin-quorum"
docker exec consul2 consul kv get prueba/clave
docker exec consul2 consul kv get -stale prueba/clave
```
Observado: `list-peers`, `put` y `get` fallaron con error 500 `No cluster leader`; `get -stale` devolvió `valor-despues-de-la-falla`.

### G. Recuperación
```powershell
docker start consul1 consul3
docker exec consul2 consul members
docker exec consul2 consul operator raft list-peers
docker exec consul2 consul kv put prueba/clave "valor-tras-recuperar-quorum"
docker exec consul2 consul kv get prueba/clave
Stop-Transcript
```
Observado: tres nodos `alive`, líder consul2, commit index 362, escritura exitosa.

## Capturas (carpeta `informe/capturas/`)

Ajusta esta lista a los nombres reales de tus archivos.

- 01: Docker funcionando (`hello-world`).
- 02: clúster levantado, con miembros y líder.
- 03: escritura previa a la falla.
- 04: líder detenido con `docker stop`.
- 05: reincorporación de consul2.
- 06: líder muerto con `docker kill`.
- 07 y 08: configuración de Autopilot y retirada de consul1 en los logs.
- 09: hora de término de consul1 según Docker.
- 10: reincorporación de consul1.
- 11: clúster sin quórum.
- 12: quórum recuperado.

## Limitaciones

- Una sola ejecución de cada prueba, en un solo equipo y con contenedores Docker; no representa un despliegue en producción.
- Las pruebas de la sección B y D se hicieron comando por comando, así que los tiempos entre `Get-Date` incluyen mi tiempo de escritura.

## Interpretación

La interpretación de estos resultados se desarrolla en la sección
«Experimentación propia» del informe (`informe/main.tex`).
