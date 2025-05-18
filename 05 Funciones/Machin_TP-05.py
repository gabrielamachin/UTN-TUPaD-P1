# Ejercicio 1
def imprimir_hola_mundo():
    print("Hola Mundo!")

# Ejercicio 2
def saludar_usuario(nombre):
    return f"Hola {nombre}!"

# Ejercicio 3
def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")

# Ejercicio 4
import math
def calcular_area_circulo(radio):
    return math.pi * (radio ** 2)

def calcular_perimetro_circulo(radio):
    return 2 * math.pi * radio

# Ejercicio 5
def segundos_a_horas(segundos):
    horas = segundos // 3600
    return horas

# Ejercicio 6
def tabla_multiplicar(numero):
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

# Ejercicio 7
def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b if b != 0 else "Indefinido"
    return suma, resta, multiplicacion, division

# Ejercicio 8
def calcular_imc(peso, altura):
    return peso / (altura ** 2)

# Ejercicio 9
def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# Ejercicio 10
def calcular_promedio(a, b, c):
    return (a + b + c) / 3

# Programa principal
# 1 Llamada a la función imprimir_hola_mundo
imprimir_hola_mundo()

# 2 Llamada a la función saludar_usuario
nombre_usuario = input("¿Cómo te llamas? ")
print(saludar_usuario(nombre_usuario))

# 3 Llamada a la función informacion_personal
nombre = input("Ingresa tu nombre: ")
apellido = input("Ingresa tu apellido: ")
edad = input("Ingresa tu edad: ")
residencia = input("Ingresa tu lugar de residencia: ")
informacion_personal(nombre, apellido, edad, residencia)

# 4 Llamada a las funciones calcular_area_circulo y calcular_perimetro_circulo
radio = float(input("Ingresa el radio del círculo: "))
area = calcular_area_circulo(radio)
perimetro = calcular_perimetro_circulo(radio)
print(f"El área del círculo es: {area}")
print(f"El perímetro del círculo es: {perimetro}")

# 5 Llamada a la función segundos_a_horas
segundos = int(input("Ingresa una cantidad de segundos: "))
print(f"{segundos} segundos son {segundos_a_horas(segundos)} horas.")

# 6 Llamada a la función tabla_multiplicar
numero = int(input("Ingresa un número para ver su tabla de multiplicar: "))
tabla_multiplicar(numero)

# 7 Llamada a la función operaciones_basicas
a = float(input("Ingresa el primer número: "))
b = float(input("Ingresa el segundo número: "))
resultados = operaciones_basicas(a, b)
print(f"Suma: {resultados[0]}")
print(f"Resta: {resultados[1]}")
print(f"Multiplicación: {resultados[2]}")
print(f"División: {resultados[3]}")

# 8 Llamada a la función calcular_imc
peso = float(input("Ingresa tu peso en kg: "))
altura = float(input("Ingresa tu altura en metros: "))
imc = calcular_imc(peso, altura)
print(f"Tu IMC es: {imc:.2f}")

# 9 Llamada a la función celsius_a_fahrenheit
celsius = float(input("Ingresa la temperatura en grados Celsius: "))
fahrenheit = celsius_a_fahrenheit(celsius)
print(f"{celsius}°C son {fahrenheit}°F.")

# 10 Llamada a la función calcular_promedio
a = float(input("Ingresa el primer número para calcular el promedio: "))
b = float(input("Ingresa el segundo número: "))
c = float(input("Ingresa el tercer número: "))
promedio = calcular_promedio(a, b, c)
print(f"El promedio es: {promedio}")