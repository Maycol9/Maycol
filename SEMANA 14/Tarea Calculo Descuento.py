# Función que calcula el descuento
def calcular_descuento(monto_total, porcentaje_descuento=10):
    # Calcular el monto del descuento
    descuento = (porcentaje_descuento / 100) * monto_total
    # Retornar el descuento
    return descuento

# Llamadas a la función
monto1 = 1000
monto2 = 1500
porcentaje_descuento2 = 15

# Primer caso: Solo se proporciona el monto total de la compra (10% de descuento por defecto)
descuento1 = calcular_descuento(monto1)
monto_final1 = monto1 - descuento1

# Segundo caso: Se proporciona tanto el monto total como el porcentaje de descuento
descuento2 = calcular_descuento(monto2, porcentaje_descuento2)
monto_final2 = monto2 - descuento2

# Mostrar los resultados
print(f"Caso 1: \nMonto total: {monto1}\nDescuento: {descuento1}\nMonto final a pagar: {monto_final1}\n")
print(f"Caso 2: \nMonto total: {monto2}\nDescuento: {descuento2}\nMonto final a pagar: {monto_final2}\n")
