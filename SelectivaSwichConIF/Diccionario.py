def lunes():
	print('lunes')

def martes():
	print('martes')

def miercoles():
	print('miercoles')

def jueves():
	print('jueves')

def viernes():
	print('viernes')

def sabado():
	print('sabado')

def domingo():
	print('domingo')

def error():
	print('error')


switchSemana = {
	
	1:lunes, 
	2:martes,	
	3:miercoles, 
	4:jueves, 
	5:viernes, 
	6:sabado, 
	7:domingo
	
	}

dia = 5

#tomamos la funcion asociada a la variable y la invocamos
switchSemana.get(dia, error)()