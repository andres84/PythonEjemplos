print("Digite el numero de una estacion: 1.Verano - 2.Otonio - 3.Invierno - 4.Primavera")
estacion = input()
casteo = int(estacion)

def verano():
    print("Usted selecciono: Verano")
def otonio():
    print("Usted selecciono: Otonio")
def invierno():
    print("Usted selecciono: Ivierno")
def primavera():
    print("Usted selecciono: Primavera")
def error():
    print("Error!!!, debe selecionar el numero del 1 al 4 de una estacion")

switch_diccionario = {
    
    1:verano,
    2:otonio,
    3:invierno,
    4:primavera
        
    }

switch_diccionario.get(casteo, error)()