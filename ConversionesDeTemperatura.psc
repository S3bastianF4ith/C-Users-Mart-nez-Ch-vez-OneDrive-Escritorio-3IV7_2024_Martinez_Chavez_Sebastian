Algoritmo ConversionesDeTemperatura
	Escribir 'Escriba los grados en farenheit'
	Leer f
	j=0
	Escribir 'Eliga la opcion que usted desee realizar'
	Mientras  j>=0 Hacer
		Escribir "1 .- Farenheit a Celsius"
		Escribir "2 .- Farenheit a Kelvin"
		Escribir "3 .- Farenheit a Rankine"
		Escribir "4 .- Salir"
		j=j-1
	Fin Mientras 
	Escribir 'Eliga la conversion que desea hacer'
	Leer opcion
	Segun opcion Hacer
		1:
			c=((f-32)/1.8)
			Escribir c '° Celsius'
		2:
			k=((f-32)/1.8)+273.15
			Escribir k '° Kelvins'
		3:
			r=f+459.67
			Escribir r '° Rankine'
	Fin Segun
	
FinAlgoritmo
