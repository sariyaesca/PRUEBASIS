class Proceso:
    def __init__(self, nombre, tiempo_llegada, duracion):
        self.nombre = nombre
        self.tiempo_llegada = tiempo_llegada
        self.duracion = duracion

def sjf(procesos):
    tiempo_actual = 0
    procesos_ordenados = []
    tiempo_espera_total = 0

    while len(procesos) > 0:
        # Filtrar los procesos que han llegado hasta el tiempo actual
        procesos_disponibles = [p for p in procesos if p.tiempo_llegada <= tiempo_actual]

        if len(procesos_disponibles) == 0:
            # Si no hay procesos disponibles, avanzamos en el tiempo
            tiempo_actual += 1
        else:
            # Ordenar los procesos disponibles por duración
            procesos_disponibles.sort(key=lambda p: p.duracion)
            
            # Tomar el proceso más corto
            proceso_elegido = procesos_disponibles[0]
            procesos_ordenados.append(proceso_elegido)

            # Actualizar el tiempo actual y el tiempo de espera total
            tiempo_actual += proceso_elegido.duracion
            tiempo_espera_total += tiempo_actual - proceso_elegido.tiempo_llegada

            # Eliminar el proceso de la lista de procesos pendientes
            procesos.remove(proceso_elegido)

    return procesos_ordenados, tiempo_espera_total / len(procesos_ordenados)

# Ejemplo de uso
if __name__ == "__main__":
    procesos = [
        Proceso("P1", 0, 6),
        Proceso("P2", 1, 8),
        Proceso("P3", 2, 7),
        Proceso("P4", 3, 3)
    ]

    procesos_ordenados, tiempo_espera_promedio = sjf(procesos)

    print("Procesos en orden de ejecución:")
    for proceso in procesos_ordenados:
        print(f"{proceso.nombre} (Tiempo de espera: {proceso.tiempo_llegada})")

    print(f"Tiempo de espera promedio: {tiempo_espera_promedio}")  