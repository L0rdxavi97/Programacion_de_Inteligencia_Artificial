"""
    Programa: Ejercicio_5.py
    Propósito: Este programa crea una hoja de cálculo con números aleatorios
    Autor: Javier Acedo Caballero
    Fecha: 27/10/2025
"""
import random

ROWS = 4
COLUMNS = 5
MIN_LIMIT = 100
MAX_LIMIT = 999

def main():
    numbers = [[random.randint(MIN_LIMIT, MAX_LIMIT) for _ in range(COLUMNS)] for _ in range(ROWS)]
    sum_list_row = []
    sum_list_column = [0] * COLUMNS

    for row in numbers:
        for number in row:
            print(number, end='\t\t')

        sum_ = sum(row)
        sum_list_row.append(sum_)

        print('\t|\t\t',sum_,'\t\t|')

    print('_' * 70)

    for row in numbers:
        for n in range(COLUMNS):
            sum_list_column[n] += row[n]

    for i in sum_list_column:
        print(i, end='\t')

    print('\t|\t', end='')

    print('TOTAL: ',sum(sum_list_row)+sum(sum_list_column),'\t|')

if __name__ == '__main__':
    main()