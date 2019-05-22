a = int(input("Ingrese cantidad de elementos: "))
n = []

for i in range (a):
    i = int(input("Ingrese número: "))
    n.append(i)

print(n)

maximo = max(n)
minimo = min(n)

n.insert(0,minimo)
n.remove(minimo)
n.insert(a+1,maximo)
n.remove(maximo)
print(n)
