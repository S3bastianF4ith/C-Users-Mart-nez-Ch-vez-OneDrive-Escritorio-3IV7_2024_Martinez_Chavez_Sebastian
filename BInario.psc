Algoritmo ConversionBinaria
	Definir num, cosciente Como Entero;
	Definir binario Como Texto;
	//El binario debe de concatenarse
	binario = '';
	Escribir  'Ingresa el numero que deseas convertir';
	Leer num;
	
	Si num >= 0 Entonces
		Mientras num > 0 Hacer
			residuo = num%2;
			nuevobinario <- ConvertirATexto(residuo)
			binario = nuevobinario + binario
			
			num = Trunc(num/2)
		Fin Mientras
		
		//Si el numero es 0
		si binario=='' Entonces
			binario ='0'
		FinSi
		Escribir 'El numero binario es: ', binario
	Fin Si
FinAlgoritmo
