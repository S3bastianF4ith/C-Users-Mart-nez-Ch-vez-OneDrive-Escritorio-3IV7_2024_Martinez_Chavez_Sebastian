Algoritmo Gestion_Reservas_Hotel
	Definir x, mes, messalida como texto
	Definir dia, año, diasalida, añosalida, habitacion como Entero
	Definir precio Como Real
	i=0
	j=0
	habitaciones=20
	manager<-02530
	Escribir 'Bienvenude, hotel de 20 habitaciones'
	Escribir 'Cuantas acciones realizara?'
	Leer j
	Repetir
		Mientras  i>=0 Hacer
			Escribir "1 .- Registro de reservas"
			Escribir "2 .- Cancelacion de reservas"
			Escribir "3 .- Consulta de disponibilidad"
			Escribir "4 .- Gestion de ocupacion (manager only)"
			Escribir "5 .- Salir"
			i=i-1
		Fin Mientras
		Leer opcion
		
		Segun opcion Hacer
			Caso 1:
				Si habitaciones>0 Entonces
					Escribir 'Selecciona tu habitacion del 1 al 20'
					Leer seleccion
					habitaciones=habitaciones-1
				SiNo
					Si habitacion=seleccion Entonces
						Escribir 'Por el momento esa habitacion no esta disponibles'
					Fin Si
				Fin Si
				Escribir 'Escriba el dia de llegada para su reservacion'
				Leer dia
				Escribir 'Escriba el mes'
				Leer mes
				Escribir 'Escriba el año'
				Leer año
				Escribir 'Escriba el dia de salida de su reservacion'
				Leer diasalida
				Escribir 'Escriba el mes de salida'
				Leer messalida
				Escribir 'Escriba el año de salida'
				Leer añosalida
				numeroreserva<-año*dia+seleccion
				Escribir 'Escriba (Seguro) para confirmar su reservacion' 
				Leer x
				Escribir 'Registro exitoso, su reservacion es de la habitacion: ', seleccion ' y la fecha reservada de llegada es es: ', dia mes año, ' Su fecha de salida es: ', diasalida messalida añosalida, ' Su numero de reserva es: ', numeroreserva
			Caso 2:
				Escribir 'Introduzca numero de reserva para cancelar la reservacion'
				Leer numeroreserva
				Si numeroreserva=numeroreserva Entonces
					habitacion<-habitacion+1
					Escribir 'Listo, su reservacion fue cancelada con exito'
				Fin Si
			Caso 3:
				Escribir 'Escriba la habitacion que quiere revisar'
				Leer seleccion
				Si selecion=seleccion Entonces
					Escribir 'ocupada del: ', dia mes año, ' hasta el: ', diasalida messalida añosalida
				SiNo
					Escribir 'Habitacion libre'
				Fin Si
			Caso 4:
				Escribir 'Ingrese el valor de manager'
				Leer manager
				Si manager=02530 Entonces
					total=(habitaciones*100)/20
					Escribir total ' Porcentaje de ocupacion del hotel'
				SiNo
					Escribir 'Codigo incorrecto'
				Fin Si
		Fin Segun
		j=j-1
	Hasta Que j=0
	
FinAlgoritmo
