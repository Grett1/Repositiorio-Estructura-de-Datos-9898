# Lista de elementos
numeros = [1, 2, 3, 4, 5]

numero_buscado = 6
mensaje_encontrado = f"El número {numero_buscado} se encuentra en la lista."
mensaje_no_encontrado = f"El número {numero_buscado} no se encuentra en la lista."

if numero_buscado in numeros:
    print(mensaje_encontrado)
else:
    print(mensaje_no_encontrado)