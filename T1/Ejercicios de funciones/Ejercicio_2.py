"""
    Programa: Ejercicio_2.py
    Propósito: Este programa es una biblioteca de funciones
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

def reverse(number):
    rev = 0

    while number > 0:
        rev = rev * 10 + number % 10
        number //= 10

    return rev

def is_palindromic(number):
    return number == reverse(number)

def is_prime(number):
    if number < 2:
        return False

    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False

    return True

def next_prime(number):
    number += 1

    while not is_prime(number):
        number += 1

    return number

def digit_n(number, position):
    num_digits = digits(number)

    for _ in range(num_digits - position - 1):
        number //= 10

    return number % 10

def digit_position(number, digit):
    num_digits = digits(number)

    for i in range(num_digits):
        if digit_n(number, i) == digit:
            return i

    return -1

def remove_behind(number, quantity):
    return number // (10 ** quantity)

def remove_ahead(number, quantity):
    num_digits = digits(number)

    return number % (10 ** (num_digits - quantity))

def paste_behind(number, digit):
    return number * 10 + digit

def paste_ahead(number, digit):
    return digit * (10 ** digits(number)) + number

def piece_of_number(number, initial_position, ending_position):
    num_digits = digits(number)
    number = remove_ahead(number, initial_position)
    number = remove_behind(number, num_digits - ending_position - 1)

    return number

def concatenate(number1, number2):
    return number1 * (10 ** digits(number2)) + number2

def main():
    print("=== PRUEBAS DE LA BIBLIOTECA NUMÉRICA ===")
    print("reverse(12345) =", reverse(12345))
    print("is_palindromic(12321) =", is_palindromic(12321))
    print("is_prime(7) =", is_prime(7))
    print("next_prime(14) =", next_prime(14))
    print("digits(98765) =", digits(98765))
    print("digit_n(98765, 0) =", digit_n(98765, 0))
    print("digit_position(98765, 6) =", digit_position(98765, 6))
    print("remove_behind(98765, 2) =", remove_behind(98765, 2))
    print("remove_ahead(98765, 2) =", remove_ahead(98765, 2))
    print("paste_behind(987, 5) =", paste_behind(987, 5))
    print("paste_ahead(987, 5) =", paste_ahead(987, 5))
    print("piece_of_number(987654321, 2, 5) =", piece_of_number(987654321, 2, 5))
    print("concatenate(123, 456) =", concatenate(123, 456))

if __name__ == '__main__':
    main()
