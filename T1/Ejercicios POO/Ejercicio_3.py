"""
    Programa: Ejercicio_3.py
    Propósito: Este programa manipula fechas a través de una clase
    Autor: Javier Acedo Caballero
    Fecha: 04/11/2025
"""

DAYS_LIST = [31,28,31,30,31,30,31,31,30,31,30,31]

class Date:
    def __init__(self, day, month, year):
        self.__year = year
        self.__month = month
        self.__day = day

    @property
    def day(self):
        return self.__day

    @property
    def month(self):
        return self.__month

    @property
    def year(self):
        return self.__year

def main():
    pass

if __name__ == '__main__':
    main()