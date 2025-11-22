"""
    Programa: Ejercicio_3.py
    Propósito: Este programa organiza números aleatorios en arrays de Numpy
    Autor: Javier Acedo Caballero
    Fecha: 22/11/2025
"""

import numpy as np

NUMBERS_QUANTITY = 20

def main():
    numbers = np.random.randint(100, size=NUMBERS_QUANTITY)

    print('Original: ',numbers)

    even = numbers[numbers % 2 == 0]
    odd = numbers[numbers % 2 != 0]

    numbers = np.concatenate([even, odd])

    print('Modificado: ',numbers)


if __name__ == '__main__':
    main()