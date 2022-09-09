class mayorEdad():

    def calcularEdad(self, e):

        if 18 <= e <=20:
            print("Usted es mayor de edad")
        elif e >= 21:
            print("Usted es mayor de edad y puede consumir alcohol")
        else:
            print("Usted es menor de edad")


edad = input("Digite edad: ")
objeto = mayorEdad()
objeto.calcularEdad(int(edad))





