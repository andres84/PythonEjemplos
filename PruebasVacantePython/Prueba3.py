"""
Pregunta 3
myArray = [1,2,1,3,3,1,2,1,5,1]
Escribir un programa en Python que recorra un arreglo y genere un histograma en base a los numeros de este. 
El arreglo se llama myArray y contiene 10 elementos que corresponden a numeros enteros del 1 al 5. 
Un histograma representa que tanto un elemento aparece en un conjunto de datos 
(Debe mostrar la frecuencia para todos los numeros del 1 al 5, incluso si no estan presentes en el arreglo). 
Por ejemplo, para el arreglo: myArray:=(1,2,1,3,3,1,2,1,5,1) el histograma se veria asi:

1: *****
2: **
3: **
4:
5: *

El codigo para declarar y poblar myArray ya está ahí, 
puede editarlo para probar con otros valores y puede hacer clic en el botón de actualizar junto a él 
para volver al valor original que se utilizará para validar su código durante la prueba. 
Asegúrese de que los resultados se impriman exactamente como aparecen aquí, ya que incluso un espacio faltante 
o sobrante puede marcar la pregunta como incorrect (Notar espacio entre los ":" y el primer asterisco).
"""

myArray = [1,2,1,3,3,1,2,1,5,1]

mapa_datos = {}

for dato in myArray:
	if dato in mapa_datos:
		mapa_datos[dato]+=1
	else:
		mapa_datos[dato] = 1
		
for valor in mapa_datos:#sorted(mapa_datos):
	print(f'{valor}:{"*" * mapa_datos[valor]}')

