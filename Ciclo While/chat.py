

print("Bienvenidos al chat")

chatOpen = True

while chatOpen:
    texto = input(">>")
    if texto == "salir":
        chatOpen = False
    texto = texto.replace(':)', '🙂')
    print(texto)
    
    


