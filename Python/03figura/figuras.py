import math

#crear funcion para calculo del perimetro

def rectangulo(base, altura):
    area= base * altura
    perimetro= 2*(base+altura)
    return area, perimetro

def triangulo(base, altura, lado1, lado2, lado3):
    area= (base * altura)/2
    perimetro= lado1 + lado2 + lado3
    return area, perimetro

def sphera(radio):
   volumen = (4/3)*math.pi*radio**3
   return volumen

def menu():
    print('Hola bienvenido a python con funciones')
    print('Elije una opcion:')
    print('A.- Area y perimetro del rectangulo')
    print('B.- Area y perimetro del triangulo')
    print('C.- Volumen de la esfera')

#program
menu()
opcion= input('Introduce la opcion que deseas realizar:').upper()

if opcion== 'A':
    base = float(input('Introduce la base'))
    altura = float(input('Introduce la altura'))
    area, perimetro = rectangulo(base, altura)
    print('El area es de:', area)
    print('El perimetro es de:', perimetro)
if opcion== 'B':
    base = float(input('Introduce la base'))
    altura = float(input('Introduce la altura'))
    lado1 = float(input('Introduce lado 1'))
    lado2 = float(input('Introduce lado 2'))
    lado3 = float(input('Introduce lado 3'))
    area, perimetro  = triangulo(base, altura, lado1, lado2, lado3 )
    print('El area es de:', area)
    print('El perimetro es de:', perimetro)
elif opcion== 'C':
    radio = float(input('Introduce el radio'))
    volumen = esfera(radio)
    print('El volumen es: ', volumen)
