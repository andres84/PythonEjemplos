from tkinter import *
from tkinter.ttk import *
from time import *
import locale

locale.setlocale(locale.LC_ALL, "es-ES") #define la fora y fecha en espaniol

def actualiza_reloj():
    etiqueta_hm.config(text=strftime("%H:%M"))
    etiqueta_s.config(text=strftime("%S"))
    etiqueta_fecha.config(text=strftime("%A, %d/%m/%y"))
    etiqueta_s.after(1000, actualiza_reloj)
    

app = Tk()
app.title("Reloj Digital")

frame_hora = Frame()
frame_hora.pack()
etiqueta_hm = Label(frame_hora, font=("Digitalk", 100), text="H:M")
etiqueta_hm.grid(row = 0, column = 0)

etiqueta_s = Label(frame_hora, font=("Digitalk", 50), text="S")
etiqueta_s.grid(row = 0, column = 1, sticky="n")

etiqueta_fecha = Label(font=("Digitalk", 50))
etiqueta_fecha.pack(anchor = "center")

actualiza_reloj()
app.mainloop()
