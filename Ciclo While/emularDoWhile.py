#emula un ciclo do while

palabra_secreta = "python"
counter = 0

while True:
    palabra = input("Ingresa la palabra secreta: ").lower()
    counter = counter + 1
    if palabra == palabra_secreta:
        break
    if palabra != palabra_secreta and counter == 7: 
        print("Lo intestaste al menos 7 veces!!!")        
        break
