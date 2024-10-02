# Nombre de la tarea: Escritura de Archivo de Texto

# Abrimos (o creamos si no existe) un archivo llamado 'my_notes.txt' en modo escritura ('w')
with open('my_notes.txt', 'w') as file:
    # Escribimos tres líneas de notas personales en el archivo
    file.write("Primera nota: Recordar estudiar todos los días.\n")
    file.write("Segunda nota: No olvidar hacer ejercicio regularmente.\n")
    file.write("Tercera nota: Aprender a organizar mejor mi tiempo.\n")

# Lectura de Archivo de Texto

# Abrimos el archivo 'my_notes.txt' en modo lectura ('r')
with open('my_notes.txt', 'r') as file:
    # Leemos cada línea del archivo y la mostramos en la consola
    for line in file:
        print(line.strip())  # .strip() elimina cualquier salto de línea adicional al imprimir

# No es necesario cerrar manualmente el archivo porque 'with' se encarga de eso automáticamente
