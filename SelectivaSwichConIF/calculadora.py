print("--- Calculadora ---")

n1 = input("Digite el primer numero: ")
n2 = input("Digite el segundo numero: ")
op = input("Digite el operador +, -, *, / para la operacion matematica: ")

num1 = int(n1)
num2 = int(n2)

def suma():
    resulsum = num1 + num2
    print("El resultado es: ", resulsum)

def resta():
    resulres = num1 - num2
    print("El resultado es: ", resulres)

def multiplicacion():
    resulmul = num1 * num2
    print("El resultado es: ", resulmul)

def division():
    if num2 != 0:
        resuldiv = num1 / num2
        print("El resultado es: ", resuldiv)
    else:
        print("Error!!! No se puede dividir por cero")

def error():
    print("Error!!!, debes escoger un caracter de operacion matematica")


operaciones = {
    
    1:suma,
    2:resta,
    3:multiplicacion,
    4:division

    }

if op == "+":
    operaciones.get(1, error)()
elif op == "-":
    operaciones.get(2, error)()
elif op == "*":
    operaciones.get(3, error)()
elif op == "/":
    operaciones.get(4, error)()
else:
    error()

