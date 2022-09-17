letra = input("Digite una letra: ")
l = letra.lower()

def letras():
    if len(l) > 1:
        print("Tiene mas de una letra", l)
    else:
        print(l)

letras()
