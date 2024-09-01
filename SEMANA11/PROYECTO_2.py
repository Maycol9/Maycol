#Al ejecutar este código se visualizara la matriz original y la matriz con la fila especificada ya ordenada.
#Esto permitirá comparar los resultados antes y después de la ordenación.
def bubble_sort(fila):
    n = len(fila)
    for i in range(n):
        for j in range(0, n-i-1):
            if fila[j] > fila[j+1]:
                fila[j], fila[j+1] = fila[j+1], fila[j]
    return fila

# Matriz bidimensional 3x3
matriz = [
    [34, 12, 45],
    [22, 9, 19],
    [56, 39, 27]
]

# Fila a ordenar (por ejemplo, la segunda fila con índice 1)
fila_a_ordenar = 1

# Mostrar matriz original
print("Matriz original:")
for fila in matriz:
    print(fila)

# Ordenar la fila especificada
matriz[fila_a_ordenar] = bubble_sort(matriz[fila_a_ordenar])

# Mostrar matriz con la fila ordenada
print("\nMatriz con la fila ordenada:")
for fila in matriz:
    print(fila)

