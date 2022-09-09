#Los diccionarios son estructura de datos que permiten almacenar valores de diferente tipo
#La principal carcateristica es que contienen una clave y un valor - clave:valor
#se encierran entre corchetes

class diccioEjemplo():
    
    
    def metodoDic(self):
    
        midiccionario = {"Alemania":"Berlin","Colombia":"Bogota","Espania":"Madrid","Ecuador":"Quito"}
        print(midiccionario) #Muestra todo el diccionario
        print(midiccionario["Colombia"]) #muestra el valor segun la clave
        midiccionario["Italia"] = "Lisboa" # asigna una nueva clave con su valor
        print(midiccionario)
        midiccionario["Italia"] = "Roma" #corrige la asignacion anterior sobreescribiendo el valor
        print(midiccionario)
        del midiccionario["Espania"] #elimina una clave con su valor
        print(midiccionario)
        midiccionario2 = {"Alemania":"Berlin", 1:"Sara", "Datos":2} #diccionario con varios tipos de datos
        print(midiccionario2)
        mitupla = ("Colombia", "Italia", "Portugal")
        diccionarioTupla = {mitupla[0]:"Bogota", mitupla[1]:"Roma", mitupla[2]:"Lisboa"} #agregar una tupla a un diccionario
        print(diccionarioTupla)
        diccionario2 = {23:"Jordan", "Nombre":"Michael", "Equipo":"Bull", "Anillos":(1991,1992,1993,1996,1997,1998)} #guarda una tupla dentro de un diccionario
        print(diccionario2)
        print(diccionario2["Anillos"]) #muestra el valor segun la clave
        diccionario3 = {23:"Jordan", "Anillos":{"Temporadas":(1991,1992,1993,1996,1997,1998)}} #guarda un diccionario dentro de otro
        print(diccionario3)
        print(diccionario3["Anillos"])
        print(diccionario3.keys()) #Muestra las claves del diccionario
        print(diccionario3.values()) #Muestra los valores del diccionario
        print(len(diccionario3)) #Muestra la longitud del diccionario

objdic = diccioEjemplo()
objdic.metodoDic()


