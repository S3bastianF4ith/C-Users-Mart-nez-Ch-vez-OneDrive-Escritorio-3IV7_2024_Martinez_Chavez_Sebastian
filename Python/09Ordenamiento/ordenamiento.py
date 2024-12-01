import time


# Función de ordenamiento burbuja
def burbuja(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n-i-1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista

# Función de ordenamiento por selección
def seleccion_sort(lista):
    n = len(lista)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if lista[j] < lista[min_idx]:
                min_idx = j
        lista[i], lista[min_idx] = lista[min_idx], lista[i]
    return lista

# Función de ordenamiento por inserción
def insercion(lista):
    for i in range(1, len(lista)):
        key = lista[i]
        j = i - 1
        while j >= 0 and key < lista[j]:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = key
    return lista

# Función de ordenamiento por mezcla (merge sort)
def merge(lista):
    if len(lista) > 1:
        mid = len(lista) // 2
        izquierda = lista[:mid]
        derecha = lista[mid:]

        # Llamadas recursivas
        merge(izquierda)
        merge(derecha)

        i = j = k = 0

        # Mezcla de las dos mitades
        while i < len(izquierda) and j < len(derecha):
            if izquierda[i] < derecha[j]:
                lista[k] = izquierda[i]
                i += 1
            else:
                lista[k] = derecha[j]
                j += 1
            k += 1
        
        # Copia los elementos restantes de izquierda
        while i < len(izquierda):
            lista[k] = izquierda[i]
            i += 1
            k += 1

        # Copia los elementos restantes de derecha
        while j < len(derecha):
            lista[k] = derecha[j]
            j += 1
            k += 1
    return lista

# Función de ordenamiento rápido (quick sort)
def quick_sort(lista):
    if len(lista) <= 1:
        return lista
    pivote = lista[len(lista) // 2]
    izquierda = [x for x in lista if x < pivote]
    medio = [x for x in lista if x == pivote]
    derecha = [x for x in lista if x > pivote]
    return quick_sort(izquierda) + medio + quick_sort(derecha)

# Función principal para la interfaz de usuario
def main():
    print("Bienvenido al programa de ordenamiento de listas.")
    
    # Solicitar al usuario que ingrese una lista de números
    while True:
        try:
            entrada = input("Ingrese hasta 40 números separados por espacios: ")
            lista_numeros = list(map(int, entrada.split()))
            if len(lista_numeros) > 40:
                print("Por favor, ingrese un máximo de 40 números.")
                continue
            break
        except ValueError:
            print("Entrada no válida. Asegúrese de ingresar solo números enteros.")

    # Mostrar opciones de ordenamiento
    print("Seleccione un método de ordenamiento:")
    print("1. Burbuja")
    print("2. Selección")
    print("3. Inserción")
    print("4. Merge")
    print("5. Quick Sort")

    while True:
        try:
            opcion = int(input("Ingrese el número de la opción deseada (1-5): "))
            if opcion in [1, 2, 3, 4, 5]:
                break
            else:
                print("Opción no válida. Por favor, elija un número entre 1 y 5.")
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número.")

    # Clonar la lista original para mostrarla después
    lista_original = lista_numeros.copy()

    # Medir el tiempo de ordenamiento
    inicio = time.time()
    
    if opcion == 1:
        lista_numeros = burbuja(lista_numeros)
    elif opcion == 2:
        lista_numeros = seleccion_sort(lista_numeros)
    elif opcion == 3:
        lista_numeros = insercion(lista_numeros)
    elif opcion == 4:
        lista_numeros = merge(lista_numeros)
    elif opcion == 5:
        lista_numeros = quick_sort(lista_numeros)

    fin = time.time()
    tiempo = fin - inicio

    # Mostrar resultados
    print("Lista original:", lista_original)
    print("Lista ordenada:", lista_numeros)
    print("Tiempo de ordenamiento: {:.6f} segundos".format(tiempo))

if __name__ == "__main__":
    main()