#Se procedio a definir una matriz bidimensional de 3x3 con valores numéricos.
#Escribe una función que tome esta matriz y un valor como parámetros.
#La función debe recorrer la matriz para buscar el valor.
#Si se encuentra el valor, debe imprimir su posición; de lo contrario, debe indicar que no se encontró.
def search_in_matrix(matrix, target):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == target:
                return f"El valor {target} se encontró en la posición ({i}, {j})"
    return f"El valor {target} no se encontró en la matriz"

# Definir la matriz 3x3
matrix = [
    [5, 8, 3],
    [1, 7, 2],
    [9, 6, 4]
]

# Definir el valor a buscar
target = 7

# Llamar a la función y mostrar el resultado
result = search_in_matrix(matrix, target)
print(result)
