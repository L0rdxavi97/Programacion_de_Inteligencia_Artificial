"""
    Programa: Estructuras_alternativas.py
    Propósito: Este programa es un conjunto de ejercicios de estructuras alternativas
    Autor: Javier Acedo Caballero
    Fecha: 19/10/2025
"""


def comparate_ages():
    try:
        age1 = int(input("Introduce la edad de la primera persona: "))
        age2 = int(input("Introduce la edad de la segunda persona: "))
    except ValueError:
        print("El valor de edad es invalido")
        return

    if age1 <= 0 or age2 <= 0:
        print("La edad debe ser mayor a 0")
        return

    if age1 > age2:
        print("La primera persona es mayor")
    elif age1 < age2:
        print("La segunda persona es mayor")
    else:
        print("Las personas tienen la misma edad")


def determine_triangle_type():
    try:
        a = int(input("Introduce longitud de primer lado del triángulo: "))
        b = int(input("Introduce longitud de segundo lado del triángulo: "))
        c = int(input("Introduce longitud de tercer lado del triángulo: "))

    except ValueError:
        print("El valor del lado del triángulo es invalido")
        return

    if a == b == c:
        print("El triángulo es equilátero")
    elif a == b or a == c or b == c:
        print("El triángulo es isósceles")
    else:
        print("El triángulo es escaleno")


def determine_leap_year():
    try:
        year = int(input("Introduce un año: "))

    except ValueError:
        print("El valor del año es invalido")
        return

    if year <= 0:
        print("El año debe ser mayor a 0")
        return

    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(f"El año {year} es bisiesto")
    else:
        print(f"El año {year} no es bisiesto")


def calculate_money_change():
    try:
        money = int(input("Introduce la cantidad en euros: "))

    except ValueError:
        print("La cantidad de euros es invalido")
        return

    value = 500

    while money > 0:
        if value > 2:
            type_ = "billete"
        else:
            type_ = "moneda"

        if money >= value:
            quantity = money // value
            money = money % value
            print(f"{quantity} {type_}(s) de {value}€")

        if value == 500:
            value = 200
        elif value == 200:
            value = 100
        elif value == 100:
            value = 50
        elif value == 50:
            value = 20
        elif value == 20:
            value = 10
        elif value == 10:
            value = 5
        elif value == 5:
            value = 2
        elif value == 2:
            value = 1
        else:
            break


def print_week_day():
    try:
        day = int(input("Introduce un número del 1 al 7: "))

    except ValueError:
        print("El valor es invalido")
        return

    if day == 1:
        print("Lunes")
    elif day == 2:
        print("Martes")
    elif day == 3:
        print("Miércoles")
    elif day == 4:
        print("Jueves")
    elif day == 5:
        print("Viernes")
    elif day == 6:
        print("Sábado")
    elif day == 7:
        print("Domingo")
    else:
        print("Número inválido, por favor ingrese un número del 1 al 7")

def greater_number_at_three():
    try:
        number1 = int(input("Introduce el primer número: "))
        number2 = int(input("Introduce el segundo número: "))
        number3 = int(input("Introduce el tercer número: "))

    except ValueError:
        print("El número es invalido")
        return

    if number1 >= number2 and number1 >= number3:
        greater = number1
    elif number2 >= number1 and number2 >= number3:
        greater = number2
    else:
        greater = number3

    print("El número greater es:", greater)


def greater_number_at_five():
    try:
        number1 = int(input("Introduce el primer número: "))
        number2 = int(input("Introduce el segundo número: "))
        number3 = int(input("Introduce el tercer número: "))
        number4 = int(input("Introduce el cuarto número: "))
        number5 = int(input("Introduce el quinto número: "))

    except ValueError:
        print("El número es invalido")
        return

    greater = number1

    if number2 > greater:
        greater = number2
    if number3 > greater:
        greater = number3
    if number4 > greater:
        greater = number4
    if number5 > greater:
        greater = number5

    print("El número mayor es:", greater)


def print_mark():
    try:
        mark = float(input("Introduce nota: "))

    except ValueError:
        print("El nota es invalida")
        return

    print("Tu calificación es ",end="")

    if mark < 0 or mark > 10:
        print("...\nLa nota debe estar entre 0 y 10")
    elif mark < 5:
        print("SUSPENSO")
    elif mark < 7:
        print("APROBADO")
    elif mark < 9:
        print("NOTABLE")
    elif mark < 10:
        print("SOBRESALIENTE")
    else:
        print("MATRICULA DE HONOR")


def menu():
    while True:
        print("\n=============MENU=================")
        print("\nSeleccione un ejercicio para ejecutar (1-8) o 0 para salir")
        print("1. Comparar edades")
        print("2. Determinar tipo de triangulo")
        print("3. Determinar si el año es bisiesto")
        print("4. Calcular cambio")
        print("5. Imprimir dia de la semana")
        print("6. Numero mas grande de tres")
        print("7. Numero mas grande de cinco")
        print("8. Imprimir la calificación de la nota")
        print("0. Salir")

        try:
            choice = input("Ingrese su elección: ")

        except ValueError:
            print("La opción es invalida")
            return

        print('\n')

        if choice == '1':
            comparate_ages()
        elif choice == '2':
            determine_triangle_type()
        elif choice == '3':
            determine_leap_year()
        elif choice == '4':
            calculate_money_change()
        elif choice == '5':
            print_week_day()
        elif choice == '6':
            greater_number_at_three()
        elif choice == '7':
            greater_number_at_five()
        elif choice == '8':
            print_mark()
        elif choice == '0':
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida, por favor intente de nuevo.")


if __name__ == "__main__":
    menu()
