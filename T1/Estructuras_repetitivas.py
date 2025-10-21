# Programa: Estructuras_repetitivas.py
# Propósito: Este programa es un conjunto de ejercicios de estructuras repetitivas
# Autor: Javier Acedo Caballero
# Fecha: 19/10/2025

import random


def even_numbers():
    num1 = int(input("Introduce el primer numero: "))
    num2 = int(input("Introduce el segundo numero: "))

    difference = num2 - num1
    counter = 0

    if difference > 1:
        for i in range(1, difference):
            val = num1 + i
            if val % 2 == 0:
                counter += 1
                print(f"Numero {counter}: {val}")


        if counter == 0:
            print("No hay numeros para imprimir")

    else:
        print("No hay numeros para imprimir")


def counter_numbers():
    counter_zero = 0
    counter_greater_zero = 0
    counter_lesser_zero = 0
    amount = int(input("Introduce el cantidad de numeros a introducir: "))

    for i in range(amount):
        if i == 0:
            counter_zero += 1
        elif i > 0:
            counter_greater_zero += 1
        else:
            counter_lesser_zero += 1

    print("La cantidad de numeros es: ", amount)
    print("La cantidad de numeros mayores a cero es: ", counter_greater_zero)
    print("La cantidad de numeros menores a cero es: ", counter_lesser_zero)
    print("La cantidad de ceros es: ", counter_zero)


def guess_the_number():
    random_number = random.randint(1, 100)
    winner = False
    print("Tienes 10 intentos para adivinar el numero")
    for i in range(10):
        print(f"Intento {i+1}")
        intent= int(input("Introduce un numero: "))
        if intent == random_number:
            print("El numero es CORRECTO")
            winner = True
            break
        else:
            print("El numero es INCORRECTO")
            if intent < random_number:
                print("El numero es más grande")
            else:
                print("El numero es más pequeño")

    if not winner:
        print("Has agotado todos los intentos")
        print("El numero era: ", random_number)


def limit_numbers():
    correct_limit = False
    while not correct_limit:
        lower_limit = int(input("Introduce limite inferior: "))
        top_limit = int(input("Introduce limite superior: "))
        if lower_limit > top_limit:
            print("el limite inferior no puede ser mas grande que el superior")
        else:
            correct_limit = True

    sum_numbers_limit = 0
    counter_over_limit = 0
    right_at_limit = False

    while True:
        number = int(input("Introduce un numero: "))
        if number == 0:
            break
        elif number < lower_limit or number > top_limit:
            counter_over_limit += 1
        elif number == lower_limit or number == top_limit:
            right_at_limit = True
        else:
            sum_numbers_limit += number

    print("La suma de los numeros que estan dentro del intervalo es: ", sum_numbers_limit)
    print("Cantida de numeros fuera de los limites: ", counter_over_limit)
    print("Número justo en los límites?: ", "Sí" if right_at_limit else "No")


def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

def prime_number():
    try:
        number = int(input("Introduce el numero: "))
        if number < 2:
            print("El numero no es valido, debe de ser mayor a 2")
        else:
            if is_prime(number):
                print(f"El número {number} es primo.")
            else:
                print(f"El número {number} no es primo.")

    except ValueError:
        print("Debes de introducir un numero entero valido")

def list_prime_numbers():
    counter = 0
    number = 2

    n = int(input("Introduce cantidad de numeros: "))
    if n<=0 :
        print("El numero no es valido, debe de ser mayor a 0")
        return

    while counter < n:
        if is_prime(number):
            print(f"{counter}: {number}")
            counter += 1
        number += 1


def calcular_cuota_mensual(capital, interes_anual, plazo_anios):
    n = plazo_anios * 12
    i = interes_anual / 100 / 12

    if i == 0:
        cuota = capital / n
    else:
        cuota = capital * (i * (1 + i)**n) / ((1 + i)**n - 1)

    return cuota

def generar_tabla_amortizacion(capital, interes_anual, plazo_anios):
    cuota = calcular_cuota_mensual(capital, interes_anual, plazo_anios)
    saldo_pendiente = capital
    i = interes_anual / 100 / 12
    n = plazo_anios * 12

    print("\nTabla de Amortización:")
    print(f"{'Cuota':<6}{'Cuota Mensual':<15}{'Interés':<12}{'Amortización':<15}{'Capital Pendiente':<20}")

    for mes in range(1, n + 1):
        interes_mes = saldo_pendiente * i
        amortizacion = cuota - interes_mes
        saldo_pendiente -= amortizacion

        if mes == n:
            saldo_pendiente = 0

        print(f"{mes:<6}{cuota:<15.2f}{interes_mes:<12.2f}{amortizacion:<15.2f}{saldo_pendiente:<20.2f}")

def calculate_mortgage():
    print("=== Calculadora de Hipoteca ===")
    try:
        capital = float(input("Importe del préstamo (€): "))
        interes_anual = float(input("Tasa de interés anual (%): "))
        plazo_anios = int(input("Plazo de pago (años): "))

        cuota = calcular_cuota_mensual(capital, interes_anual, plazo_anios)
        print(f"\nCuota mensual: {cuota:.2f} €")
        generar_tabla_amortizacion(capital, interes_anual, plazo_anios)

    except ValueError:
        print("Por favor, introduce valores numéricos válidos.")

def menu():
    while True:
        print("\n=============MENU=================")
        print("\nSeleccione un ejercicio para ejecutar (1-7) o 0 para salir:")
        print("1. Numeros pares entre dos numeros")
        print("2. Contador de numeros")
        print("3. Adivina el numero")
        print("4. Numeros entre limites")
        print("5. Comprobador de numero primo")
        print("6. Lista de numeros primos")
        print("7. Calculadora de hipoteca")
        print("0. Salir")

        choice = input("Ingrese su elección: ")
        print('\n')

        if choice == '1':
            even_numbers()
        elif choice == '2':
            counter_numbers()
        elif choice == '3':
            guess_the_number()
        elif choice == '4':
            limit_numbers()
        elif choice == '5':
            prime_number()
        elif choice == '6':
            list_prime_numbers()
        elif choice == '7':
            calculate_mortgage()
        elif choice == '0':
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida, por favor intente de nuevo.")


menu()