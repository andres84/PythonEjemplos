#ojo tener cuidado en definir bien los tabs en las funciones
"""
def funcion1():
	numero1 = 5
	nuemro2 = 2
		
	if(numero1>nuemro2):
		print("el numero1 es mayor")
	elif(numero1<nuemro2):
		print("el nuemero2 es mayor")
	else:
		print("los numeros son iguales")

funcion1()"""

"""def funcion2():
	numero=[1, 2, 3, 4]

	for k in numero:
		print(k)


funcion2()"""


"""def metodo1():
	for mostrar in range(3):
			print(mostrar)


metodo1()"""

"""class carro():
	# init method or constructor
    def __init__(self, model, color):
        self.model = model
        self.color = color
         
    def show(self):
        print("Model is", self.model )
        print("color is", self.color )
         
# both objects have different self which
# contain their attributes
audi = carro("audi a4", "blue")
ferrari = carro("ferrari 488", "green")
 
audi.show()     # same output as car.show(audi)
ferrari.show()  # same output as car.show(ferrari)"""



class datosejemplo():
	def __init__(self, contenido):
			self.contenido = contenido
	def mostrar(self):
			print("El datos es: ", self.contenido)
		
datos1 = datosejemplo("caparazon")
datos1.mostrar()





 











