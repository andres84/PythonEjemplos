"""
Pregunta 1

Escribir un programa en Python que puede determinar si una matriz es simetrica. 
Una matriz es simetrica si se ve igual si esta invertida. 

Por ejemplo ('a', 'b', 'c', 'd', 'd', 'c', 'b', 'a') es simetrica y ('a', 'b', 'c', 'd', 'd', 'b', 'c', 'a') 
no lo es. Suponga que n sera siempre un numero par entre 2 y 10 (No hay necesidad de validar esto). 
Si es simetrico su programa debe imprimir 'Symmetric', de lo contrario imprimir 'Asymmetric'

La salida de los datos para el arreglo en el ejemplo myArray = ['a', 'b', 'c', 'd', 'd', 'c', 'b', 'a'] seria:
Symmetric"""

myArray = ['a', 'b', 'c', 'd', 'd', 'c', 'b', 'a']

def invertido(cadena):
    if cadena == cadena[::-1]:
        print('Symmetric')
    else:
        print('Asymmetric')

invertido(myArray)