class notaEjemplo():

    def calculoNota(self, nota):
    
        if nota>=3:
            print("Aprobado")
        else:
            print("No aprobado")


recibe = input("Digite la Nota: ")
examen = notaEjemplo()
examen.calculoNota(int(recibe))






