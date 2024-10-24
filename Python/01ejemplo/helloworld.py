print("Hola mundo")
#esto es un comentario

#vamos a definir una variable

x=17.89

print(x)

#ejemplo de if

y = 28
if y < 0:
    print('Es menor que 0')
elif y > 0:
    print('es mayor que 0')
else :
    print('es cero')

valores = [6, 8, 9, 10]
if 5 in valores:
    #cuando sea verdad
    print('esta')
else :
    print('no esta')

#bucles
numero=0
print('tabla del 2')

while numero <= 10:
    print('Resultado :' , 2*numero)
    numero+=1

#bucle for
numeros = [3, 7, 5, 8]

for n in numeros :
    print(n)
    