import tkinter as tk
from tkinter import messagebox
import time

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def merge(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        izquierda = arr[:mid]
        derecha = arr[mid:]

        merge(izquierda)
        merge(derecha)

        i = j = k = 0

        while i < len(izquierda) and j < len(derecha):
            if izquierda[i] < derecha[j]:
                arr[k] = izquierda[i]
                i += 1
            else:
                arr[k] = derecha[j]
                j += 1
            k += 1
        
        while i < len(izquierda):
            arr[k] = izquierda[i]
            i += 1
            k += 1

        while j < len(derecha):
            arr[k] = derecha[j]
            j += 1
            k += 1
    return arr

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivote = arr[len(arr) // 2]
    izquierda = [x for x in arr if x < pivote]
    medio = [x for x in arr if x == pivote]
    derecha = [x for x in arr if x > pivote]
    return quick_sort(izquierda) + medio + quick_sort(derecha)

def sort_numbers():
    try:
        input_numbers = entry.get()
        numbers = list(map(int, input_numbers.split(',')))

        if len(numbers) > 40:
            messagebox.showerror("Error", "Por favor, ingrese un máximo de 40 números.")
            return

        method = sorting_method.get()

        start_time = time.time()
        if method == "Burbuja":
            sorted_numbers = bubble_sort(numbers.copy())
        elif method == "Selección":
            sorted_numbers = selection_sort(numbers.copy())
        elif method == "Inserción":
            sorted_numbers = insertion_sort(numbers.copy())
        elif method == "Merge":
            sorted_numbers = merge(numbers.copy())
        elif method == "Quick":
            sorted_numbers = quick_sort(numbers.copy())
        else:
            messagebox.showerror("Error", "Método de ordenamiento no válido.")
            return
        end_time = time.time()

        result_text = f"Lista original: {numbers}\nLista ordenada: {sorted_numbers}\nTiempo de ordenamiento: {end_time - start_time:.6f} segundos"
        messagebox.showinfo("Resultados", result_text)

    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese solo números separados por comas.")

root = tk.Tk()
root.title("Ordenador de Números")

label = tk.Label(root, text="Ingrese hasta 40 números separados por comas:")
label.pack()

entry = tk.Entry(root, width=50)
entry.pack()

sorting_method = tk.StringVar(value="Burbuja")
method_frame = tk.Frame(root)
method_frame.pack()

bubble_radio = tk.Radiobutton(method_frame, text="Burbuja", variable=sorting_method, value="Burbuja")
bubble_radio.pack(side=tk.LEFT)

selection_radio = tk.Radiobutton(method_frame, text="Selección", variable=sorting_method, value="Selección")
selection_radio.pack(side=tk.LEFT)

insertion_radio = tk.Radiobutton(method_frame, text="Inserción", variable=sorting_method, value="Inserción")
insertion_radio.pack(side=tk.LEFT)

merge_radio = tk.Radiobutton(method_frame, text="Merge", variable=sorting_method, value="Merge")
merge_radio.pack(side=tk.LEFT)

quick_radio = tk.Radiobutton(method_frame, text="Quick", variable=sorting_method, value="Quick")
quick_radio.pack(side=tk.LEFT)

sort_button = tk.Button(root, text="Ordenar", command=sort_numbers)
sort_button.pack()

root.mainloop()