Algoritmo La_Vida_De_Las_Personas
	Definir año, edad, persona Como Entero
	Dimension Años[18]
	Años[1] <- 1930 
	Años[2] <- 1940
	Años[3] <- 1960
	Años[4] <- 1972
	Años[5] <- 1980
	Años[6] <- 1990
	Años[7] <- 1999
	Años[8] <- 2000
	Años[9] <- 2000
	Años[10] <- 2000
	Años[11] <- 2001
	Años[12] <- 2010
	Años[13] <- 2010
	Años[14] <- 2012
	Años[15] <- 2037
	Años[16] <- 2040
	Años[17] <- 2042
	Años[18] <- 2050
	
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
			Escribir "1 .- Cantidad de personas vivan en un año determinado"
			Escribir "2 .- Edad de la persona mas joven en determinado año"
			Escribir "3 .- Edad de la persona mas vieja en determinado año"
			p=p-1
		Fin Mientras
		Leer opcion
		
		Segun opcion Hacer
			caso 1:
				Escribir "Ingrese un año:"
				Leer añoDeseado
				// Inicializar una variable para verificar si el año se encuentra
				encontrado <- Falso
				// Recorrer el arreglo de años
				Para i desde 1 hasta 18 Hacer
					Si Años[i] == añoDeseado Entonces
						encontrado <- Verdadero
					Fin Si
				Fin Para
				// Verificar si el año fue encontrado
				Escribir 'Ingresa la persona'
				Leer cantidadeseada
				Para m desde 1 Hasta 18 Hacer
						Si persona[m] >= persona[16] Entonces
							Si persona[m] == cantidadeseada Entonces
								np= (persona[m]+3)*(1+10^3)
								Escribir 'El numero de personas es: ' np ' en el año: ' añoDeseado 
							Fin Si
						Fin Si
					FinPara
				Caso 2:
					Escribir "Ingrese un año:"
					Leer añoDeseado
					// Inicializar una variable para verificar si el año se encuentra
					encontrado <- Falso
					// Recorrer el arreglo de años
					Para i desde 1 hasta 18 Hacer
						Si Años[i] == añoDeseado Entonces
							encontrado <- Verdadero
						Fin Si
					Fin Para
					Escribir 'Elige el año del 1 al 18 de acuerdo al año elegido'
					Leer m
					Para m desde 1 Hasta 18 Hacer
						Si m=persona[m] Entonces
								ameno=(m+persona[m])
								Escribir 'La persona mas joven de: ', añoDeseado ' tiene: ', ameno ' años'
						Fin Si
					FinPara
				caso 3:
					Escribir "Ingrese un año:"
					Leer añoDeseado
					// Inicializar una variable para verificar si el año se encuentra
					encontrado <- Falso
					// Recorrer el arreglo de años
					Para i desde 1 hasta 18 Hacer
						Si Años[i] == añoDeseado Entonces
							encontrado <- Verdadero
						Fin Si
					Fin Para
					Escribir 'Elige el año del 1 al 18 de acuerdo al año elegido'
					Leer m
						Si m=m Entonces
							ameno=m+10
							Escribir 'La persona mas vieja de: ', añoDeseado ' tiene: ', ameno ' años'
						Fin Si
			De Otro Modo: Escribir 'La persona mas vieja de: ', añoDeseado ' tiene: ', ameno ' años'
		Fin Segun

	
	
FinAlgoritmo
