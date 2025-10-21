# Programa: Estructuras_alternativas.py
# Propósito: Este programa es un conjunto de ejercicios de estructuras alternativas
# Autor: Javier Acedo Caballero
# Fecha: 19/10/2025


def comparate_ages():
    age1 = int(input("Introduce la edad de la primera persona: "))
    age2 = int(input("Introduce la edad de la segunda persona: "))
    if age1 > age2:
        print("La primera persona es mayor")
    elif age1 < age2:
        print("La segunda persona es mayor")
    else:
        print("Las personas tienen la misma edad")


def determine_triangle_type():
    a = int(input("Introduce longitud de primer lado del triángulo: "))
    b = int(input("Introduce longitud de segundo lado del triángulo: "))
    c = int(input("Introduce longitud de tercer lado del triángulo: "))

    if a == b == c:
        print("El triángulo es equilátero")
    elif a == b or a == c or b == c:
        print("El triángulo es isósceles")
    else:
        print("El triángulo es escaleno")


def determine_leap_year():
    year = int(input("Introduce un año: "))
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(f"El año {year} es bisiesto")
    else:
        print(f"El año {year} no es bisiesto")


def calculate_money_change():
    pass


def print_week_day():
    day = int(input("Introduce un número del 1 al 7: "))
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

def greatter_number_at_three():
    print("Introduce solo numeros enteros")
    numbers = []
    for i in range(1, 4):
        numbers.append(int(input(f"introduce numero {i}: ")))
    numbers.sort()
    print(numbers[-1])

def greatter_number_at_five():
    print("Introduce solo numeros enteros")
    numbers = []
    for i in range(1, 6):
        numbers.append(int(input(f"introduce numero {i}: ")))
    numbers.sort()
    print(numbers[-1])

def print_mark():
    mark = float(input("Introduce nota: "))
    print("Tu calificación es ",end="")
    if mark < 0 or mark > 10:
        print("La nota debe ser mayor a 0 y menor a 10")
    elif mark < 5:
        print("SUSPENSO")
    elif mark>= 5 and mark < 7:
        print("APROBADO")
    elif mark>= 7 and mark < 9:
        print("NOTABLE")
    elif mark>= 9 and mark < 10:
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
        print("8. Imprimir la calificacion de la nota")
        print("0. Salir")

        choice = input("Ingrese su elección: ")
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
            greatter_number_at_three()
        elif choice == '7':
            greatter_number_at_five()
        elif choice == '8':
            print_mark()
        elif choice == '0':
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida, por favor intente de nuevo.")

menu()