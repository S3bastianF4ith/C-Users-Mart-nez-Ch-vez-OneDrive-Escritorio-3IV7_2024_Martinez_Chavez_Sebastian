import tkinter as tk
from tkinter import messagebox, simpledialog
import os

# Ruta del archivo de almacenamiento de alumnos
ARCHIVO = "Ow.txt"

# Lista global para almacenar a los alumnos
alumnos = []

# Función para cargar los datos desde el archivo
def cargar_datos():
    if os.path.exists(ARCHIVO):
        with open(ARCHIVO, "r") as f:
            for linea in f:
                # Separamos los datos por comas
                partes = linea.strip().split(",")
                if len(partes) >= 6:
                    boleta = partes[0]
                    nombre = partes[1]
                    apellido_paterno = partes[2]
                    apellido_materno = partes[3]
                    fecha_nacimiento = partes[4]
                    # Las calificaciones se guardan como una lista de floats
                    calificaciones = list(map(float, partes[5:]))
                    alumno = {
                        "boleta": boleta,
                        "nombre": nombre,
                        "apellido_paterno": apellido_paterno,
                        "apellido_materno": apellido_materno,
                        "fecha_nacimiento": fecha_nacimiento,
                        "calificaciones": calificaciones
                    }
                    alumnos.append(alumno)

# Función para guardar los datos en el archivo
def guardar_datos():
    with open(ARCHIVO, "w") as f:
        for alumno in alumnos:
            f.write(f"{alumno['boleta']},{alumno['nombre']},{alumno['apellido_paterno']},{alumno['apellido_materno']},{alumno['fecha_nacimiento']},{','.join(map(str, alumno['calificaciones']))}\n")

# Función para registrar un nuevo alumno
def registrar_alumno():
    boleta = simpledialog.askstring("Boleta", "Ingresa la boleta del alumno:")
    nombre = simpledialog.askstring("Nombre", "Ingresa el nombre del alumno:")
    apellido_paterno = simpledialog.askstring("Apellido Paterno", "Ingresa el apellido paterno del alumno:")
    apellido_materno = simpledialog.askstring("Apellido Materno", "Ingresa el apellido materno del alumno:")
    fecha_nacimiento = simpledialog.askstring("Fecha de Nacimiento", "Ingresa la fecha de nacimiento (DD/MM/YYYY):")

    calificaciones = []
    for i in range(3):
        calificacion = simpledialog.askfloat(f"Calificación {i+1}", f"Ingrese la calificación {i+1}:")
        calificaciones.append(calificacion)

    alumno = {
        'boleta': boleta,
        'nombre': nombre,
        'apellido_paterno': apellido_paterno,
        'apellido_materno': apellido_materno,
        'fecha_nacimiento': fecha_nacimiento,
        'calificaciones': calificaciones
    }
    
    alumnos.append(alumno)
    guardar_datos()
    messagebox.showinfo("Éxito", "Alumno registrado exitosamente")

# Función para consultar la lista de alumnos
def consultar_alumnos():
    if not alumnos:
        messagebox.showinfo("Lista Vacía", "No hay alumnos registrados.")
    else:
        info = "Lista de Alumnos:\n\n"
        for alumno in alumnos:
            info += (f"Boleta: {alumno['boleta']}, Nombre: {alumno['nombre']} {alumno['apellido_paterno']} {alumno['apellido_materno']}, "
                     f"Fecha de Nacimiento: {alumno['fecha_nacimiento']}, Calificaciones: {alumno['calificaciones']}\n")
        messagebox.showinfo("Lista de Alumnos", info)

# Función para editar los datos de un alumno por su boleta
def editar_alumno():
    boleta = simpledialog.askstring("Boleta", "Ingrese la boleta del alumno que desea editar:")
    for alumno in alumnos:
        if alumno['boleta'] == boleta:
            alumno['nombre'] = simpledialog.askstring("Nombre", f"Nuevo nombre ({alumno['nombre']}):") or alumno['nombre']
            alumno['apellido_paterno'] = simpledialog.askstring("Apellido Paterno", f"Nuevo apellido paterno ({alumno['apellido_paterno']}):") or alumno['apellido_paterno']
            alumno['apellido_materno'] = simpledialog.askstring("Apellido Materno", f"Nuevo apellido materno ({alumno['apellido_materno']}):") or alumno['apellido_materno']
            for i in range(3):
                nueva_calificacion = simpledialog.askfloat(f"Calificación {i+1}", f"Nueva calificación {i+1} ({alumno['calificaciones'][i]}):")
                if nueva_calificacion is not None:
                    alumno['calificaciones'][i] = nueva_calificacion
            
            guardar_datos()
            messagebox.showinfo("Éxito", "Alumno editado exitosamente")
            return
    messagebox.showwarning("No Encontrado", "No se encontró un alumno con esa boleta.")

# Función para eliminar un alumno por su boleta
def eliminar_alumno():
    boleta = simpledialog.askstring("Boleta", "Ingrese la boleta del alumno que desea eliminar:")
    for alumno in alumnos:
        if alumno['boleta'] == boleta:
            alumnos.remove(alumno)
            guardar_datos()
            messagebox.showinfo("Éxito", "Alumno eliminado exitosamente")
            return
    messagebox.showwarning("No Encontrado", "No se encontró un alumno con esa boleta.")

# Función para el menú principal
def main():
    cargar_datos()  # Cargamos los datos al inicio

    while True:
        # Menú de opciones
        opcion = simpledialog.askstring("Menú de Gestión", 
            "1. Registrar Alumno\n2. Consultar Lista de Alumnos\n3. Editar Alumno\n4. Eliminar Alumno\n5. Salir\nSeleccione una opción:")

        if opcion == "1":
            registrar_alumno()
        elif opcion == "2":
            consultar_alumnos()
        elif opcion == "3":
            editar_alumno()
        elif opcion == "4":
            eliminar_alumno()
        elif opcion == "5":
            messagebox.showinfo("Adiós", "¡Hasta luego!")
            break
        else:
            messagebox.showwarning("Opción no válida", "Por favor, seleccione una opción válida.")

# Ejecutar el programa
if __name__ == "__main__":
    main()

    print("Lista de Alumnos: \n")