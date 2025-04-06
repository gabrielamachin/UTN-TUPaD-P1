# Ejercicio 1
# Solicitar la edad del usuario
edad = int(input("Ingresa tu edad: "))

# Verificar si el usuario es mayor de 18 años
if edad > 18:
    print("Es mayor de edad.")
else:
    print("No es mayor de edad.")

# Ejercicio 2
# Solicitar la nota del usuario
nota = float(input("Ingresa tu nota: "))

# Verificar si la nota es mayor o igual a 6
if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")

# Ejercicio 3
# Solicitar un número al usuario
numero = int(input("Ingresa un número: "))

# Verificar si el número es par
if numero % 2 == 0:
    print("Ha ingresado un número par.")
else:
    print("Por favor, ingrese un número par.")

# Ejercicio 4
# Solicitar la edad del usuario
edad = int(input("Ingresa tu edad: "))

# Determinar la categoría según la edad
if edad < 12:
    print("Niño/a")
elif edad >= 12 and edad < 18:
    print("Adolescente")
elif edad >= 18 and edad < 30:
    print("Adulto/a joven")
else:
    print("Adulto/a")

# Ejercicio 5
# Solicitar la contraseña al usuario
contraseña = input("Ingrese una contraseña: ")

# Verificar la longitud de la contraseña
if 8 <= len(contraseña) <= 14:
    print("Ha ingresado una contraseña correcta.")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres.")

# Ejercicio 6
import random
from statistics import mode, median, mean

# Generar una lista de 50 números aleatorios entre 1 y 100
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

# Calcular la moda, la mediana y la media
moda = mode(numeros_aleatorios)
mediana = median(numeros_aleatorios)
media = mean(numeros_aleatorios)

# Mostrar los resultados
print(f"Moda: {moda}")
print(f"Mediana: {mediana}")
print(f"Media: {media}")

# Comparar la moda, la mediana y la media para determinar el sesgo
if media > mediana > moda:
    print("Sesgo positivo o a la derecha.")
elif media < mediana < moda:
    print("Sesgo negativo o a la izquierda.")
else:
    print("No hay sesgo.")

# Ejercicio 7
# Solicitar una frase o palabra al usuario
texto = input("Ingresa una frase o palabra: ")

# Verificar si el último carácter es una vocal
if texto[-1].lower() in 'aeiouáéíóú':
    texto += '!'
    
# Imprimir el resultado
print(texto)

# Ejercicio 8
# Solicitar el nombre al usuario
nombre = input("¿Cuál es tu nombre? ")

# Solicitar la opción de transformación
opcion = int(input("Selecciona una opción:\n1. Mayúsculas\n2. Minúsculas\n3. Primera letra mayúscula\n"))

# Transformar el nombre según la opción seleccionada
if opcion == 1:
    print(nombre.upper())
elif opcion == 2:
    print(nombre.lower())
elif opcion == 3:
    print(nombre.title())
else:
    print("Opción no válida. Por favor, ingresa 1, 2 o 3.")

# Ejercicio 9
# Solicitar la magnitud del terremoto
magnitud = float(input("Introduce la magnitud del terremoto en la escala de Richter: "))

# Clasificar según la magnitud
if magnitud < 3:
    print("Muy leve (imperceptible).")
elif 3 <= magnitud < 4:
    print("Leve (ligeramente perceptible).")
elif 4 <= magnitud < 5:
    print("Moderado (sentido por personas, pero generalmente no causa daños).")
elif 5 <= magnitud < 6:
    print("Fuerte (puede causar daños en estructuras débiles).")
elif 6 <= magnitud < 7:
    print("Muy Fuerte (puede causar daños significativos).")
else:
    print("Extremo (puede causar graves daños a gran escala).")

# Ejercicio 10
# Solicitar información al usuario
hemisferio = input("¿En qué hemisferio te encuentras? (Ingresa N para norte, S para sur): ").upper()
mes = int(input("¿En qué mes del año estás? (Ingresa 1 para enero, 2 para febrero, etc.): "))
dia = int(input("¿Qué día del mes es? (1-31): "))

# Determinar la estación según el hemisferio, mes y día
if hemisferio == 'N':
    # Hemisferio norte
    if (mes == 12 and dia >= 21) or (mes <= 3 and dia <= 20):  # Invierno: 21 diciembre - 20 marzo
        estacion = "Invierno"
    elif (mes == 3 and dia >= 21) or (mes <= 6 and dia <= 20):  # Primavera: 21 marzo - 20 junio
        estacion = "Primavera"
    elif (mes == 6 and dia >= 21) or (mes <= 9 and dia <= 20):  # Verano: 21 junio - 20 septiembre
        estacion = "Verano"
    else:  # Otoño: 21 septiembre - 20 diciembre
        estacion = "Otoño"

elif hemisferio == 'S':
    # Hemisferio sur
    if (mes == 12 and dia >= 21) or (mes <= 3 and dia <= 20):  # Verano: 21 diciembre - 20 marzo
        estacion = "Verano"
    elif (mes == 3 and dia >= 21) or (mes <= 6 and dia <= 20):  # Otoño: 21 marzo - 20 junio
        estacion = "Otoño"
    elif (mes == 6 and dia >= 21) or (mes <= 9 and dia <= 20):  # Invierno: 21 junio - 20 septiembre
        estacion = "Invierno"
    else:  # Primavera: 21 septiembre - 20 diciembre
        estacion = "Primavera"

else:
    estacion = "Hemisferio inválido. Por favor, ingresa 'N' o 'S'."

# Imprimir la estación correspondiente
print(f"La estación en el hemisferio {hemisferio} en el mes {mes} y día {dia} es: {estacion}")
