dato = input("Por favor ingrese algo:")

print(dato)

lista = ["Hola", "Mundo"]

if lista.count(dato) > 0:
    print("Esta informacion existe:", dato)
else:
    print("Esta informacion no existe", dato)
