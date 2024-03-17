def calcular_descuento(monto_total, porcentaje_descuento=23):
    """
    Calcula el descuento aplicando el porcentaje al monto total de la compra.

    Args:
    - monto_total (float): El monto total de la compra.
    - porcentaje_descuento (float): El porcentaje de descuento a aplicar, por defecto es 10.

    Returns:
    - float: El monto del descuento calculado.
    """
    descuento = monto_total * (porcentaje_descuento / 100)
    return descuento


# Llamadas a la función
monto_compra1 = 258
monto_compra2 = 65
porcentaje_descuento2 = 23

descuento1 = calcular_descuento(monto_compra1)
descuento2 = calcular_descuento(monto_compra2, porcentaje_descuento2)

# Resultados
print("Resultados de las llamadas a la función:")
print(
    f"Monto total de la compra: ${monto_compra1}, Descuento: ${descuento1}, Monto final a pagar: ${monto_compra1 - descuento1}")
print(
    f"Monto total de la compra: ${monto_compra2}, Descuento: ${descuento2}, Monto final a pagar: ${monto_compra2 - descuento2}")

