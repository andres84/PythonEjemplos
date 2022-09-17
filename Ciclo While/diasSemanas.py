class diasSemanas:
    
    def semana(self):
        
        dia = 0    
        
        semana = ['Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes', 'Sabado', 'Domingo']
        while dia < 7:
            print("Hoy es " + semana[dia])
            dia += 1

objeto = diasSemanas()
objeto.semana()


