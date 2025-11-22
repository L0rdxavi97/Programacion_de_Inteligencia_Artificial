"""
    Programa: Ejercicio_6.py
    Propósito: Este programa es una modificación que crea una hoja de cálculo con números aleatorios usando arrays de Numpy
    Autor: Javier Acedo Caballero
    Fecha: 22/11/2025
"""

import numpy as np

ROWS = 4
COLUMNS = 5
MIN_LIMIT = 100
MAX_LIMIT = 999
NUMBERS_QUANTITY = 20


def main():

    numbers = np.random.randint(MIN_LIMIT,MAX_LIMIT,size=(ROWS,COLUMNS))

    col_sums = np.sum(numbers, axis=0)
    row_sums = np.sum(numbers, axis=1)

    for r in range(ROWS):
        print(numbers[r], "|", row_sums[r])

    print('-'*45)
    print(col_sums, "| TOTAL: ", np.sum(col_sums))

if __name__ == '__main__':
    main()