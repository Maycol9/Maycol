# Diccionario  'informacion_personal'
# Con información ficticia sobre una persona
informacion_personal = {
    "Nombre": "Matias Pérez",
    "Edad": 30,
    "Ciudad": "Puyo",
    "Profesion": "Ingeniero"
}

# Acceder al valor de la clave "ciudad" y modificarlo por una ciudad diferente
informacion_personal["Ciudad"] = "Ambato"

# Se procedio agregar una nueva clave-valor que represente la "profesion"
informacion_personal["Profesion"] = "Desarrollador de Software"

# Verificar si la clave "telefono" existe en el diccionario. Si no existe, agregarla con un valor ficticio
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "097-653-6825"

# Eliminar la clave "edad" del diccionario
del informacion_personal["Edad"]

# Imprimir el diccionario resultante
print("Diccionario final después de todas las operaciones:")
print(informacion_personal)
