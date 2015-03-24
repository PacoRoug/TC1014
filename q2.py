def find_threes(lista):
    threes=0
    for i in lista:
        i=float(i)
        if (i/3 == int(i/3)):
            threes=threes+i
    return int(threes)


lista=[]
n=input("Número para la lista. Escribe 'ya' para terminar la lista ")
while (n != "ya"):
    lista.append(n)
    n=input("Siguiente número ")
print("Total:",find_threes(lista))

