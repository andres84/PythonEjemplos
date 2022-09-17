from tkinter import *
from time import *
#texto_hora=""
#texto_dia = ""
#texto_fecha = ""
#dia = strftime()
#hora = strftime()
#fecha = strftime()
ventana = Tk() #se crea el objeto de tipo Tk para los graficos
ventana.title("Reloj Digital") #titulo del frame
ventana.config(bg="white") #fondo del frame
ventana.geometry("350x550+500+100") #la funcion geometry da las dimenciones del cuadro(350x250) y da la posicion en el plano cartesiano xy(500+100) 
ventana.minsize(width=250, height=500) #el usuario puede establecer el tamanio inicializado de la ventana en su tamanio minimo y aun asi poder maximizar y ampliar la ventana.
ventana.columnconfigure(0, weight=15)
ventana.rowconfigure(0, weight=15)
ventana.columnconfigure(0, weight=1)
ventana.rowconfigure(1, weight=1)
ventana.columnconfigure(0, weight=1)
ventana.rowconfigure(2, weight=1)

def obtener_tiempo():
    hora = strftime("%H:%M:%S")
    dia = strftime("%A")
    fecha = strftime("%d - %m - %y")
    x = texto_hora.winfo_height()
    t = int((x-5)*0.32)
    if dia =='Monday':
	    dia = 'Lunes'
    elif dia =='Tuesday':
	    dia = 'Martes'
	elif dia =='Wednesday':
	    dia = 'Miercoles'
	elif dia =='Thursday':
	dia = 'Jueves'
	elif dia =='Friday':
	    dia = 'Viernes'
elif dia =='Saturday':
	dia = 'Sabado'
elif dia =='Sunday':
	dia = 'Domingo'

texto_hora.config(text=hora, font = ('Radioland', t))
texto_dia.config(text=dia )
texto_fecha.config(text=fecha)
	
texto_hora.after(1000, obtener_tiempo)

texto_hora = Label(ventana,  fg = 'aqua', bg='black')
texto_hora.grid(row=0,sticky="nsew", ipadx=5, ipady=20)
texto_dia = Label(ventana,  fg = 'white',  bg='gray2', font = ('Lucida Calligraphy',20))
texto_dia.grid(row=1,sticky="nsew")
texto_fecha = Label(ventana,  fg = 'green2',  bg='gray3', font = ('Comic Sans MS',20, 'bold'))
texto_fecha.grid(row=2,sticky="nsew")


obtener_tiempo()
ventana.mainloop() #el metodo mainloop ejecuta el grafico
