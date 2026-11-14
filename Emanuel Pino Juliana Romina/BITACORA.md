# Bitácora de trabajo — TA-IND-01

Registra cada sesión después de realizarla. Usa la fecha real y no completes sesiones anteriores de manera retrospectiva.

## Sesión 1 — 13 de noviembre de 2026

**Actividades realizadas**

- Revisé la estructura del repositorio grupal y la organización de las carpetas de mis compañeros.
- Creé mi carpeta individual con un README y la estructura inicial del informe en LaTeX.
- Preparé las carpetas para diagramas, evidencias y experimento.
- Creé el primer commit con la estructura inicial del trabajo.
- Actualicé el repositorio con `git pull --rebase` e incorporé los cambios remotos.
- Publiqué el primer commit en GitHub.

**Dificultad encontrada:** Al intentar publicar el commit, Git no pudo solicitar las credenciales de forma interactiva.

**Solución:** Inicié sesión y luego pude publicar el commit.

**Tiempo dedicado:** Pendiente de completar.

## Sesión 2 — 13 de noviembre de 2026

**Actividades realizadas**

- Ejecuté el experimento de Redis Cluster con seis nodos: tres primarios y tres réplicas.
- Revisé el estado del clúster y la distribución de los 16 384 slots.
- Guardé la clave `estudiante`, comprobé que correspondía al slot 13012 y la consulté desde otro nodo.
- Probé dos fallos por separado: primero se detuvo `redis-3` y `redis-4` asumió el rol de primario; después `redis-3` volvió como réplica. En otra prueba se detuvo `redis-4` y `redis-3` asumió el rol de primario.
- Guardé las capturas del experimento y documenté los resultados y conclusiones en el informe.

**Dificultades o soluciones:** Pendiente de completar.

**Tiempo dedicado:** Pendiente de completar.
