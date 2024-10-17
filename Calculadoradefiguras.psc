//programa para dar area y perimetro con funciones
//vamos a crear el subproceso del retangulo
SubProceso rectangulo(base,altura)
	Definir area,perimetro Como Real
	area=base*altura
	perimetro=2*(base+altura)
	Escribir "El area del rectangulo es: ", area
	Escribir "El perimetro del rectangulo es: ", perimetro
FinSubProceso

SubProceso triangulo(base,altura, lado1, lado2, lado3)
	Definir area,perimetro Como Real
	area=(base*altura)/2
	perimetro=lado1+lado2+lado3
	Escribir "El area del triangulo es: ", area
	Escribir "El perimetro del triangulo es: ", perimetro
FinSubProceso

SubProceso Rombo(diagonalmayor, diagonalmenor, lado)
	Definir area,perimetro Como Real
	area=(diagonalmayor*diagonalmenor)/2
	perimetro= lado*4
	Escribir "El area del Rombo es: ", area
	Escribir "El perimetro del Rombo es: ", perimetro
FinSubProceso

SubProceso Pentagono(apotema, pentalado)
	Definir area,perimetro Como Real
	perimetro= pentalado*5
	area= (perimetro*apotema)/2
	Escribir "El area del Pentagono es: ", area
	Escribir "El perimetro del Pentagono es: ", perimetro
FinSubProceso

SubProceso Heptagono(apotema, heptalado)
	Definir area,perimetro Como Real
	perimetro= heptalado*7
	area= (perimetro*apotema)/2
	Escribir "El area del Pentagono es: ", area
	Escribir "El perimetro del Pentagono es: ", perimetro
FinSubProceso

SubProceso Octagono(apotema, octalado)
	Definir area,perimetro Como Real
	perimetro= octalado*8
	area= (perimetro*apotema)/2
	Escribir "El area del Pentagono es: ", area
	Escribir "El perimetro del Pentagono es: ", perimetro
FinSubProceso

SubProceso Eneagono(apotema, enealado)
	Definir area,perimetro Como Real
	perimetro= enealado*9
	area= (perimetro*apotema)/2
	Escribir "El area del Pentagono es: ", area
	Escribir "El perimetro del Pentagono es: ", perimetro
FinSubProceso

SubProceso Dodecagono(apotema, dodelado)
	Definir area,perimetro Como Real
	perimetro= dodelado*12
	area= (perimetro*apotema)/2
	Escribir "El area del Pentagono es: ", area
	Escribir "El perimetro del Pentagono es: ", perimetro
FinSubProceso

Algoritmo calculadoredefiguras
	Definir opcion Como Caracter
	Definir base,altura,lado1,lado2,lado3, apotema, pentalado, enealado Como Real
	Definir diagonalmayor, diagonalmenor, lado, heptalado, octalado, dodelado Como Real
	//vamos a crear el menu
	Escribir "Selecciona una opcion: "
	Escribir "A area y perimetro del Rectangulo"
	Escribir "B area y perimetro del Triangulo"
	Escribir "C area y perimetro del Rombo"
	Escribir "D area y perimetro del Pentagono"
	Escribir "E area y perimetro del Heptagono"
	Escribir "F area y perimetro del Octagono"
	Escribir "G area y perimetro del Eneagono"
	Escribir "H area y perimetro del Dodecagono"

	Leer opcion
	Segun opcion Hacer
		caso "A":
			Escribir "Ingrese la base del rectangulo"
			Leer base
			Escribir "Ingrese la altura del rectangulo"
			Leer altura
			rectangulo(base,altura)
		caso "B":
			Escribir "Ingrese la base del triangulo"
			Leer base
			Escribir "Ingrese la altura del triangulo"
			Leer altura
			Escribir "Ingresa lado1"
			Leer lado1
			Escribir "Ingresa lado2"
			Leer lado2
			Escribir "Ingresa lado3"
			Leer lado3
			triangulo(base,altura,lado1,lado2,lado3)
		Caso "C":
			Escribir "Ingrese la diagonal mayor del rombo"
			Leer diagonalmayor
			Escribir "Ingrese la diagonal menor del rombo"
			Leer diagonalmenor
			Escribir "Ingrese el lado del rombo"
			Leer lado
			Rombo(diagonalmayor, diagonalmenor, lado)
		Caso "D":
			Escribir "Ingrese la apotema del pentagono"
			Leer apotema
			Escribir "Ingrese el lado del pentagono"
			Leer pentalado
			Pentagono(apotema, pentalado)
		Caso "E":
			Escribir "Ingrese la apotema del heptagono"
			Leer apotema
			Escribir "Ingrese el lado del heptagono"
			Leer heptalado
			Heptagono(apotema, heptalado)
		Caso "F":
			Escribir "Ingrese la apotema del octagono"
			Leer apotema
			Escribir "Ingrese el lado del octagono"
			Leer octalado
			Octagono(apotema, octalado)
		Caso "G":
			Escribir "Ingrese la apotema del eneagono"
			Leer apotema
			Escribir "Ingrese el lado del eneagono"
			Leer enealado
			Eneagono(apotema, enealado)
		Caso "H":
			Escribir "Ingrese la apotema del dodecagono"
			Leer apotema
			Escribir "Ingrese el lado del dodecagono"
			Leer dodelado
			Dodecagono(apotema, dodelado)
		De Otro Modo:
			Escribir "Opcion no valida"
	Fin Segun
FinAlgoritmo
