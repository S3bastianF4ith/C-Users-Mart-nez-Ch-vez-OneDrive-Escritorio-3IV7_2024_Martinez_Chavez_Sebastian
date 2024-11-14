import tkinter as tk
from tkinter import messagebox, simpledialog
import os

ARCHIVO = "Ow.txt"  # Asegúrate de que el archivo esté en la misma carpeta o proporciona la ruta completa

personajes = [
    {"nombre": "Ana", "nombre completo": "Ana-Amari", "edad": "62", "nacionalidad": "Egipcia", "rol": "Apoyo", "bando": "Cuenta-Propia", "arma principal": "Rifle-Biotico", "arma secundaria": "NA", "pasiva": "Nanopotenciamiento", "ultimate": "Dardo-Sedante", "habilidades": ["Granada-Biotica", "NA", "NA"]},
    {"nombre": "Ashe", "nombre completo": "Elizabeth-Caledonia", "edad": "41", "nacionalidad": "Americana", "rol": "Daño", "bando": "Banda-Deadlock-Rebels", "arma principal": "Vibora", "arma secundaria": "NA", "pasiva": "B.O.B", "ultimate": "Escopeta-Recortada", "habilidades": ["Diamita", "NA", "NA"]},
    {"nombre": "Baptiste", "nombre completo": "Jean-Baptiste-Augustin", "edad": "38", "nacionalidad": "Haiti", "rol": "Apoyo", "bando": "Overwatch", "arma principal": "Lanzagrandas-Biotico", "arma secundaria": "NA", "pasiva": "Exobotas", "ultimate": "Ventana-de-Amplificación", "habilidades": ["Energia-Biotica", "Campo-de-Inmortalidad", "NA"]},
    {"nombre": "Bastion", "nombre completo": "Bastion-E54", "edad": "32", "nacionalidad": "Sueco", "rol": "Daño", "bando": "Overwatch", "arma principal": "Modo-Asalto", "arma secundaria": "Modo-Reconocimiento", "pasiva": "NA", "ultimate": "Artilleria", "habilidades": ["Granada-Tactica-A-36", "Reconfiguración", "NA"]},
    {"nombre": "Brigitte", "nombre completo": "Brigitte-Lindholm", "edad": "25", "nacionalidad": "Sueca", "rol": "Apoyo", "bando": "Overwatch", "arma principal": "Mangual-Mecanico", "arma secundaria": "Escudo-Barrera", "pasiva": "Inspiración", "ultimate": "Rally", "habilidades": ["Kit-de-Reparación", "Lanzamiento-de-Mangual", "Carga-con-Escudo"]},
    {"nombre": "Cassidy", "nombre completo": "Cole-Cassidy", "edad": "39", "nacionalidad": "Americano", "rol": "Daño", "bando": "Overwatch", "arma principal": "Pacificador", "arma secundaria": "NA", "pasiva": "Tiro-Certero", "ultimate": "Evasión", "habilidades": ["Granada-Segadora", "NA", "NA"]},
    {"nombre": "D.Va", "nombre completo": "Hana-Song", "edad": "21", "nacionalidad": "Coreana", "rol": "Tanque", "bando": "Overwatch", "arma principal": "Cañones-de-Fusión", "arma secundaria": "Pistola-de-Luz", "pasiva": "Eyección", "ultimate": "Autodestrucción", "habilidades": ["Propulsores", "Matriz-de-Defensa", "Micromisiles"]},
    {"nombre": "Doomfist", "nombre completo": "Akande-Ogondimu", "edad": "47", "nacionalidad": "Nigeriano", "rol": "Tanque", "bando": "Talon", "arma principal": "Cañon-de-Mano", "arma secundaria": "NA", "pasiva": "Portador-del-Guante", "ultimate": "Golpe-de-Meteoro", "habilidades": ["Golpe-Sismico", "Puño-Cohete", "Bloqueo-de-Poder"]},
    {"nombre": "Echo", "nombre completo": "Echo", "edad": "14", "nacionalidad": "Suiza", "rol": "Daño", "bando": "Overwatch", "arma principal": "Disparo-Triple", "arma secundaria": "NA", "pasiva": "Planeo", "ultimate": "Duplicación", "habilidades": ["Bombas-Lapa", "Haz-Enfocado", "Vuelo"]},
    {"nombre": "Genji", "nombre completo": "Genji-Shimada", "edad": "37", "nacionalidad": "Japones", "rol": "Daño", "bando": "Overwatch", "arma principal": "Shuriken", "arma secundaria": "NA", "pasiva": "Ciberagilidad", "ultimate": "Hoja-del-Dragon", "habilidades": ["Desvio", "Corte-Veloz", "NA"]},
    {"nombre": "Hanzo", "nombre completo": "Hanzo-Shimada", "edad": "40", "nacionalidad": "Japones", "rol": "Daño", "bando": "Cuenta-Propia", "arma principal": "Arco-de-la-Tormenta", "arma secundaria": "NA", "pasiva": "Escalada", "ultimate": "Ataque-del-Dragon", "habilidades": ["Tormenta-de-Flechas", "Flecha-Sonica", "Agilidad-del-Dragon"]},
    {"nombre": "Illari", "nombre completo": "Illari-Quispe-Ruiz", "edad": "18", "nacionalidad": "Peruana", "rol": "Apoyo", "bando": "Cuenta-Propia", "arma principal": "Rifle-Solar", "arma secundaria": "NA", "pasiva": "NA", "ultimate": "Sol-Cautivo", "habilidades": ["Erupción", "Helioterapia", "NA"]},
    {"nombre": "Junker-Queen", "nombre completo": "Odessa-Stone", "edad": "31", "nacionalidad": "Australiana", "rol": "Tanque", "bando": "Junkers", "arma principal": "Escopeta", "arma secundaria": "Cuchillo-Dentado", "pasiva": "Subidon-de-Adrenalina", "ultimate": "Desenfreno", "habilidades": ["Grito-de-Guerra", "Matanza", "NA"]},
    {"nombre": "Junkrat", "nombre completo": "Jamison-Fawkes", "edad": "27", "nacionalidad": "Australiano", "rol": "Daño", "bando": "Junkers", "arma principal": "Lanzagranadas", "arma secundaria": "NA", "pasiva": "Caos-Total", "ultimate": "Neumatico-Devastador", "habilidades": ["Mina-de-Conmoción", "Trampa-de-Osos", "NA"]},
    {"nombre": "Juno", "nombre completo": "Juno-Tao-Minh", "edad": "19", "nacionalidad": "Vietnamita", "rol": "Apoyo", "bando": "Overwatch", "arma principal": "Mediarma", "arma secundaria": "NA", "pasiva": "Cubrebotas-Marciano", "ultimate": "Rayo-Orbital", "habilidades": ["Impulso-de-Planeo", "Hiperanillo", "Torpedos-de-Pulsar"]},
    {"nombre": "Kiriko", "nombre completo": "Kiriko-Kamori", "edad": "21", "nacionalidad": "Japonesa", "rol": "Apoyo", "bando": "Yōkai-de-Hanamura", "arma principal": "Kunái", "arma secundaria": "Ofunda-de-Sanación", "pasiva": "Escalada", "ultimate": "Marcha-del-Kitsune", "habilidades": ["Paso-Ligero", "Suzu-de-Protección", "NA"]},
    {"nombre": "Lifeweaver", "nombre completo": "Niran-PruksaManee", "edad": "31", "nacionalidad": "Tailandes", "rol": "Apoyo", "bando": "Cuenta-Propia", "arma principal": "Salva-Espinosa", "arma secundaria": "Brote-Sanador", "pasiva": "NA", "ultimate": "Arbol-de-la-Vida", "habilidades": ["Paso-Regenerador", "Agarre-Vital", "Plataforma-Petraloide"]},
    {"nombre": "Lucio", "nombre completo": "Lucio-Dos-Santos", "edad": "28", "nacionalidad": "Brazileño", "rol": "Apoyo", "bando": "Overwatch", "arma principal": "Amplificador-de-Sonido", "arma secundaria": "NA", "pasiva": "Trotamuros", "ultimate": "Barrera-de-Sonido", "habilidades": ["Cambio-de-Pista", "Subidon", "Onda-Sonora"]},
    {"nombre": "Mauga", "nombre completo": "Mauga-Malosi", "edad": "37", "nacionalidad": "Samoano", "rol": "Tanque", "bando": "Talon", "arma principal": "Guni", "arma secundaria": "Cha-Cha", "pasiva": "Berserker", "ultimate": "Lucha-en-la-Jaula", "habilidades": ["Arrollar", "Sobreestimulación-Cardiaca", "NA"]},
    {"nombre": "Mei", "nombre completo": "Mei-Ling-Zhou", "edad": "33", "nacionalidad": "China", "rol": "Daño", "bando": "Overwatch", "arma principal": "Pistola-Endotermica", "arma secundaria": "NA", "pasiva": "NA", "ultimate": "Ventisca", "habilidades": ["Muro-de-Hielo", "Crionica", "NA"]},
     {"nombre": "Mercy", "nombre completo": "Angela-Ziegler", "edad": "39", "nacionalidad": "Suiza", "rol": "Apoyo", "bando": "Overwatch", "arma principal": "Baston-Caduceo", "arma secundaria": "Pistola-Caducea", "pasiva": "Descenso-Angelical", "ultimate": "Valkiria", "habilidades": ["Angel-de-la-Guardia", "Resurrección", "NA"]},
    {"nombre": "Moira", "nombre completo": "Moira-O'Deorain", "edad": "50", "nacionalidad": "Iraquie", "rol": "Apoyo", "bando": "Talon", "arma principal": "Rayo-Biotico", "arma secundaria": "NA", "pasiva": "NA", "ultimate": "Coalesencia", "habilidades": ["Evanescencia", "Orbe-Biotico", "NA"]},
    {"nombre": "Orisa", "nombre completo": "OR-15", "edad": "1", "nacionalidad": "Nunbaniana", "rol": "Tanque", "bando": "Cuenta-Propia", "arma principal": "Ametralladora-de-Fusión-Aumentada", "arma secundaria": "NA", "pasiva": "NA", "ultimate": "Impacto-Terrestre", "habilidades": ["Jabalina-de-Energia", "Girojabalina", "Fortificación"]},
    {"nombre": "Pharah", "nombre completo": "Fareeha-Amari", "edad": "34", "nacionalidad": "Egipcia", "rol": "Daño", "bando": "Overwatch", "arma principal": "Lanzacohetes", "arma secundaria": "NA", "pasiva": "Planeador", "ultimate": "Bombardeo", "habilidades": ["Impulso-Propulsores", "Disparo-de-Conmocion", "NA"]},
    {"nombre": "Ramattra", "nombre completo": "Ravager-Omnico-(Ramattra)", "edad": "28", "nacionalidad": "Nepales", "rol": "Tanque", "bando": "Null-Sector", "arma principal": "Acelerador-del-Vacio-(Forma-Nemesis)", "arma secundaria": "NA", "pasiva": "NA", "ultimate": "Aniquilación", "habilidades": ["Barrera-de-Vacio", "Vortice-Voraz", "Forma-Nemesis"]},
    {"nombre": "Reaper", "nombre completo": "Gabriel-Reyes", "edad": "60", "nacionalidad": "Americano", "rol": "Daño", "bando": "Talon", "arma principal": "Escopetas-Infernales", "arma secundaria": "NA", "pasiva": "Siega", "ultimate": "Aniquilación-de-Almas", "habilidades": ["Paso-de-las-Tinieblas", "Forma-Espectral", "NA"]},
    {"nombre": "Reinhardt", "nombre completo": "Reinhardt-Wilhelm", "edad": "63", "nacionalidad": "Aleman", "rol": "Tanque", "bando": "Overwatch", "arma principal": "Martillo-a-Reaccion", "arma secundaria": "NA", "pasiva": "NA", "ultimate": "Terratemblor", "habilidades": ["Embestida", "Onda-de-Fuego", "Campo-Protector"]},
    {"nombre": "Roadhog", "nombre completo": "Mako-Rutledge", "edad": "50", "nacionalidad": "Australiano", "rol": "Tanque", "bando": "Junkers", "arma principal": "Chatarrera", "arma secundaria": "NA", "pasiva": "NA", "ultimate": "Whole-Hog", "habilidades": ["Inhalador", "Garfio", "Corral-de-Cerdos"]},
    {"nombre": "Sigma", "nombre completo": "Siebren-de-Kuiper", "edad": "64", "nacionalidad": "Holandes", "rol": "Tanque", "bando": "Talon", "arma principal": "Hiperesferas", "arma secundaria": "NA", "pasiva": "NA", "ultimate": "Flujo-Gravitatorio", "habilidades": ["Agarre-Cinetico", "Acreción", "Barrera-Experimental"]},
    {"nombre": "Soujourn", "nombre completo": "Vivian-Chase", "edad": "51", "nacionalidad": "Canadiense", "rol": "Daño", "bando": "Overwatch", "arma principal": "Cañon-de-Riel", "arma secundaria": "NA", "pasiva": "NA", "ultimate": "Overclock", "habilidades": ["Maniobra-Evasiva", "Disparo-Inmovilizador", "NA"]},
    {"nombre": "Soldado-76", "nombre completo": "Jack-Morrison", "edad": "58", "nacionalidad": "Americano", "rol": "Daño", "bando": "Cuenta-Propia", "arma principal": "Rifle-de-Puslsos-Pesado", "arma secundaria": "NA", "pasiva": "NA", "ultimate": "Visor-Tactico", "habilidades": ["Campo-Biotico", "Sprint", "Cohetes-Helice"]},
    {"nombre": "Sombra", "nombre completo": "Olivia-Colomar", "edad": "32", "nacionalidad": "Mexicana", "rol": "Daño", "bando": "Talon", "arma principal": "Subfusil", "arma secundaria": "NA", "pasiva": "Oportunista", "ultimate": "PEM", "habilidades": ["Virus", "Baliza-de-Ecolocalización", "Hackeo"]},
    {"nombre": "Symmetra", "nombre completo": "Satya-Vaswani", "edad": "30", "nacionalidad": "India", "rol": "Daño", "bando": "Corporación-Vishkar", "arma principal": "Proyector-de-Fotones", "arma secundaria": "NA", "pasiva": "NA", "ultimate": "Barrera-de-Fotones", "habilidades": ["Torreta-Centinela", "Teletransportador", "NA"]},
    {"nombre": "Torbjörn", "nombre completo": "Trobjörn-Lindholm", "edad": "59", "nacionalidad": "Sueco", "rol": "Daño", "bando": "Overwatch", "arma principal": "Remachacadora", "arma secundaria": "Martillo-de-Forja", "pasiva": "NA", "ultimate": "Nucleo-de-Magma", "habilidades": ["Torreta-Desplegable", "Sobrecarga", "NA"]},
    {"nombre": "Tracer", "nombre completo": "Lena-Oxton", "edad": "28", "nacionalidad": "Inglesa", "rol": "Daño", "bando": "Overwatch", "arma principal": "Pistolas-de-Pulso", "arma secundaria": "NA", "pasiva": "NA", "ultimate": "Bomba-de-Pulso", "habilidades": ["Traslación", "Regresión", "NA"]},
    {"nombre": "Venture", "nombre completo": "Cameron-Sloan", "edad": "26", "nacionalidad": "Mexicana", "rol": "Daño", "bando": "Cuenta-Propia", "arma principal": "Excavadora-Inteligente", "arma secundaria": "NA", "pasiva": "Golpe-Perforante", "ultimate": "Impacto-Tectonico", "habilidades": ["Perforación", "Enterrarse", "NA"]},
    {"nombre": "Winston", "nombre completo": "Winton-Overwat", "edad": "31", "nacionalidad": "Lunario", "rol": "Tanque", "bando": "Overwatch", "arma principal": "Cañon-de-Tesla", "arma secundaria": "NA", "pasiva": "NA", "ultimate": "Rabia-Primal", "habilidades": ["Escudo-Burbuja", "Salto-Potenciado", "NA"]},
    {"nombre": "Widowmaker", "nombre completo": "Amélie-Lacroix", "edad": "35", "nacionalidad": "Francesa", "rol": "Daño", "bando": "Talon", "arma principal": "Beso-de-la-Viuda", "arma secundaria": "NA", "pasiva": "NA", "ultimate": "Infravisión", "habilidades": ["Gancho", "Mina-Venenosa", "NA"]},
    {"nombre": "Wrecking-Ball", "nombre completo": "Hammond", "edad": "16", "nacionalidad": "Lunario", "rol": "Tanque", "bando": "Junkers", "arma principal": "Cañones-Cuadruples", "arma secundaria": "Bola-Arrolladora", "pasiva": "NA", "ultimate": "Campo-Minado", "habilidades": ["Gancho-Garra", "Impacto-Demoledor", "Escudo-Adaptable"]},
    {"nombre": "Zarya", "nombre completo": "Aleksandra-Zaryanova", "edad": "30", "nacionalidad": "Rusa", "rol": "Tanque", "bando": "Overwatch", "arma principal": "Cañon-de-Particulas", "arma secundaria": "NA", "pasiva": "Recolección-de-Energia", "ultimate": "Bomba-de-Gravedad", "habilidades": ["Barrera-de-Particulas", "Barrera-Proyectada", "NA"]},
    {"nombre": "Zenyatta", "nombre completo": "Tekhartha-Zenyatta", "edad": "33", "nacionalidad": "Nepales", "rol": "Apoyo", "bando": "Cuenta-Propia", "arma principal": "Orbes-de-Destrucción", "arma secundaria": "NA", "pasiva": "Patada-Veloz", "ultimate": "Trascendencia", "habilidades": ["Orbe-de-Discordia", "Orbe-de-Armonia", "NA"]}
]

def cargar_datos():
    if os.path.exists(ARCHIVO):  # Verifica si el archivo existe
        with open(ARCHIVO, "r") as f:
            for linea in f:
                partes = linea.strip().split(",")  # Separa los datos por comas
                if len(partes) >= 13:  # Asegúrate de que haya suficientes datos para un personaje
                    nombre = partes[0]
                    nombrecompleto = partes[1]
                    edad = partes[2]
                    nacionalidad = partes[3]
                    rol = partes[4]
                    bando = partes[5]
                    armaprincipal = partes[6]
                    armasecundaria = partes[7]
                    pasiva = partes[8]
                    ultimate = partes[9]
                    habilidades = [float(habilidad) for habilidad in partes[10:]]  # Convierte las habilidades a flotantes
                    personaje = {
                        "nombre": nombre,
                        "nombre completo": nombrecompleto,
                        "edad": edad,
                        "nacionalidad": nacionalidad,
                        "rol": rol,
                        "bando": bando,
                        "arma principal": armaprincipal,
                        "arma secundaria": armasecundaria,
                        "pasiva": pasiva,
                        "ultimate": ultimate,
                        "habilidades": habilidades
                    }
                    personajes.append(personaje)  # Añade el personaje a la lista
    else:
        print("El archivo no existe")

def guardar_datos():
    with open(ARCHIVO, "w") as f:
        for personaje in personajes:
            f.write(f"{personaje['nombre']},{personaje['nombre completo']},{personaje['edad']},{personaje['nacionalidad']},{personaje['rol']},{personaje['bando']},{personaje['arma principal']},{personaje['arma secundaria']},{personaje['pasiva']},{personaje['ultimate']},{','.join(map(str, personaje['habilidades']))}\n")

def registrar_personaje():
    nombre = simpledialog.askstring("nombre", "Ingresa el nombre del personaje:")
    nombrecompleto = simpledialog.askstring("nombre completo", "Ingresa el nombre completo del personaje:")
    edad = simpledialog.askstring("edad", "Ingresa la edad del personaje:")
    nacionalidad = simpledialog.askstring("nacionalidad", "Ingresa la nacionalidad del personaje:")
    rol = simpledialog.askstring("rol", "Ingresa el rol del personaje:")
    bando = simpledialog.askstring("bando", "Ingresa el bando del personaje:")
    armaprincipal = simpledialog.askstring("arma principal", "Ingresa el arma principal del personaje:")
    armasecundaria = simpledialog.askstring("arma secundaria", "Ingresa el arma secundaria del personaje:")
    pasiva = simpledialog.askstring("pasiva", "Ingresa la pasiva del personaje:")
    ultimate = simpledialog.askstring("ultimate", "Ingresa la ultimate del personaje:")

    habilidades = []
    for i in range(3):
        habilidad = simpledialog.askstring(f"Habilidad {i+1}", f"Ingrese la habilidad {i+1}:")
        habilidades.append(habilidad)

    personaje = {
        "nombre": nombre,
        "nombre completo": nombrecompleto,
        "edad": edad,
        "nacionalidad": nacionalidad,
        "rol": rol,
        "bando": bando,
        "arma principal": armaprincipal,
        "arma secundaria": armasecundaria,
        "pasiva": pasiva,
        "ultimate": ultimate,
        "habilidades": habilidades
    }
    personajes.append(personaje)
    guardar_datos()
    messagebox.showinfo("Éxito", "Personaje registrado exitosamente")

def consultar_personajes():
    if not personajes:
        messagebox.showinfo("Lista Vacía", "No hay personajes registrados.")
    else:
        # Crear una lista con los nombres de los personajes
        info = "Lista de Personajes:\n\n"
        for i, personaje in enumerate(personajes, 1):
            info += f"{i}. {personaje['nombre']} {personaje['nombre completo']} {personaje['edad']}{personaje['nacionalidad']} {personaje['rol']}) {personaje['bando']} {personaje['arma principal']} {personaje['arma secundaria']} {personaje['pasiva']} {personaje['ultimate']} {personaje['habilidades']}\n"
        
        # Mostrar la lista
        messagebox.showinfo("Lista de Personajes", info)

def editar_personaje():
    nombre = simpledialog.askstring("nombre", "Ingrese el nombre del personaje que desea editar:")
    for personaje in personajes:
        if personaje['nombre'] == nombre:
            personaje['nombre'] = simpledialog.askstring("nombre", f"Nuevo nombre ({personaje['nombre']}):") or personaje['nombre']
            personaje['nombrecompleto'] = simpledialog.askstring("nombre completo", f"Nuevo nombre completo ({personaje['nombrecompleto']}):") or personaje['nombrecompleto']
            personaje['edad'] = simpledialog.askstring("edad", f"Nueva edad ({personaje['edad']}):") or personaje['edad']
            personaje['nacionalidad'] = simpledialog.askstring("nacionalidad", f"Nuevo nacionalidad ({personaje['nacionalidad']}):") or personaje['nacionalidad']
            personaje['rol'] = simpledialog.askstring("rol", f"Nuevo rol ({personaje['rol']}):") or personaje['rol']
            personaje['bando'] = simpledialog.askstring("bando", f"Nuevo bando ({personaje['bando']}):") or personaje['bando']
            personaje['armaprincipal'] = simpledialog.askstring("Nueva arma principal", f"Nuevo arma principal ({personaje['armaprincipal']}):") or personaje['armaprincipal']
            personaje['armasecundaria'] = simpledialog.askstring("arma secundaria", f"Nuevo arma secundaria ({personaje['armasecundaria']}):") or personaje['armasecundaria']
            personaje['pasiva'] = simpledialog.askstring("pasiva", f"Nueva pasiva ({personaje['pasiva']}):") or personaje['pasiva']
            personaje['ultimate'] = simpledialog.askstring("ultimate", f"Nueva ultimate ({personaje['ultimate']}):") or personaje['ultimate']
            for i in range(3):
                nueva_habilidad = simpledialog.askfloat(f"Habilidad {i+1}", f"Nueva habilidad {i+1} ({personaje['habilidades'][i]}):")
                if nueva_habilidad is not None:
                    personaje['habilidades'][i] = nueva_habilidad

            guardar_datos()
            messagebox.showinfo("Éxito", "Personaje editado exitosamente")
            return
    messagebox.showwarning("No Encontrado", "No se encontró un personaje con ese nombre.")

def eliminar_personaje():
    nombre = simpledialog.askstring("nombre", "Ingrese el nombre del personaje que desea eliminar:")
    for personaje in personajes:
        if personaje['nombre'] == nombre:
            personajes.remove(personaje)
            guardar_datos()
            messagebox.showinfo("Éxito", "Personaje eliminado exitosamente")
            return
    messagebox.showwarning("No Encontrado", "No se encontró un personaje con ese nombre.")

def main():
    cargar_datos  # Cargar los datos al inicio

    while True:
        opcion = simpledialog.askstring("Menú de Gestión", 
            "1. Registrar personaje\n2. Consultar Lista de personajes\n3. Editar personaje\n4. Eliminar personaje\n5. Salir\nSeleccione una opción:")

        if opcion == "1":
            registrar_personaje()
        elif opcion == "2":
            consultar_personajes()
        elif opcion == "3":
            editar_personaje()
        elif opcion == "4":
            eliminar_personaje()
        elif opcion == "5":
            messagebox.showinfo("Adiós", "¡Hasta luego!")
            break
        else:
            messagebox.showwarning("Opción no válida", "Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main()

