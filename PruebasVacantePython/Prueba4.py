"""
Pregunta 4
n=5
Escribir un programa en Python que imprima una X construida a base de la letra X 
y utilizar el carácter de subrayado como espacio. 
El tamaño de la x se basa en una variable n que indicará el tamaño de la letra para imprimir (en una matriz de n x n). Por ejemplo, para n = 5 se obtiene:

X___X
_X_X_
__X__
_X_X_
X___X

y para n=6 se obtiene:

X____X
_X__X_
__XX__
__XX__
_X__X_
X____X

Si n es igual a cero imprimir "ERROR"
"""

def dato1(n):
    for i in range(n):
        for j in range(n):
            if (i == 0 or i == 5) and (j == 0 or j == 5):
                print("*", end='')
            elif (i == 1 or i == 4) and (j == 1 or j == 4):
                print("*", end='')
            elif (i == 2 or i == 3) and (j == 2 or j == 3):
                print("*", end='')
            else:
                print("_", end='')
        print()

def dato2(variable):
    
    for i in range(variable):
        for j in range(variable):
            if (i == 0 or i == 4) and (j == 0 or j == 4):
                print("*", end='')
            elif (i == 1 or i == 3) and (j == 1 or j == 3):
                print("*", end='')
            elif (i == 2 or i == 2) and (j == 2 or j == 2):
                print("*", end='')
            else:
                print("_", end='')
        print()

n = int(input("Digite 5 ó 6: "))
if n == 5:
   dato2(n)
elif n == 6:
   dato1(n)
elif n == 0:
   print("Error!!!")
else:
    print("Solo debe digitar 5 ó 6!!!")