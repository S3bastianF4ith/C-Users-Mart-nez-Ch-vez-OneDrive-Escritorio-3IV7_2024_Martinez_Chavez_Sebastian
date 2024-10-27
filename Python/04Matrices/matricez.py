def ingresar_matriz(tamano):
    matriz = []

    print(f"Introduce los valores de la matriz de {tamano} x {tamano}")
    for i in range(tamano):
        fila = []  # Inicializar la fila aquí
        for j in range(tamano):
            valor = float(input(f"Elemento: [{i + 1}] [{j + 1}]: "))  # Usar f-string para formatear
            fila.append(valor)
        matriz.append(fila)  # Agregar la fila completa a la matriz
    return matriz  # Devolver la matriz completa

def transponer_matriz(matriz):
    tamano = len(matriz)  # Obtener el tamaño de la matriz
    matriz_transpuesta = []
    for j in range(tamano):
        fila = []
        for i in range(tamano):
            fila.append(matriz[i][j])
        matriz_transpuesta.append(fila)
    return matriz_transpuesta  # Devolver la matriz transpuesta

def imprimir_matriz(matriz):
    for fila in matriz:
        print(fila)  # Imprimir cada fila de la matriz

# Programa principal
while True:
    # Elegir tamaño de matriz
    tamano = input("¿Quieres crear una matriz de 3x3 o 5x5? (escribe 3 o 5): ")
    if tamano in ['3', '5']:
        tamano = int(tamano)
        break
    else:
        print("Opción no válida. Por favor elige 3 o 5.")

# Ingresar y mostrar la matriz
print(f"\nMatriz {tamano}x{tamano}: ")
matriz1 = ingresar_matriz(tamano)

# Mostrar matriz original
print(f"\nMatriz {tamano}x{tamano} original:")
imprimir_matriz(matriz1)

# Transponer la matriz
matriz1_transpuesta = transponer_matriz(matriz1)

# Mostrar matriz transpuesta
print(f"\nMatriz {tamano}x{tamano} transpuesta:")
imprimir_matriz(matriz1_transpuesta)


