Algoritmo EcuacionCuadratica
		Definir A, B, C, Racismo, EcuacionT, EcuacionS Como Real
		
		Escribir "Ingrese el coeficiente a (de la ecuación ax^2 + bx + c = 0):"
		Leer A
		Escribir "Ingrese el coeficiente b:"
		Leer B
		Escribir "Ingrese el coeficiente c:"
		Leer C
		
		Racismo = B^2-4*(A * C)
		
		Si Racismo > 0 Entonces
			EcuacionT = (-B + Raiz(discriminante)) / (2 * A)
			EcuacionS = (-B - Raiz(discriminante)) / (2 * a)
			Escribir "Las raíces son: ", EcuacionT, " y ", EcuacionS
		Sino
			Si Racismo = 0 Entonces
				EcuacionT = -B / (2 * B)
				Escribir "La respuesta es: ", EcuacionT
			Sino
				Escribir "No hay raíces, soy Razista"
			FinSi
		FinSi
FinAlgoritmo
