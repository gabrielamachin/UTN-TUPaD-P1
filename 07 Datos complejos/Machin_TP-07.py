# Ejercicio 1
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}

precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300

print(precios_frutas)

# Ejercicio 2
precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800

print(precios_frutas)

# Ejercicio 3
lista_frutas = list(precios_frutas.keys())

print(lista_frutas)

# Ejercicio 4
# Crear diccionario vacío para los contactos
agenda = {}

# Cargar 5 contactos
print("Carga 5 contactos:")
for i in range(5):
    nombre = input(f"Ingresa el nombre del contacto #{i+1}: ")
    numero = input(f"Ingresa el número de teléfono de {nombre}: ")
    agenda[nombre] = numero

# Consultar un número
consulta = input("\nIngresa el nombre del contacto que quieres buscar: ")

# Verificar si existe y mostrar el número
if consulta in agenda:
    print(f"El número de {consulta} es: {agenda[consulta]}")
else:
    print(f"No se encontró ningún contacto con el nombre '{consulta}'.")

# Ejercicio 5
# Solicitar una frase al usuario
frase = input("Ingresa una frase: ")

# Separar la frase en palabras
palabras = frase.lower().split()  # Conversión a minúsculas, para evitar duplicados por mayúsculas

# Obtener palabras únicas usando un set
palabras_unicas = set(palabras)
print("\nPalabras únicas:")
print(palabras_unicas)

# Contar frecuencia de cada palabra usando un diccionario
conteo_palabras = {}
for palabra in palabras:
    if palabra in conteo_palabras:
        conteo_palabras[palabra] += 1
    else:
        conteo_palabras[palabra] = 1

print("\nCantidad de veces que aparece cada palabra:")
print(conteo_palabras)

# Ejercicio 6
# Crear un diccionario para almacenar los alumnos y sus notas
alumnos = {}

# Ingresar datos de 3 alumnos
for i in range(3):
    nombre = input(f"Ingresa el nombre del alumno #{i+1}: ")
    notas = input(f"Ingresa 3 notas separadas por espacios para {nombre}: ")
    notas = tuple(map(float, notas.split()))
    
    # Verificar que haya exactamente 3 notas
    if len(notas) != 3:
        print("Por favor ingresa exactamente 3 notas.")
        continue
    
    alumnos[nombre] = notas

# Calcular y mostrar el promedio de cada alumno
print("\nPromedios:")
for nombre, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f"{nombre}: {promedio:.2f}")

# Ejercicio 7
# Sets con nombres de estudiantes que aprobaron cada parcial
parcial1 = {"Sofia", "Luis", "Marcos", "Jorge", "Luciana"}
parcial2 = {"Luis", "Marcos", "Romina", "Luciana", "Melina"}

# Estudiantes que aprobaron ambos parciales (intersección)
ambos = parcial1 & parcial2
print("Aprobaron ambos parciales:")
print(ambos)

# Estudiantes que aprobaron solo uno (diferencia simétrica)
solo_uno = parcial1 ^ parcial2
print("\nAprobaron solo uno de los parciales:")
print(solo_uno)

# Estudiantes que aprobaron al menos un parcial (unión)
al_menos_uno = parcial1 | parcial2
print("\nAprobaron al menos un parcial:")
print(al_menos_uno)

# Ejercicio 8
# Diccionario de productos con stock
stock_productos = {
    "cuadernos": 20,
    "agendas": 35,
    "lapiceras": 15
}

# Mostrar el stock actual
print("Stock actual:")
for producto, stock in stock_productos.items():
    print(f"{producto}: {stock} unidades")

# Pedir al usuario un producto
producto = input("\nIngresa el nombre de un producto: ").lower()

# Verificar si el producto existe
if producto in stock_productos:
    print(f"El stock actual de '{producto}' es: {stock_productos[producto]} unidades.")
    
    # Consultar si el usuario desea agregar unidades
    agregar = input("Quieres agregar unidades a este producto? (Sí/No): ").lower()
    if agregar == "sí":
        unidades = int(input("¿Cuántas unidades quieres agregar?: "))
        stock_productos[producto] += unidades
        print(f"Nuevo stock de '{producto}': {stock_productos[producto]} unidades.")
else:
    print(f"El producto '{producto}' no está en el stock.")
    agregar_nuevo = input("¿Quieres agregarlo como nuevo producto? (Sí/No): ").lower()
    if agregar_nuevo == "sí":
        unidades = int(input(f"¿Cuántas unidades tiene '{producto}'?: "))
        stock_productos[producto] = unidades
        print(f"Producto '{producto}' agregado con {unidades} unidades.")

# Mostrar stock actualizado
print("\nStock actualizado:")
for producto, stock in stock_productos.items():
    print(f"{producto}: {stock} unidades")

# Ejercicio 9
agenda = {
    ("Lunes", "10:00"): "Reunión con el equipo",
    ("Martes", "15:30"): "Llamadas con clientes",
    ("Miércoles", "09:00"): "Clase de inglés"
}

# Consultar actividad
dia = input("Ingresá el día: ")
hora = input("Ingresá la hora (ej. 10:00): ")

clave = (dia, hora)

if clave in agenda:
    print(f"Actividad agendada: {agenda[clave]}")
else:
    print("No hay ninguna actividad agendada en ese día y horario.")

# Ejercicio 10
original = {
    "Argentina": "Buenos Aires",
    "Chile": "Santiago",
    "Brasil": "Brasilia"
}

diccionario_invertido = {capital: pais for pais, capital in original.items()}

print(diccionario_invertido)