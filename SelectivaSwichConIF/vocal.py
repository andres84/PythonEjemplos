print("--- Programa que dice que tipo de letra es ---")

letra = input("Digite una letra: ")
l = letra.lower()

"""def tipoLetra():
    if l == "a" or l == "e" or l == "i" or l == "o" or l == "u":
        print("La letra es una Vocal")
    elif l[0:2]:
        print("Debe digitar solo una letra, no numeros ni palabras")
    else:
        print("La letra es una Consonante")

tipoLetra()"""

def a():
    print("La letra es una Vocal")
def e():
    print("La letra es una Vocal")
def i():
    print("La letra es una Vocal")
def o():
    print("La letra es una Vocal")
def u():
    print("La letra es una Vocal")
def consonante():
    if l != "a" or "e" or "i" or "o" or "u":
        print("es una consonante")
def error():
    if l.isnumeric():
        print("Error!!! es un numero")


vocales ={

    1:a,
    2:e,
    3:i,
    4:o,
    5:u,
    6:consonante
}

if len(l) > 1:
    print("Solo debe escribir una letra")
elif l == "a":
    vocales.get(1, error)()
elif l == "e":
    vocales.get(2, error)()
elif l == "i":
    vocales.get(3, error)()
elif l == "o":
    vocales.get(4, error)()
elif l == "u":
    vocales.get(5, error)()
elif l.isalpha():
    vocales.get(6, error)()
else:
    error()