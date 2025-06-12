# Ejercicio 1
# Función recursiva para calcular el factorial
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Solicitar número al usuario
num = int(input("Ingresa un número entero positivo: "))

# Calcular y mostrar el factorial de cada número del 1 al num
print(f"Factoriales del 1 al {num}:")
for i in range(1, num + 1):
    print(f"{i}! = {factorial(i)}")

# Ejercicio 2
# Función recursiva para obtener el valor en la posición n de la serie de Fibonacci
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Solicitar posición al usuario
pos = int(input("Ingresa la posición hasta la que deseas ver la serie de Fibonacci: "))

# Mostrar la serie completa hasta esa posición
print(f"Serie de Fibonacci hasta la posición {pos}:")
for i in range(pos + 1):
    print(f"F({i}) = {fibonacci(i)}")

# Ejercicio 3
# Función recursiva para calcular n^m
def potencia(n, m):
    if m == 0:
        return 1  # Caso base: cualquier número elevado a 0 es 1
    else:
        return n * potencia(n, m - 1)  # Fórmula recursiva

# Algoritmo general para probar la función
base = int(input("Ingrese la base (n): "))
exponente = int(input("Ingrese el exponente (m): "))

resultado = potencia(base, exponente)
print(f"{base}^{exponente} = {resultado}")

# Ejercicio 4
# Función recursiva para convertir un número decimal a binario
def decimal_a_binario(n):
    if n == 0:
        return ""
    else:
        return decimal_a_binario(n // 2) + str(n % 2)

numero = int(input("Ingrese un número entero positivo: "))

if numero == 0:
    print("0 en binario es: 0")
else:
    binario = decimal_a_binario(numero)
    print(f"{numero} en binario es: {binario}")

# Ejercicio 5
def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    if palabra[0] != palabra[-1]:
        return False
    return es_palindromo(palabra[1:-1])

palabra = input("Ingrese una palabra sin espacios ni tildes: ").lower()
print(f"¿'{palabra}' es palíndromo?: {es_palindromo(palabra)}")

# Ejercicio 6
def suma_digitos(n):
    if n < 10:
        return n
    else:
        return (n % 10) + suma_digitos(n // 10)

numero = int(input("Ingrese un número entero positivo para sumar sus dígitos: "))
print(f"La suma de los dígitos de {numero} es: {suma_digitos(numero)}")

# Ejercicio 7
def contar_bloques(n):
    if n == 1:
        return 1
    else:
        return n + contar_bloques(n - 1)
    
niveles = int(input("Ingrese el número de bloques en el nivel más bajo de la pirámide: "))
print(f"Se necesitan {contar_bloques(niveles)} bloques en total para construir la pirámide.")
    
# Ejercicio 8
def contar_digito(numero, digito):
    if numero == 0:
        return 0
    elif numero % 10 == digito:
        return 1 + contar_digito(numero // 10, digito)
    else:
        return contar_digito(numero // 10, digito)

numero = int(input("Ingrese un número entero positivo: "))
digito = int(input("Ingrese un dígito entre 0 y 9 para contar: "))
print(f"El dígito {digito} aparece {contar_digito(numero, digito)} veces en {numero}.")