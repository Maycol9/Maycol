#Esta es una lista que contiene las temperaturas registradas en tres ciudades (Quito, Cuenca y Guayaquil) durante 7 días. Para cada día, se registran tres temperaturas (por ejemplo, mañana, tarde y noche).

# La Lista de los nombres de las tres ciudades: Quito, Cuenca y Guayaquil.

# Al Recorrer las ciudades: Un ciclo for itera a través del índice de las ciudades en el arreglo. En cada iteración, se imprime el nombre de la ciudad correspondiente.

# Tiene como objetivo recorrer los días: Dentro de cada ciudad, se recorre cada uno de los 7 días en un segundo ciclo for.

#Acumulando las temperaturas: Para cada día, se suman las tres temperaturas registradas usando un ciclo for interno, que itera sobre las temperaturas de ese día.

#Cálculando el promedio: Una vez sumadas las tres temperaturas de un día, se calcula el promedio dividiendo la suma entre 3 (el número de temperaturas por día).

#La salida de los resultados: Para cada día, se imprime el promedio de las temperaturas calculado con dos decimales de precisión.
arreglo_temperaturas = [
    # Quito
    [
        [10, 15, 11], [30, 56, 24], [23, 21, 25], [17, 25, 30], [27, 70, 59], [25, 32, 68], [37, 24, 62]
    ],
    # Cuenca
    [
        [19, 50, 40], [10, 13, 15], [14, 17, 10], [18, 13, 15], [12, 18, 24], [13, 16, 17], [13, 14, 25]
    ],
    # Guayaquil
    [
        [16, 38, 54], [45, 66, 74], [33, 24, 45], [87, 71, 14], [74, 68, 56], [19, 81, 17], [34, 23, 20]
    ]
]

# Lista con los nombres de las ciudades
ciudades = ["Quito", "Cuenca", "Guayaquil"]

# Recorrer las ciudades
for ciudad in range(len(arreglo_temperaturas)):
    print(f"Ciudad: {ciudades[ciudad]}")

    # Recorrer los días
    for dia in range(len(arreglo_temperaturas[ciudad])):
        acumulador = 0

        # Recorrer las temperaturas de cada día
        for temperatura in arreglo_temperaturas[ciudad][dia]:
            acumulador += temperatura

        # Calcular el promedio de temperaturas para ese día
        promedio = acumulador / len(arreglo_temperaturas[ciudad][dia])
        print(f"  Día {dia + 1}: Promedio de temperatura = {promedio:.2f}")


def calcular_promedio_temperaturas(arreglo_temperaturas, ciudades):
    promedios_por_ciudad = {}

    # Recorrer las ciudades
    for ciudad in range(len(arreglo_temperaturas)):
        print(f"Ciudad: {ciudades[ciudad]}")

        total_temperaturas = 0
        total_dias = 0

        # Recorrer los días
        for dia in range(len(arreglo_temperaturas[ciudad])):
            acumulador = 0

            # Recorrer las temperaturas de cada día
            for temperatura in arreglo_temperaturas[ciudad][dia]:
                acumulador += temperatura

            # Calcular el promedio de temperaturas para ese día
            promedio = acumulador / len(arreglo_temperaturas[ciudad][dia])
            total_temperaturas += promedio
            total_dias += 1
            print(f"  Día {dia + 1}: Promedio de temperatura = {promedio:.2f}")

        # Calcular el promedio semanal de la ciudad
        promedio_semanal = total_temperaturas / total_dias
        promedios_por_ciudad[ciudades[ciudad]] = promedio_semanal
        print(f"Promedio semanal de temperatura en {ciudades[ciudad]} = {promedio_semanal:.2f}\n")

    return promedios_por_ciudad



ciudades = ["Quito", "Cuenca", "Guayaquil"]

promedios = calcular_promedio_temperaturas(arreglo_temperaturas, ciudades)
print("Promedios de temperatura por ciudad:", promedios)
