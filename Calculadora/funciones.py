def sumar( numero1:float, numero2:float ) -> float:
  ''''
    La función calcula la suma de dos números recibidos por parámetro.
    Retorna el resultado de dicha suma
  '''
  return numero1 + numero2

def restar( numero1, numero2 ):
  ''''
    La función calcula la resta de dos números recibidos por parámetro.
    Retorna el resultado de dicha resta
  '''
  return numero1 - numero2

def multiplicar( numero1, numero2 ):
  ''''
    La función calcula la multiplicción de dos números recibidos por parámetro.
    Retorna el resultado de dicha multiplicación
  '''
  return numero1 * numero2

def dividir( numero1, numero2 ):
  ''''
    La función calcula la division de dos números recibidos por parámetro.
    Retorna el resultado de dicha división siempre y cuando no se intente
    dividir por 0
  '''

  return numero1 / numero2

def potencia( numero1, numero2 ):
  ''''
    La función calcula la la potencia del primer parámetro elevado al segundo parámetro.
    Retorna el resultado de dicha potencia
  '''
  return numero1 ** numero2

def resto( numero1, numero2 ):
  ''''
    La función calcula el resto de una division entre dos números recibidos por parámetro.
    Retorna el resto de dicha división siempre y cuando no se intente
    dividir por 0
  '''
  return numero1 % numero2

def factorial_A( numero ):
  ''''
    La función recibe un parámetro y crea un ciclo FOR para iterar desde el número 1
    hasta el numero recibido por argumento + 1 (para incluir al numero recibido en la firma 
    de la función) Se  calcula el factorial acumulando los resultados de multiplicar el número
    almacenado en la variable resultado por la cantidad de iteraciones del ciclo.
    Cumple con el objetivo de obtener el número factorial pero no con el de ser RECURSIVA.
  '''
  resultado = 1
  for i in range(1, numero + 1):
    resultado *= i  
  return resultado

      
  

def factorial_B( numero ):
  ''''
    La función recibe un parámetro y valida que el mismo sea 1. Ya que el factorial de 0 y 1 es preci
    samente el número 1. Basado en esa premisa matemática almancena en la variable resultado
    el valor de multiplicar al numero recibido - 1 hasta llegar al numero 1. De esta forma la función
    se llama a si misma hasta cumplir con la condición dada como base.
  '''
  if numero == 0 or numero == 1:
    resultado = 1

  elif numero > 1:
    resultado = numero * factorial_B(numero - 1)
  return resultado




