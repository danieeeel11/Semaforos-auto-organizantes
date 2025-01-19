# Semaforos-auto-organizantes

Reglas:
* En cada paso de tiempo agregar a un contador el número de vehículos que se acercan o esperan ante una luz roja a una distancia d. Cuando este contador exceda un umbral n, cambie el semáforo. (Siempre que el semáforo cambia, reiniciar el contador a cero)
* Los semáforos deben permanecer un mínimo de tiempo u en verde
* Si pocos vehículos (m o menos, mayor de cero) están por cruzar una luz verde a una corta distancia r, no cambiar el semáforo (los vehículos que estén cerca del semáforo no frenen de golpe)
* Si no hay un vehículo que se acerque a una luz verde a una distancia d y por lo menos un vehículo se aproxima a una luz roja a una distancia d, entonces cambiar el semáforo
* Si hay un vehículo detenido en el camino a una corta distancia e más allá de una luz verde, cambiar el semáforo
* Si hay vehículos detenidos en ambas direcciones a una corta distancia e más allá de la intersección, entonces cambiar ambas luces a rojo. Cuando una de las direcciones se libere, restaurar la luz verde en esa dirección
