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

## Evidencias bibliográficas — 13 de noviembre de 2026

**Actividades realizadas**

- Comprobé las tres capturas PNG de Fruth y Scherzinger (2024), Kokociński y colaboradores (2023) y Sabaghian y colaboradores (2023): corresponden a las fuentes citadas y sus fragmentos relevantes son legibles.
- Incorporé una subsección de evidencias bibliográficas en los anexos, con las capturas en páginas horizontales, sus citas y explicaciones sobre mantenimiento de Redis Cluster, consistencia ante fallos y replicación.
- Conservé las cinco capturas del experimento y las referencias existentes. Las capturas académicas no tienen resaltados gráficos; las explicaciones se añadieron como texto del informe.
- Ajusté los saltos de línea de dos títulos para evitar que sobresalgan del margen y la versión del PDF de salida para admitir el diagrama existente.
- Compilé con Biber y revisé las citas y la maquetación del PDF: 18 páginas, 21 referencias citadas, sin citas indefinidas ni desbordamientos de cajas. Permanece el aviso de separación silábica española del entorno.

**Dificultad y solución:** MiKTeX muestra avisos de configuración y bloqueo de su base de paquetes. Se utilizó la configuración local existente dentro de mi carpeta para compilar sin cambiar la instalación global.

**Tiempo dedicado:** No registrado.
