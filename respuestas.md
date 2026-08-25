# Respuestas - Actividad práctica: trabajo colaborativo con Pull Requests

**Equipo:** Juan Manuel Goncalves de Faria y Esteban Faria

## 1. ¿Por qué es conveniente trabajar con ramas en lugar de modificar directamente main?

Porque las ramas permiten desarrollar cada funcionalidad de forma **aislada**. Además, permite que varias personas trabajen en paralelo sobre lo mismo proyecto sin pisarse, y que cada cambio sea revisado antes de integrarse.

## 2. ¿Cuál es la diferencia entre un Pull Request y un merge?

El **merge** es una operación de Git que combina dos historias de cambios en una sola. El **Pull Request** es un mecanismo de colaboración que ofrecen plataformas como GitHub: consiste en *solicitar* incorporar los cambios de una rama a otra, acompañado de un proceso de discusión, aprobaciones y controles automáticos. Un PR normalmente termina en un merge, pero el concepto es más amplio: incluye todo el proceso de revisión previo.

## 3. ¿Qué ventajas aporta el Code Review?

Permite que otro desarrollador analice el código antes de integrarlo: detecta errores temprano, mejora la calidad y seguridad, verifica el cumplimiento de convenciones del equipo y difunde conocimiento del proyecto entre los integrantes. También funciona como control de calidad humano que complementa a los tests automáticos.

## 4. ¿Qué ocurre cuando realizamos un nuevo push sobre una rama que tiene un Pull Request abierto?

El Pull Request **se actualiza automáticamente** el PR no representa archivos congelados, sino el estado actual de la rama comparada contra su destino.

## 5. ¿Por qué pueden producirse conflictos aunque utilicemos Pull Requests?

Porque los Pull Requests detectan pero **no resuelven** incompatibilidades: si dos ramas modifican las mismas líneas de un mismo archivo, Git no puede decidir automáticamente cuál cambio es el correcto.

## 6. ¿Qué función cumple la protección de la rama main?

Convierte a main en una rama protegida donde nadie puede pushear directamente: los cambios solo pueden ingresar mediante Pull Requests. Así se garantiza que solo código revisado y validado llegue a la rama principal.

## 7. ¿Qué ventajas tiene utilizar tests automáticos dentro de un Pull Request?

Los tests automáticos (CI) validan objetivamente cada PR al momento de crearse o actualizarse: compilación, pruebas y análisis de estilo se ejecutan solos y también esto bloquea regresiones antes del merge y reduce la carga del reviewer.
