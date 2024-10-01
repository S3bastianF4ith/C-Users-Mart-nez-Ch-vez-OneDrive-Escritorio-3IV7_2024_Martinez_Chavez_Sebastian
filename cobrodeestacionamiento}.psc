Algoritmo sin_titulo
	Definir horaentrada, minutoentrada, segundosentrada, horasalida, minutosalida, segundosalida Como Reales
	Definir totalhoras, totalminutos, minutostotalescuenta, totalsegundos Como Reales
	Definir  totalcobro Como Reales
	
	//Entrada de datos
	Escribir  ' Ingrese la hora de entrada (FORMATO DE 24 HORAS)'
	Leer horaentrada
	Escribir  ' Ingrese los minutos de entrada (FORMATO DE 0 A 59)'
	Leer minutoentrada
	Escribir  ' Ingrese los segundos de entrada (FORMATE DE 0 A 59)'
	Leer segundosentrada
	Escribir  ' Ingrese la hora de de salida (FORMATO DE 24 HORAS)'
	Leer horasalida
	Escribir  ' Ingrese los minutos de salida (FORMATO DE 0 A 59)'
	Leer minutosalida
	Escribir  ' Ingrese los segundos de salida (FORMATO DE 0 A 59)'
	Leer segundosalida
	
	//Proceso 
	//calcular el tiempo total en minutos
	totalhoras =horasalida-horaentrada
	totalminutos=minutosalida-minutoentrada
	totalsegundos=segundosalida-segundosentrada
	
	//evaluar casos
	Si totalminutos<0 Entonces
		totalminutos=totalminutos+60
		totalhoras=totalhoras-1
	Fin Si
	Si totalsegundos<0 Entonces
		totalsegundos=totalsegundos+60
		totalminutos=totalminutos-1
	Fin Si
	
	//convertitr a minutos
	segunminutos=(totalsegundos/60)
	totalminutos=(totalhoras*60)+totalminutos+segunminutos
	
	//calculo de cobro
	totalcobro=0
	//per hora completa
	Si totalminutos >= 60 Entonces
		totalcobro=totalcobro+(totalminutos/60)*15
	Fin Si
	//cobro de cada fraccion
	minutosrestantes=totalminutos*0.60
	Si minutosrestantes>0 Entonces
		fracciones15min=minutosrestantes
		totalcobro=totalcobro+fracciones15min*6
	Fin Si
	//cobrar cada fraccion 
	//mostrar el resultado
	Escribir 'El total a pagar es de: ', totalcobro, 'pesos'
	
	
FinAlgoritmo
