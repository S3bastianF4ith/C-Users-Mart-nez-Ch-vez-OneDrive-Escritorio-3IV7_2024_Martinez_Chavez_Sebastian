Algoritmo ConversionesDeUnidades
	Escribir 'Escriba la medida en pies'
	Leer patas
	i=0
	Escribir 'Eliga la opcion que usted desee realizar'
	Mientras  i>=0 Hacer
		Escribir "1 .- Pies a Pulgadas"
		Escribir "2 .- Pies a Yardas"
		Escribir "3 .- Pies a Centimetros"
		Escribir "4 .- Pies a Metros"
		Escribir "5 .- Salir"
		i=i-1
	Fin Mientras 
	Escribir 'Eliga la conversion que desea hacer'
	Leer opcion
	Segun opcion Hacer
		1:
			pulgadas=patas*12
			Escribir pulgadas 'In'
		2:
			yardas=patas/3
			Escribir yardas 'Yd'
		3:
			centimetros=patas*2.54
			Escribir centimetros 'Cm'
		4:
			metro=patas/3.281	
			Escribir metro 'M'
	Fin Segun
	
FinAlgoritmo
