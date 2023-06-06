lista = []

print(type(lista))

lista = ["Ecuador", "Colombia", "Brasil"]
print(lista)

lista = ["Juan", 45, 6.4, True, ["Ecuador", "Colombia", "Brasil"]]
print(lista)

lista = ["Ecuador", "Colombia", "Brasil"]
lista.append("Mexico")
print(lista)

lista2 = lista.copy()
print(lista2)

lista2.clear()
print(lista2)

lista2 = lista.copy()
print(lista2.count("Colombia"))

lista2.append("Bolivia")
lista2.append("Colombia")
print(lista2.count("Colombia"))

print(lista2)

print(len(lista2))

print(lista2[3])
print(lista2[1])

lista2[5] = "Peru"
print(lista2)

print(lista2.index("Colombia"))

#eliminar elementos de una lista

lista2.pop() #elimina el ultimo elemento de la lista
print(lista2)

lista2.remove("Brasil") #Elimina un elemento en especifico
print(lista2)

lista2.reverse() #da la vuelta los elemento de la lista
print(lista2)

lista2.sort() #organiza los elementos segun el codigo asci
print(lista2)

lista3 = ["d" ,"B","b","c"]
lista3.sort()
print(lista3)

#TUPLAS

tupla = ()
print(type(tupla))

"""tupla.append("Diego")
print(tupla)"""

tupla2 = ("Juan", "Pedro", "Maria", "Juan")
print(tupla2)

print(tupla2.count("Juan"))
print(tupla2.index("Maria"))

# ctrl k y cntr c comenta una linea automaticamente
# ctrl K y ctrl U descomenta una linea

print(tupla2[2])
print(tupla2[3])

lista = list(tupla2) # de tupla a lista
print(type(lista))

lista.append("Mario")
print(lista)

tupla2 = tuple(lista) # de lista a tupla
print(tupla2)

#Range

rango = range(6)
print(rango)

# Set

set = {2,3,4,5,6,6}
print(set)
print(type(set))

#Diccionarios

cliente001 = {
    "Nombre" : "Diego",
    "Cedula" :  1354864982,
    "Celular" : "0987654321",
    "Correo" : "ejemplo@gmail.com"
}

print(cliente001)
print(type(cliente001))

print(cliente001["Correo"])
print(cliente001.get("Celular"))

cliente001["Nombre"] = "Juan"
print(cliente001.get("Nombre"))
print(cliente001)

print(len(cliente001)) #longitud del diccionario

cliente001["EstadoCivil"]="Viudo" #agregar elemento
print(cliente001)

cliente001.popitem() #elimina el ultimo elemento del diccionario
print(cliente001)

cliente001.pop("Celular")
print(cliente001)

del cliente001["Cedula"]
print(cliente001)

cliente002 = dict(cliente001)
print(cliente001)
print(cliente002)

