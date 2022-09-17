ni = int(input("Digite el primer numero: "))
nf = int(input("Digite el segundo numero: "))
titulo = input("-- Mostrar numeros pares o impares dentro del rango, presione enter!!! --")
mostrar = int(input("Presione 1 para par y 2 para impar: "))

def par():
    print("Estos son los numeros pares dentro del rango de ", ni, " a ", nf)
    for i in range(ni, nf + 1, 1):
        if i % 2 == 0:
            print(i)

def impar():
    print("Estos son los numeros impares dentro del rango de ", ni, " a ", nf)
    for i in range(ni, nf + 1, 1):
        if i % 2 != 0:
            print(i)

def error():
    print("muestra error")

dicParImpar = {    
   1:par,
   2:impar    
}

dicParImpar.get(mostrar, error)()

"""ni = int(input("Digite el primer numero: "))
nf = int(input("Digite el segundo numero: "))

def numerosPares():
    for i in range(ni, nf + 1, 1):
        if i % 2 == 0:
            print(i)

def numerosImpares():
    for i in range(ni, nf + 1, 1):
        if i % 2 != 0:
            print(i)

print("Numeros pares")
numerosPares()
print("Numeros impares")
numerosImpares()"""