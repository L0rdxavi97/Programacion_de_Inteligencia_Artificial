"""
    Programa: Ejercicio_4.py
    Propósito: Este programa desplaza números de una lista
    Autor: Javier Acedo Caballero
    Fecha: 27/10/2025
"""
NUMBERS_QUANTITY = 5


def main():
    numbers = []

    try:
        for i in range(NUMBERS_QUANTITY):
            numbers.append(int(input(f'Introduce numero {i+1}: ')))

    except ValueError:
        print('El numero ingresado no es valido')
        return

    print('Original: ',numbers)

    last_number = numbers[-1]

    for n in range(len(numbers)-1,0,-1):
        numbers[n] = numbers[n-1]

    numbers[0] = last_number

    print('Modificada: ',numbers)

if __name__ == '__main__':
    main()