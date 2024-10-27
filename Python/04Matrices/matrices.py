# Vamos a crear una suma de matrices de 3 x 3

def ingresar_matriz():
    matriz = []

    print("Introduce los valores de la matriz de 3 x 3")
    for i in range(3):
        fila = []  # Inicializar la fila aquí
        for j in range(3):
            valor = float(input(f"Elemento: [{i + 1}] [{j + 1}]: "))  # Usar f-string para formatear
            fila.append(valor)
        matriz.append(fila)  # Agregar la fila completa a la matriz
    return matriz  # Devolver la matriz completa


def sumar_matriz(matriz1, matriz2):
    matrizsuma = []

    for i in range(3):
        fila = []
        for j in range(3):
            fila.append(matriz1[i][j] + matriz2[i][j])
        matrizsuma.append(fila)
    return matrizsuma  # Devolver la matriz suma


def imprimir_matriz(matriz):
    for fila in matriz:
        print(fila)  # Imprimir cada fila de la matriz


# Programa principal
print("Matriz 1: ")
matriz1 = ingresar_matriz()

print("Matriz 2: ")
matriz2 = ingresar_matriz()

# Sumar las matrices
matriz_resultado = sumar_matriz(matriz1, matriz2)

# Mostrar el resultado
print("El resultado es: ")
imprimir_matriz(matriz_resultado)
