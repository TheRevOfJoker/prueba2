import requests

# Función para calcular la distancia entre dos ciudades utilizando la API de MapQuest
def calcular_distancia(ciudad_origen, ciudad_destino):
    url = f'http://www.mapquestapi.com/directions/v2/route?key=2mdSiJvcJwtNK46RxzcHc9YKLHpEXtNw&from={ciudad_origen}&to={ciudad_destino}'
    response = requests.get(url)
    data = response.json()
    distancia = data['route']['distance']
    return distancia

# Función para calcular la duración del viaje en horas, minutos y segundos
def calcular_duracion(ciudad_origen, ciudad_destino):
    url = f'http://www.mapquestapi.com/directions/v2/route?key=2mdSiJvcJwtNK46RxzcHc9YKLHpEXtNw&from={ciudad_origen}&to={ciudad_destino}'
    response = requests.get(url)
    data = response.json()
    duracion = data['route']['formattedTime']
    return duracion

# Función para calcular el combustible requerido para el viaje en litros
def calcular_combustible(distancia):
    consumo_litros_por_km = 0.12  # Consumo promedio de combustible por kilómetro
    combustible = distancia * consumo_litros_por_km
    return combustible

# Función para imprimir la narrativa del viaje
def imprimir_narrativa(ciudad_origen, ciudad_destino, distancia, duracion, combustible):
    print(f"Viaje de {ciudad_origen} a {ciudad_destino}:")
    print(f"Distancia: {distancia:.2f} km")
    print(f"Duración: {duracion}")
    print(f"Combustible requerido: {combustible:.2f} litros")

# Programa principal
ciudad_origen = input("Ciudad de Origen: ")
ciudad_destino = input("Ciudad de Destino: ")

distancia = calcular_distancia(ciudad_origen, ciudad_destino)
duracion = calcular_duracion(ciudad_origen, ciudad_destino)
combustible = calcular_combustible(distancia)

imprimir_narrativa(ciudad_origen, ciudad_destino, distancia, duracion, combustible)

# Salida del programa con la letra "q"
while True:
    opcion = input("Presione 'q' para salir: ")
    if opcion.lower() == 'q':
        break