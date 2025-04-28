# Ejercicio 1
lista_multiplos_4 = list(range(4,101,4))
print(lista_multiplos_4)

# Ejercicio 2
lista_colores = ["Azul","Verde","Violeta", "Gris","Blanco"]
print(lista_colores[-2])

# Ejercicio 3
lista_vacia = []
lista_vacia.append("lunes")
lista_vacia.append("martes")
lista_vacia.append("miercoles")
print(lista_vacia)

# Ejercicio 4
animales = ["perro", "gato", "conejo", "pez"]
animales[1] = "loro"
animales[-1] = "oso"
print(animales)

# Ejercicio 5
# En este ejercicio se crea una lista llamada numeros que contiene los siguientes elementos: [8, 15, 3, 22, 7].
# La función max() se aplica sobre la lista numeros, y devuelve el valor máximo, que es 22.
# Aquí, se llama al método remove() sobre la lista numeros, con el argumento 22.
# Después de esta operación, la lista numeros se modifica y el número 22 es eliminado.
# El programa imprime la lista numeros después de haber eliminado el valor máximo (22). La salida será: [8, 15, 3, 7]
numeros = [8, 15, 3, 22, 7]
numeros.remove(max(numeros))
print(numeros)

# Ejercicio 6
lista_multiplos_10 = list(range(10,31,5))
print(lista_multiplos_10[:2])

# Ejercicio 7
autos = ["sedan", "polo", "suran", "gol"]
autos[1] = "twingo"
autos[2] = "sandero"
print(autos)

# Ejercicio 8
dobles = []
dobles.append(str(5*2))
dobles.append(str(10*2))
dobles.append(str(15*2))
print(dobles)

# Ejercicio 9
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]
# a) Agregar "jugo" a la lista del tercer cliente usando append.
compras[2].append("jugo")

# b) Reemplazar "fideos" por "tallarines" en la lista del segundo cliente.
compras[1][1] = "tallarines"

# c) Eliminar "pan" de la lista del primer cliente.
compras[0].remove("pan")

# d) Imprimir la lista resultante por pantalla
print(compras)

# Ejercicio 10
lista_anidada = [15, True, [25.5, 57.9, 30.6], False]
print(lista_anidada)