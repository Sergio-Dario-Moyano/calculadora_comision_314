import os
from funciones import *


def menu():
    bandera_numero1 = False
    bandera_numero2 = False
    bandera_operaciones = False
    while(True):
        print("MENU CALCULADORA\n1.Ingresar Primer Operando\n2.Ingresar Segundo Operando\n3.Calcular Todas las operaciones\n4.Informar Resultados\n5.Salir")
        opcion = int(input("Su opcion: "))
        if opcion == 1:
            operando1 = input("Ingreso Primer Operando: ")
            while True:
                if operando1.strip() == "":
                    print("<------- ERROR...El campo está vacío, reingrese un número: --------->")
                    operando1 = input("Ingreso Primer Operando: ")
                else:
                    break
            numero1 = int(operando1)
            bandera_numero1 = True

        elif opcion == 2:
            operando2 = input("Ingreso Segundo Operando: ")
            while True:
                if operando2.strip() == "":
                    print("<------- ERROR...El campo está vacío, reingrese un número: --------->")
                    operando2 = input("Ingreso segundo Operando: ")
                else:
                    break
            numero2 = int(operando2)
            bandera_numero2 = True
            bandera_operaciones = True

        elif opcion == 3:
            if bandera_numero1 == False or bandera_numero2 == False:
                print("<---------- ERROR... NO HAY OPERANDOS PARA REALIZAR LA OPERACION -------------->")
                menu()
              
            resultado_suma:float = sumar(numero1, numero2)
            resultado_resta:float = restar(numero1, numero2)
            resultado_multiplicacion:float = multiplicar(numero1, numero2)
            
            resultado_division:float = dividir(numero1, numero2)
            
            resultado_potencia:float = potencia(numero1, numero2)
            resultado_resto:float = resto(numero1, numero2)
            factorial_a = factorial_A( numero1 )
            factorial_b = factorial_B( numero2 )
           
            print("¡¡Todas las operaciones fueron realizadas exitosamente!!")

        elif opcion == 4:
            if bandera_operaciones == True:
                print(f'''
                    EL resultado de la suma de los operandos es: {resultado_suma}
                    -------------------------------------------------------------
                    EL resultado de la resta de los operandos es: {resultado_resta}
                    -------------------------------------------------------------
                    EL resultado de la multiplicación de los operandos es: {resultado_multiplicacion}
                    -------------------------------------------------------------
                    EL resultado de la división de los operandos es: {resultado_division}
                    -------------------------------------------------------------
                    EL resultado de la potencia de los operandos es: {resultado_potencia}
                    -------------------------------------------------------------
                    EL resultado de la resto de los operandos es: {resultado_resto}
                    -------------------------------------------------------------
                    EL fctorial del número 1 es: {factorial_a}
                    -------------------------------------------------------------
                    EL fctorial del número 2 es: {factorial_b}
                ''')
            else:
                print("ERROR, no hay resultados que informar")

        elif opcion == 5:
            print("Saliendo...")
            break
        else:
            print("Opcion invalida ingrese números entre 1-5")
        input("Pulse boton para continuar...")
        os.system('clear')

    
    
menu()
