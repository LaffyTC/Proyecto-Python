lista = [15,"Nombre",3.1415,True]
#lista.extend([3,4])      ##Añade otra lista a la lista inicial.
#lista.append(3)      ##Añade un elemento al final de la lista.
#lista.insert (15, 3)   ##Añade un elemento en una posición determinada.
#lista.remove(15)   ##Busca un dato de la lista y lo borra.
#lista.pop()    ##Elimina el último elemento de la lista, si se le da una posición, elimina el elemento en
                #aquel lugar.
#lista.reverse()    ##Invierte el orden de la lista.
#lista.sort()   ##Ordena los elementos de menor a mayor.
#lista.sort(reverse=true)   ##Ordena los elementos de mayor a menor.

print(lista[3])

usuario = ["usernameTest1","pass123","correo@correo.cl"]

numeros = [10,50,100,255,500]
numeros.append(1000)

extra=[75, 350,999]
numeros.extend(extra)
print(numeros)

numeros.insert(6,5000)
print(numeros)

numeros.remove(50)
print(numeros)

numeros.pop()
print(numeros)

numeros.pop(3)
print(numeros)

numeros.reverse()
print(numeros)

numeros.sort()
print(numeros)

numeros.sort(reverse=True)
print(numeros)