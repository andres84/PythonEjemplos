"""La variable i contiene un dato numérico que inicia en 0. 
El ciclo while  contiene una condición (i < 10) que es evaluada (¿true o false?), 
mientras el resultado sea True ejecutará todas las lineas indentadas debajo de while. 
Éstas líneas incrementan la variable i en 1 (i+=1), 
lo que eventualmente la llevará a valer 10 lo que hará que abandone el ciclo."""

class imprimeNumeros(object):
    
    def imprime(self):
        
        i=0
        
        while i<10:    
            i+=1
            print (i)

objeto = imprimeNumeros()
objeto.imprime()



