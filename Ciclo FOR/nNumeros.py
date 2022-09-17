#suma los todos los numeros hasta el numero digitado
s = int(input("Digite un numero: "))
for i in range(s):
    print("suma hasta: ", s, " + ", i, " = ", s+i)
    s+=i
print("La suma de los N primeros numeros es: ",s)
