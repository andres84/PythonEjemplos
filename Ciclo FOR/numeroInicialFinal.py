#muestra los numeros enteros que hay dentro de un rango
ni = int(input("Digite el primer numero: "))
nf = int(input("Digite el segundo numero: "))
ini = ni
f = nf
c = 1
ni+=1
nf-=1

for i in range(ni, nf, c):
    c+=1
print("La cantidad de numeros que hay entre ", ini, " y ", f, " son: ", c)
