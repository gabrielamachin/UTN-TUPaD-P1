# Ejercicio 1
print("Hola Mundo!")

# Ejercicio 2
nombre = input("¿Cuál es tu nombre? ")
print(f"Hola {nombre}!")

# Ejercicio 3
nombre = input("¿Cuál es tu nombre? ")
apellido = input("¿Cuál es tu apellido? ")
edad = input("¿Cuántos años tienes? ")
residencia = input("¿Dónde vives? ")
print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")

# Ejercicio 4
import math
radio = float(input("¿Cuál es el radio del círculo? "))
area = math.pi * (radio ** 2)
perimetro = 2 * math.pi * radio

print(f"El área del círculo es: {area:.2f}")
print(f"El perímetro del círculo es: {perimetro:.2f}")

# Ejercicio 5
segundos = int(input("¿Cuántos segundos quieres convertir a horas? "))
horas = segundos // 3600  # 1 hora = 3600 segundos

print(f"{segundos} segundos equivalen a {horas} horas.")

# Ejercicio 6
numero = int(input("¿De qué número deseas ver la tabla de multiplicar? "))

print(f"Tabla de multiplicar del {numero}:")
for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")

# Ejercicio 7
numero1 = int(input("Ingresa el primer número (distinto de 0): "))
numero2 = int(input("Ingresa el segundo número (distinto de 0): "))

if numero1 == 0 or numero2 == 0:
    print("Los números no deben ser 0. Por favor, ingresa números distintos de 0.")
else:
    suma = numero1 + numero2
    resta = numero1 - numero2
    multiplicacion = numero1 * numero2
    division = numero1 / numero2

    print(f"La suma de {numero1} y {numero2} es: {suma}")
    print(f"La resta de {numero1} y {numero2} es: {resta}")
    print(f"La multiplicación de {numero1} y {numero2} es: {multiplicacion}")
    print(f"La división de {numero1} y {numero2} es: {division:.2f}")

# Ejercicio 8
peso = float(input("¿Cuál es tu peso en kilogramos? "))
altura = float(input("¿Cuál es tu altura en metros? "))

imc = peso / (altura ** 2)
print(f"Tu índice de masa corporal (IMC) es: {imc:.2f}")

# Ejercicio 9
celsius = float(input("¿Cuál es la temperatura en grados Celsius? "))

fahrenheit = (9/5) * celsius + 32
print(f"La temperatura en Fahrenheit es: {fahrenheit:.2f}")

# Ejercicio 10
numero1 = float(input("Ingresa el primer número: "))
numero2 = float(input("Ingresa el segundo número: "))
numero3 = float(input("Ingresa el tercer número: "))

promedio = (numero1 + numero2 + numero3) / 3
print(f"El promedio de los tres números es: {promedio:.2f}")