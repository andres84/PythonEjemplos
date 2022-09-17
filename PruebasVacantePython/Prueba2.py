"""
Pregunta 2
myArray = [13,2,4,35,1,35,7]
Tienes un arreglo (llamado myArray) con 5 elementos (enteros en el rango de 1 a 100). 
Escribe un programa en Python que imprima el numero mas alto del arreglo (Si se repite, solo imprimir una vez). 
El programa solo debe imprimir el numero, sin ningun texto.
"""

myArray = [13,2,4,35,1,35,7]

def mayor(numero):
    maximo = None
    for numero in myArray:
        if maximo is None or numero > maximo:
            maximo = numero
    print(maximo)

mayor(myArray)