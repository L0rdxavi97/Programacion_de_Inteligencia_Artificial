"""
    Programa: Ejercicio_3.py
    Propósito: Este programa es un conversor de numero a sistema de palotes
    Autor: Javier Acedo Caballero
    Fecha: 23/10/2025
"""

def digits(number):
    if number == 0:
        return 1

    count = 0

    while number > 0:
        count += 1
        number //= 10

    return count

def conversor(number):
    digits_ = digits(number)
    text=''

    for n in range(digits_):
        for m in range(number[n]):
            text += '|'
        if n != digits_ - 1:
            text += '-'

    return text

def main():
    try:
        number = int(input('Ingresa un numero a convertir: '))
    except ValueError:
        print('El numero ingresado no es valido')
        return

    print('El resultado es:', conversor(number))


if __name__ == '__main__':
    main()