Algoritmo La_Vida_De_Las_Personas
	Definir a�o, edad, persona Como Entero
	Dimension A�os[18]
	A�os[1] <- 1930 
	A�os[2] <- 1940
	A�os[3] <- 1960
	A�os[4] <- 1972
	A�os[5] <- 1980
	A�os[6] <- 1990
	A�os[7] <- 1999
	A�os[8] <- 2000
	A�os[9] <- 2000
	A�os[10] <- 2000
	A�os[11] <- 2001
	A�os[12] <- 2010
	A�os[13] <- 2010
	A�os[14] <- 2012
	A�os[15] <- 2037
	A�os[16] <- 2040
	A�os[17] <- 2042
	A�os[18] <- 2050
	
	Dimension persona[18]
	persona[1] <- 1
	persona[2] <- 10
	persona[3] <- 10
	persona[4] <- 3
	persona[5] <- 8
	persona[6] <- 50	
	persona[7] <- 4
	persona[8] <- 9
	persona[9] <- 69
	persona[10] <- 50
	persona[11] <- 70
	persona[12] <- 5
	persona[13] <- 9
	persona[14] <- 80
	persona[15] <- 5
	persona[16] <- 0
	persona[17] <- 0
	persona[18] <- 0
	p=0
	
		Mientras  p>=0 Hacer
			Escribir "1 .- Cantidad de personas vivan en un a�o determinado"
			Escribir "2 .- Edad de la persona mas joven en determinado a�o"
			Escribir "3 .- Edad de la persona mas vieja en determinado a�o"
			p=p-1
		Fin Mientras
		Leer opcion
		
		Segun opcion Hacer
			caso 1:
				Escribir "Ingrese un a�o:"
				Leer a�oDeseado
				// Inicializar una variable para verificar si el a�o se encuentra
				encontrado <- Falso
				// Recorrer el arreglo de a�os
				Para i desde 1 hasta 18 Hacer
					Si A�os[i] == a�oDeseado Entonces
						encontrado <- Verdadero
					Fin Si
				Fin Para
				// Verificar si el a�o fue encontrado
				Escribir 'Ingresa la persona'
				Leer cantidadeseada
				Para m desde 1 Hasta 18 Hacer
						Si persona[m] >= persona[16] Entonces
							Si persona[m] == cantidadeseada Entonces
								np= (persona[m]+3)*(1+10^3)
								Escribir 'El numero de personas es: ' np ' en el a�o: ' a�oDeseado 
							Fin Si
						Fin Si
					FinPara
				Caso 2:
					Escribir "Ingrese un a�o:"
					Leer a�oDeseado
					// Inicializar una variable para verificar si el a�o se encuentra
					encontrado <- Falso
					// Recorrer el arreglo de a�os
					Para i desde 1 hasta 18 Hacer
						Si A�os[i] == a�oDeseado Entonces
							encontrado <- Verdadero
						Fin Si
					Fin Para
					Escribir 'Elige el a�o del 1 al 18 de acuerdo al a�o elegido'
					Leer m
					Para m desde 1 Hasta 18 Hacer
						Si m=persona[m] Entonces
								ameno=(m+persona[m])
								Escribir 'La persona mas joven de: ', a�oDeseado ' tiene: ', ameno ' a�os'
						Fin Si
					FinPara
				caso 3:
					Escribir "Ingrese un a�o:"
					Leer a�oDeseado
					// Inicializar una variable para verificar si el a�o se encuentra
					encontrado <- Falso
					// Recorrer el arreglo de a�os
					Para i desde 1 hasta 18 Hacer
						Si A�os[i] == a�oDeseado Entonces
							encontrado <- Verdadero
						Fin Si
					Fin Para
					Escribir 'Elige el a�o del 1 al 18 de acuerdo al a�o elegido'
					Leer m
						Si m=m Entonces
							ameno=m+10
							Escribir 'La persona mas vieja de: ', a�oDeseado ' tiene: ', ameno ' a�os'
						Fin Si
			De Otro Modo: Escribir 'La persona mas vieja de: ', a�oDeseado ' tiene: ', ameno ' a�os'
		Fin Segun

	
	
FinAlgoritmo
