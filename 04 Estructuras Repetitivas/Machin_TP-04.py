# Ejercicio 1
for i in range(101):
    print(i)

# Ejercicio 2
# Solicitar un número al usuario
numero = int(input("Ingresa un número: "))

# Convertir el número a texto y contar los caracteres
cantidad_digitos = len(str(abs(numero)))

# Mostrar el resultado
print("Cantidad de dígitos:", cantidad_digitos)

# Ejercicio 3 -- Corregir
# Solicitar los dos números al usuario
inicio = int(input("Ingresa el primer número: "))
fin = int(input("Ingresa el segundo número: "))

# Validar que 'inicio' sea menor que 'fin'
if inicio > fin:
    inicio, fin = fin, inicio  # Intercambiar si están al revés

# Sumar los valores entre 'inicio' y 'fin', excluyendo ambos
suma = 0
for i in range(inicio + 1, fin):
    suma += i

# Mostrar el resultado
print("La suma de los enteros entre", inicio, "y", fin, "es:", suma)

# Ejercicio 4
# Inicializar la suma
suma_total = 0

print("Ingresa números enteros para sumarlos. Escribe 0 para terminar.")

while True:
    numero = int(input("Ingresa un número: "))
    if numero == 0:
        break
    suma_total += numero

# Mostrar el resultado
print("La suma total es:", suma_total)

# Ejercicio 5
import random

# Generar un número aleatorio entre 0 y 9
numero_secreto = random.randint(0, 9)

intentos = 0
adivinado = False

print("¡Adivina el número secreto entre 0 y 9!")

while not adivinado:
    intento = int(input("Tu intento: "))
    intentos += 1

    if intento == numero_secreto:
        adivinado = True
        print("¡Correcto! Adivinaste el número.")
    else:
        print("No adivinaste el número. Intenta de nuevo.")

print("Número de intentos:", intentos)

# Ejercicio 6
# Imprimir números pares del 100 al 0, en orden descendente
for i in range(100, -1, -1):
    if i % 2 == 0:
        print(i)

# Ejercicio 7
# Solicitar al usuario un número entero positivo
numero = int(input("Ingresa un número entero positivo: "))

# Validar que sea positivo
if numero < 0:
    print("El número debe ser positivo.")
else:
    suma = 0
    for i in range(0, numero + 1):
        suma += i
    print("La suma de los números de 0 a", numero, "es:", suma)

# Ejercicio 8
cantidad_numeros = 100

# Contadores
pares = 0
impares = 0
positivos = 0
negativos = 0

print(f"Ingrese {cantidad_numeros} números enteros:")

for _ in range(cantidad_numeros):
    num = int(input("Número: "))

    # Par o impar
    if num % 2 == 0:
        pares += 1
    else:
        impares += 1

    # Positivo o negativo
    if num > 0:
        positivos += 1
    elif num < 0:
        negativos += 1

# Resultados
print("\nResultados:")
print("Cantidad de números pares:", pares)
print("Cantidad de números impares:", impares)
print("Cantidad de números positivos:", positivos)
print("Cantidad de números negativos:", negativos)

# Ejercicio 9
cantidad_numeros = 100

suma_total = 0

print(f"Ingrese {cantidad_numeros} números enteros:")

for _ in range(cantidad_numeros):
    num = int(input("Número: "))
    suma_total += num

media = suma_total / cantidad_numeros

# Mostrar el resultado
print("\nLa media de los", cantidad_numeros, "números ingresados es:", media)

# Ejercicio 10
# Solicitar un número al usuario
numero = input("Ingresa un número: ")

# Invertir el orden de los dígitos y mostrarlo
numero_invertido = numero[::-1]
print("El número invertido es:", numero_invertido)




