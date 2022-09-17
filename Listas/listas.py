#las listas son mutables
class listas:
    
    def funcionlista(self):
        milista = ["Andres", "Liliana", "Sara", "Isabella", "Lucia", "Santiago", 1, 2, 3]
        print("1: ", milista[:])#muestra toda la lista
        print("2: ", milista[2])#muestra el contenido de la posicion de la lista teniendo en cuenta que la lista comienza en 0
        print("3: ", milista[-2])#muestra la segunta posicion de la lista en orden inversa
        print("4: ", milista[0:4])#muestra el contenido de la lista desde la posicion 0 hasta la 4
        print("5: ", milista[:4])#toma los cuatro primeros elementos de la lista
        print("6: ", milista[1:3])#muestra el contenido de la lista en la posicion 1 y 2
        print("7: ", milista[2:])#toma los elementos de la lista desde la posicion 2
        milista.append("4")#incliye un nuevo elemento en la lista en la ultima posicion
        print("8: ", milista[:])
        milista2 = [1, 2, 3]
        milista2.insert(2, 7) #incluye un nuevo elemento en la lista en la posicion 2
        print("9: ", milista2[:])
        milista3 = [1, 2, 3, 4]
        milista3.extend([5, 6, 7, 8])#incluye varios elementos a la lista
        print("10: ", milista3[:])
        print("11: ", milista.index("Isabella")) #muestra la posicion de la lista donde se encuentra el elemento
        print("12: ", "Liliana" in milista)#marca true si el elemento se encuentra en la lista
        milista.remove(1)#remueve el elemento de la lista
        print("13: ", milista[:])
        milista.pop()#elimina el ultimo elemento de la lista
        print("14: ", milista[:])
        milista4 = [1, 2, 3, 4] * 3#repite la lista tres veces
        print("15: ", milista4[:])

objetolista = listas()
objetolista.funcionlista()





