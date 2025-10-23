"""
    Programa: Ejercicio_1_mod_3.py
    Propósito: Este programa es una calculadora con funciones para diferentes propósitos, tercera modificación
    Autor: Javier Acedo Caballero
    Fecha: 23/10/2025
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
    print('1. Introducir números')
    print('2. Sumar')
    print('3. Restar')
    print('4. Multiplicar')
    print('5. Dividir')
    print('6. Salir')
    print('==========================================')
    return input("Selecciona una opción: ")

def main():
    number_1 = 0
    number_2 = 0
    numbers_entered = False

    while True:
        option=menu()

        if option == '1':
            try:
                number_1 = float(input("Ingresa primer número: "))
                number_2 = float(input("Ingresa segundo número: "))
                numbers_entered = True
            except ValueError:
                print("Número inválido. Inténtalo de nuevo.")
                numbers_entered = False
                continue

        elif option in ['2', '3', '4', '5']:
            if not numbers_entered:
                print("Debes introducir primero los números (opción 1).")
                continue

            if option == '2':
                print(f"Resultado: {plus(number_1, number_2)}")

            elif option == '3':
                print(f"Resultado: {subtract(number_1, number_2)}")

            elif option == '4':
                print(f"Resultado: {multiply(number_1, number_2)}")

            elif option == '5':
                print(f"Resultado: {divide(number_1, number_2)}")

        elif option == '6':
            print("Saliendo del programa...")
            break

        else:
            print("Opción inválida. Intenta de nuevo.")

if __name__ == '__main__':
    main()
