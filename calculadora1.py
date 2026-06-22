#calculadora de 0
import math


calculardora = []
def seleccion():
     opciones = [
    "sumar",
    "restar",
    "multiplicar",
    "dividir",
    "potencia",
    "raíz cuadrada",
    "módulo",
    "porcentaje",
    "salir"
    ]
     operaciones = {
    1: sumar,
    2: restar,
    3: multiplicacion,
    4: division,
    5: potencia,
    6: raiz,
    7: modulo,
    8: porcentaje,
}
     print("\nMENU DE OPCIONES")
     while True:
        
        for i, opcion in enumerate(opciones, start=1):
         print(f"{i}. {opcion}")

        eleccion = int(input("Seleccione una opción: "))
         
        if eleccion == 9:  # ahora "salir" es la opción 9
            print("Hasta luego")
            break
  
        a = float(input("Introduzca el primer número: "))

        if eleccion == 6:  # raíz solo necesita un número
            b = None
        else:
            b = float(input("Introduzca el segundo número: "))

        if eleccion in operaciones:
            resultado = operaciones[eleccion](a, b)
            print("Resultado:", resultado)
        else:
             print("Opción inválida")

def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b == 0:
     return "no se puede dividir"
    return a / b
def potencia(a, b):
    return a ** b

def raiz(a, b=None):
    if a < 0:
        return "no se puede calcular raíz de un número negativo"
    return math.sqrt(a)

def modulo(a, b):
    if b == 0:
        return "no se puede calcular módulo con divisor 0"
    return a % b

def porcentaje(a, b):
    return (a * b) / 100
     
print("se termino la calculadora")

#tenes q ponerle while para crear bucle, hacerle menu y eleccion de opciones

seleccion()