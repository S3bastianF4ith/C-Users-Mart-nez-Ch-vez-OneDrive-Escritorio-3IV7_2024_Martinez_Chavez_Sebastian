Algoritmo NegativosPositivos
	Definir numero Como Real
    Definir positivos, negativos Como Entero
    positivos <- 0
    negativos <- 0
	Escribir 'Escriba cantidad de numeros'
	leer i
	Repetir
		Escribir  'Escriba el numero'
		Leer numero
		Si numero > 0 Entonces
			positivos <- positivos + 1
		Sino
			negativos <- negativos + 1
		FinSi
		i=i-1
	Hasta Que i=0
	
    Escribir "Números positivos: ", positivos
    Escribir "Números negativos: ", negativos
FinAlgoritmo
