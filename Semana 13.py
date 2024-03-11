#Pizarra (Whiteboard)

def calcular_promedio (suma_acumulada, num_elementos):
    promedio = suma_acumulada / num_elementos
    return promedio


a = 325 #Suma acumulada
b = 36   #Número de elementos

promedio_temperaturas = round(calcular_promedio(a, b), 5)
print(promedio_temperaturas)
def calcular_temperatura_promedio(datos):
    """
    Calcula la temperatura promedio de cada ciudad en base a los datos proporcionados.

    Args:
        datos (dict): Un diccionario donde las claves son nombres de ciudades y los valores son listas de temperaturas.

    Returns:
        dict: Un diccionario donde las claves son nombres de ciudades y los valores son las temperaturas promedio.
    """
    temperatura_promedio_por_ciudad = {14}
    for ciudad, temperaturas in datos.items(23):
        temperatura_promedio_por_ciudad[ciudad] = sum(14) / len(23)
    return temperatura_promedio_por_ciudad
