def conversion_binaria():
    # Definir num como entero
    num = int(input('Ingresa el número que deseas convertir: '))
    
    # Inicializar binario como una cadena vacía
    binario = ''
    
    if num >= 0:
        while num > 0:
            residuo = num % 2
            # Concatenar el residuo a la izquierda
            binario = str(residuo) + binario
            
            # Actualizar num usando la división entera
            num //= 2  # Trunc(num / 2)
        
        # Si el número es 0
        if binario == '':
            binario = '0'
        
        print('El número binario es:', binario)

# Llamar a la función
conversion_binaria()

def conversion_decimal():
    # Definir binario como texto
    binario = input('Ingresa el número binario que deseas convertir: ')
    
    # Inicializar el resultado decimal
    decimal = 0
    
    # Recorrer cada dígito del número binario
    for i, digito in enumerate(reversed(binario)):
        if digito == '1':
            decimal += 2 ** i  # Calcular la potencia de 2 correspondiente
    
    print('El número decimal es:', decimal)

# Llamar a la función
conversion_decimal()
