#las listas son inmutables no se pueden utilizar los metodos(append, insert, remove, etc.) aunque si permite la busqueda de elementos
class tuplasClases():
    
    def funciontupla(self):
        mitupla = ("Andres", 1, 1984, 5)
        print(mitupla)#muestra los elementos de la tupla
        print(mitupla[2])#muestra el elemento que se encuentra en la posicion 2
        listatupla = list(mitupla)#convierte una tupla en lista
        print(listatupla)
        milista=["Liliana", 1, 1988, 5, 1]
        tuplalista = tuple(milista)#convierte una lista en tupla
        print(tuplalista)
        print(1988 in tuplalista)#busca si un elemento de encuentra en la tupla con true
        print(tuplalista.count(1))#cuenta cuantas veces aparece el 1 en la lista
        print(len(tuplalista))#muestra la longitus de la tuplas
        tuplaunitaria = ("Andres",)#para que sea una tupla unitaria se debe colocar la coma para que indique que contiene un unico elemanto
        print(len(tuplaunitaria))
        tuplasinparentesis = "andres", "sara", 1, 3, 2013 #la tupla sin parentesis se denomina empaquetado de tuplas
        print(tuplasinparentesis)
        tupla4 = ("Andres", 29, 6, 1984)
        nombre, dia, mes, anio = tupla4 #desempaquetado de tuplas
        print(nombre, dia, mes, anio)
        tupla5 = ("Lucia", 2, 4, 5)
        print(tupla5.index(5)) #muestra la posicion en que se encuentra el elemento en la tupla 
        


objetotupla = tuplasClases()
objetotupla.funciontupla()




