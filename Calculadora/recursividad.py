# Ejercitación Clase 5 (Recursividad)
# 1. Realizar una función recursiva que calcule la suma de los primeros números naturales:
# def sumar_naturales (numero:int) -> int:
# 5 + 4 + 3 + 2 + 1 = 15

# def sumar_natuarles (numero: int) -> int:

#   if numero == 0 or numero == 1:
#     resultado = 1

#   elif numero > 1:
#     resultado = numero + sumar_natuarles(numero - 1)
#   return resultado
  
# print(sumar_natuarles(5))

# 2. Realizar una función recursiva que calcule la potencia de un número:
# def calcular_potencia (base:int , exponente:int) -> int:

# def calcular_potencia (base:int , exponente:int) -> int:
#   if exponente == 0:
#     return 1

#   resultado = base * calcular_potencia(base, exponente - 1 )
#   return resultado

# print(calcular_potencia(5, 3))


# 3. Realizar una función para calcular el número de Fibonacci (investigar que es) de un número ingresado por consola. La función deberá seguir el siguiente prototipo:

# def calcular_fibonacci (numero:int) -> int:
#   if numero == 0:
#     return 0
#   elif numero == 1:
#     return 1
#   else:
#     return calcular_fibonacci( numero -1 ) + calcular_fibonacci( numero -2 )

# numero = 10

# for i in range(numero):
#   print(calcular_fibonacci(i))
  
# Ejercitación Clase 5 (Funciones Avanzado)


# 1. Desarrollar una función que verifique el DNI de una persona, la misma recibirá un str (se asume que solamente contiene caracteres numéricos).
#  Si la cantidad de caracteres es menor a 6 o mayor a 8, retornara False. Si la cantidad de caracteres está comprendida entre 6 y 8 devolverá True

# Para saber la cantidad de elementos de un str usamos la función len()

# numero = input("Ingrese su DNI: ")

# def verificar_dni(numero:str) -> str:
#   if len(numero) < 6 or len(numero) > 8:
#     return False
#   else:
#     return True

# print(verificar_dni(numero))

# 2. Desarrollar una función que complete el número de DNI de una persona. Recibirá un str (se asume que solamente contiene caracteres numéricos),
#  deberá medirla (len) y completar con ceros a la izquierda hasta llegar a un total de 8 caracteres, y devolviendo la cadena resultante. 
# En caso de que el dni sea invalido (que no tiene entre 6 y 8 caracteres) devolvera una cadena que dice : “DNI INVALIDO”

# Ej: Se ingresa “12345”, y devolverá “DNI INVALIDO”.
# Ej: Se ingresa “123456”, y devolverá “00123456”.
# Ej: Se ingresa “1234567”, y devolverá “01234567”.
# Ej: Se ingresa “12345678”, y devolverá “12345678”.
# Ej: Se ingresa “123456789”, y devolverá “DNI INVALIDO”.

# Nota: Reutilizar la función del ejercicio 1 para validar si el dni es válido

# def completar_dni( numero ):
#   numero_verificado: str = verificar_dni(numero)

#   if numero_verificado == False:
#     print("DNI INVÁLIDO")
#   else:
#     cantidad_caracteres = len(numero)
#     if cantidad_caracteres == 6:
#       print(f"00{ numero }")
#     elif cantidad_caracteres == 7:
#       print(f"0{ numero }")
#     else: 
#        print(numero)

# completar_dni(numero)