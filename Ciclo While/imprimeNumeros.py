"""La variable i contiene un dato num�rico que inicia en 0. 
El ciclo while  contiene una condici�n (i < 10) que es evaluada (�true o false?), 
mientras el resultado sea True ejecutar� todas las lineas indentadas debajo de while. 
�stas l�neas incrementan la variable i en 1 (i+=1), 
lo que eventualmente la llevar� a valer 10 lo que har� que abandone el ciclo."""

class imprimeNumeros(object):
    
    def imprime(self):
        
        i=0
        
        while i<10:    
            i+=1
            print (i)

objeto = imprimeNumeros()
objeto.imprime()



