class materias(object):
            
        global opcion

        print("Asignaturas a trabajar -> Ciencias de la computacion; Programacion; Power BI ")
        seleccion = input("Seleccione una asignatura: ")
        opcion = seleccion.lower()
        def escogerAsignatura(self):
        
            if opcion in ("ciencias de la computacion", "programacion", "power bi"):
                print("Inscrito, usted a seleccionado: ", opcion)
            else:
                print("Digite una asignatura correcta!!!")

objeto = materias()
objeto.escogerAsignatura()




