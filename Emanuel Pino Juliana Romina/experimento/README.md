# Experimento Redis Cluster

Este entorno prepara seis nodos Redis 7.4 para formar un clúster de prueba con
tres primarios y tres réplicas. Los servicios, la red y los volúmenes pertenecen
al proyecto Compose `redis-cluster-experimento`; no se publican puertos en el
host ni se conectan contenedores de otros proyectos.

Cada nodo tiene un volumen independiente en `/data`. AOF está habilitado y el
timeout de clúster es de 5000 ms. La red interna usa los nombres DNS de los
servicios; Redis anuncia el puerto de cliente `6379` y el bus de clúster `16379`.

## Requisitos

- Docker Desktop iniciado.
- Docker Compose v2 disponible desde PowerShell como `docker compose`.
- La imagen `redis:7.4` descargada localmente.

Ejecuta los comandos de las siguientes secciones desde esta carpeta.

## 1. Iniciar los seis nodos

```powershell
docker compose up -d
docker compose ps
```

Espera a que los seis servicios estén en ejecución antes de crear el clúster.

## 2. Crear el clúster

Este comando solicita confirmación en la terminal. Escribe `yes` cuando
`redis-cli` muestre la distribución propuesta:

```powershell
docker compose exec redis-1 redis-cli --cluster create redis-1:6379 redis-2:6379 redis-3:6379 redis-4:6379 redis-5:6379 redis-6:6379 --cluster-replicas 1
```

La opción `--cluster-replicas 1` solicita una réplica por cada primario.

## 3. Verificar los nodos y el estado

Lista los seis nodos y revisa sus roles y la relación de replicación:

```powershell
docker compose exec redis-1 redis-cli -h redis-1 -p 6379 CLUSTER NODES
```

Comprueba también la cobertura de slots y el estado del clúster:

```powershell
docker compose exec redis-1 redis-cli --cluster check redis-1:6379
```

En la salida de `CLUSTER NODES`, verifica que haya tres nodos primarios (`master`)
y tres réplicas (`slave` en esta versión), y que cada réplica indique su primario.
La comprobación de slots debe indicar cobertura completa antes de continuar.

## 4. Insertar y consultar un dato

El cliente `redis-cli -c` sigue las redirecciones del clúster si la clave
corresponde a otro nodo:

```powershell
docker compose exec redis-1 redis-cli -c -h redis-1 -p 6379 SET demo:mensaje TAIND01_demo
docker compose exec redis-1 redis-cli -c -h redis-1 -p 6379 GET demo:mensaje
```

Guarda las salidas reales de las verificaciones y pruebas en `evidencias/`;
no se incluyen resultados anticipados en este archivo.

## 5. Cierre del experimento

Detén y elimina los contenedores y la red del proyecto, conservando los
volúmenes con los datos:

```powershell
docker compose down
```

No agregues `-v` a este comando: esa opción elimina también los volúmenes
persistentes. Para volver a iniciar el experimento, ejecuta `docker compose up
-d` y verifica el estado del clúster antes de continuar.
