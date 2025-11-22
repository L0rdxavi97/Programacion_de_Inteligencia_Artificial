"""
    Programa: Ejercicio_2.py
    Propósito: Este programa es una modificación usando Numpy para realizar calculos con números en arrays
    Autor: Javier Acedo Caballero
    Fecha: 22/11/2025
"""

from numpy import random

NUMBERS_QUANTITY = 20

def main():
    numbers = random.randint(100, size=NUMBERS_QUANTITY)
    square,cube = numbers ** 2, numbers ** 3

    for n in range(NUMBERS_QUANTITY):
        print(f"{numbers[n]}\t\t{square[n]}\t\t{cube[n]}")

if __name__ == '__main__':
    main()