"""
    Programa: Estructuras_repetitivas.py
    Propósito: Este programa es un conjunto de ejercicios de estructuras repetitivas
    Autor: Javier Acedo Caballero
    Fecha: 19/10/2025
"""
import random


def even_numbers():
    try:
        number1 = int(input("Introduce el primer numero: "))
        number2 = int(input("Introduce el segundo numero: "))
    except ValueError:
        print("El numero no es valido")
        return

    difference = number2 - number1
    counter = 0

    if difference > 1:
        for i in range(1, difference):
            val = number1 + i
            if val % 2 == 0:
                counter += 1
                print(f"Numero {counter}: {val}")


        if counter == 0:
            print("No hay números para imprimir")

    elif difference < 0:
        print("El primer numero debe de ser menor al segundo numero")
    else:
        print("No hay números para imprimir")


def counter_numbers():
    counter_zero = 0
    counter_greater_zero = 0
    counter_lesser_zero = 0

    try:
        amount = int(input("Introduce el cantidad de números a introducir: "))
    except ValueError:
        print("El numero no es valido")
        return

    for i in range(amount):
        if i == 0:
            counter_zero += 1
        elif i > 0:
            counter_greater_zero += 1
        else:
            counter_lesser_zero += 1

    print("La cantidad de números es: ", amount)
    print("La cantidad de números mayores a cero es: ", counter_greater_zero)
    print("La cantidad de números menores a cero es: ", counter_lesser_zero)
    print("La cantidad de ceros es: ", counter_zero)


def guess_the_number():
    random_number = random.randint(1, 100)
    winner = False

    print("Tienes 10 intentos para adivinar el numero")

    for i in range(10):
        print(f"Intento {i+1}")
        try:
            intent = int(input("Introduce un numero: "))
        except ValueError:
            print("El numero no es valido")
            return
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
    lower_limit = 0
    top_limit = 0

    while not correct_limit:
        try:
            lower_limit = int(input("Introduce limite inferior: "))
            top_limit = int(input("Introduce limite superior: "))
        except ValueError:
            print("El limite no es valido")
            return
        if lower_limit > top_limit:
            print("el limite inferior no puede ser mas grande que el superior")
        else:
            correct_limit = True

    sum_numbers_limit = 0
    counter_over_limit = 0
    right_at_limit = False

    while True:
        try:
            number = int(input("Introduce un numero: "))
        except ValueError:
            print("El numero no es valido")
            return

        if number == 0:
            break
        elif number < lower_limit or number > top_limit:
            counter_over_limit += 1
        elif number == lower_limit or number == top_limit:
            right_at_limit = True
        else:
            sum_numbers_limit += number

    print("La suma de los números que están dentro del intervalo es: ", sum_numbers_limit)
    print("Cantidad de números fuera de los limites: ", counter_over_limit)
    print("Número justo en los límites?: ", "Sí" if right_at_limit else "No")


def is_prime(number):
    if number < 2:
        return False
    elif number == 2:
        return True
    else:
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

    try:
        n = int(input("Introduce cantidad de números: "))
    except ValueError:
        print("El numero no es valido")
        return

    if n<=0 :
        print("El numero no es valido, debe de ser mayor a 0")
        return

    while counter < n:
        if is_prime(number):
            print(f"{counter}: {number}")
            counter += 1
        number += 1


def calculate_monthly_fee(capital, annual_interest, term_years):
    n = term_years * 12
    i = annual_interest / 100 / 12

    if i == 0:
        fee = capital / n
    else:
        fee = capital * (i * (1 + i) ** n) / ((1 + i) ** n - 1)

    return fee

def generate_amortization_table(capital, annual_interest, term_years, fee):
    outstanding_balance = capital
    i = annual_interest / 100 / 12
    n = term_years * 12

    print("\nTabla de Amortización:")
    print(f"{'Cuota':<6}{'Cuota Mensual':<15}{'Interés':<12}{'Amortización':<15}{'Capital Pendiente':<20}")

    for month in range(1, n + 1):
        interest_month = outstanding_balance * i
        amortization = fee - interest_month
        outstanding_balance -= amortization

        if month == n:
            outstanding_balance = 0

        print(f"{month:<6}{fee:<15.2f}{interest_month:<12.2f}{amortization:<15.2f}{outstanding_balance:<20.2f}")

def calculate_mortgage():
    print("=== Calculadora de Hipoteca ===")

    try:
        capital = float(input("Importe del préstamo (€): "))
        annual_interest = float(input("Tasa de interés anual (%): "))
        term_years = int(input("Plazo de pago (años): "))
    except ValueError:
        print("Debes de introducir un numero valido")
        return

    fee = calculate_monthly_fee(capital, annual_interest, term_years)

    print(f"\nCuota mensual: {fee:.2f} €")

    generate_amortization_table(capital, annual_interest, term_years, fee)


def menu():
    while True:
        print("\n=============MENU=================")
        print("\nSeleccione un ejercicio para ejecutar (1-7) o 0 para salir:")
        print("1. Números pares entre dos números")
        print("2. Contador de números")
        print("3. Adivina el numero")
        print("4. Números entre limites")
        print("5. Comprobador de numero primo")
        print("6. Lista de números primos")
        print("7. Calculadora de hipoteca")
        print("0. Salir")

        try:
            choice = input("Ingrese su elección: ")
        except ValueError:
            print("Debes de introducir un numero valido")
            return

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


if __name__ == '__main__':
    menu()
