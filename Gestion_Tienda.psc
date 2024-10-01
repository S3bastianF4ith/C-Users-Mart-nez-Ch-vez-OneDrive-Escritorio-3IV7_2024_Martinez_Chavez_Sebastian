Algoritmo Gestion_Tienda
	Definir producto como texto
	Definir codigo, cantidad como Entero
	Definir precio Como Real
	i=0
	Mientras  i>=0 Hacer
		Escribir "1 .- ingresar un nuevo Producto"
		Escribir "2 .- Actualiza un producto"
		Escribir "3 .- Consulta el inventario"
		Escribir "4 .- Generar Reporte"
		Escribir "5 .- Salir"
		i=i-1
	Fin Mientras 
	Leer opcion
	Segun opcion Hacer
		Caso 1:
			Escribir "Ingresa el nombre del producto"
			Leer producto
			Escribir "Ingresa el codigo del producto"
			Leer codigo
			Escribir "Ingresa la cantidad"
			Leer cantidad
			Escribir "Ingresa el precio"
			Leer precio
			
		Caso 2:
			Escribir "Ingresa el código del producto a actualizar"
			Leer codigoproducto
			Escribir "Ingresa la nueva cantidad"
			Leer cantidad
			
		Caso 3:
			Escribir "Consultar inventarios"
			Escribir "Nombre del producto ", producto
			Escribir "Código del producto ", codigo
			Escribir "Precio del producto ", precio
			Escribir "Cantidad del producto ", cantidad
			
		Caso 4:
			Escribir "Genere su reporte"
			
	Fin Segun
	
FinAlgoritmo
