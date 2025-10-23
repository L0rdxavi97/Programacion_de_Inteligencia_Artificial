"""
    Programa: Ejercicio_1.py
    Propósito: Este programa es una calculadora con funciones para diferentes propósitos
    Autor: Javier Acedo Caballero
    Fecha: 22/10/2025
"""

def plus(number_1, number_2):
    return number_1 + number_2

def subtract(number_1, number_2):
    return number_1 - number_2

def multiply(number_1, number_2):
    return number_1 * number_2

def divide(number_1, number_2):
    if number_2 == 0:
        return "Error: División por cero no permitida."
    return number_1 / number_2

def menu():
    print('================ MENU ====================')
    print('1. Sumar')
    print('2. Restar')
    print('3. Multiplicar')
    print('4. Dividir')
    print('5. Salir')
    print('==========================================')


def main():
    try:
        number_1 = float(input("Ingresa primer numero: "))
        number_2 = float(input("Ingresa segundo numero: "))
    except ValueError:
        print("Numero invalido")
        return

    while True:
        menu()

        option = input("Ingresa una opción: ")

        if option == '1':
            print("Resultado:", plus(number_1, number_2))
        elif option == '2':
            print("Resultado:", subtract(number_1, number_2))
        elif option == '3':
            print("Resultado:", multiply(number_1, number_2))
        elif option == '4':
            print("Resultado:", divide(number_1, number_2))
        elif option == '5':
            print("Saliendo...")
            break
        else:
            print("Opción invalida")


if __name__ == '__main__':
    main()