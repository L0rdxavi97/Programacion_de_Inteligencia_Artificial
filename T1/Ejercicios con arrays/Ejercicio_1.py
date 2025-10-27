"""
    Programa: Ejercicio_1.py
    Propósito: Este programa realiza calculos con números en listas
    Autor: Javier Acedo Caballero
    Fecha: 27/10/2025
"""
import random

NUMBERS_QUANTITY = 20


def main():
    number = [random.randint(1, 100) for _ in range(NUMBERS_QUANTITY)]
    square = [n ** 2 for n in number]
    cube = [n ** 3 for n in number]

    for n in range(len(number)):
        print(number[n],end='\t')
        print(square[n],end='\t')
        print(cube[n])

if __name__ == '__main__':
    main()