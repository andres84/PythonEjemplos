"""En el ejemplo anterior se crea un ciclo infinito (while True). 
Con esto indicamos que el ciclo siempre se ejecuta pues while nunca obtiene un Falso. (Tudor, 2019) 
�C�mo se sale del ciclo? Cuando i==13 se ejecuta la instrucci�n break. Eso termina la ejecuci�n de todo el ciclo."""

class infinito:
    
    def infini(self):
        i =0
        while True:
            i+=1
            print(i)
            if i==13:
                break

objeto = infinito()
objeto.infini()




