"""Continue detiene la ejecución de la iteración (vuelta) actual y pasa a la siguiente.
En el ejemplo anterior vemos dos ciclos, 
parecidos al anterior ya explicado. Hay un momento en el que se compara si i==7, 
y luego ocurre un continue. 
Es decir, cuando el valor sea 7, termina la iteración actual (ya no ejecuta print(i)) 
y pasa a la siguiente iteración (i+=1)."""

class continuar:
    

    def conti(self):
        i=0
        
        while i<10:
            i+=1
            if i==7:
                continue
            print(i)

objeto = continuar()
objeto.conti()



