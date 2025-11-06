"""
    Programa: Ejercicio_2.py
    Propósito: Este programa manipula fracciones a través de una clase
    Autor: Javier Acedo Caballero
    Fecha: 04/11/2025
"""

from math import gcd

class Fraction:
    def __init__(self, numerator, denominator=1):
        if isinstance(numerator, float):
            s = str(numerator)
            if '.' in s:
                decimals = len(s.split('.')[1])
                factor = 10 ** decimals
                numerator = int(round(numerator * factor))
                denominator = factor
        if isinstance(denominator, float):
            s = str(denominator)
            if '.' in s:
                decimals = len(s.split('.')[1])
                factor = 10 ** decimals
                denominator = int(round(denominator * factor))
        if denominator == 0:
            raise ValueError("El denominador no puede ser cero.")
        if denominator < 0:
            numerator, denominator = -numerator, -denominator
        common = gcd(numerator, denominator)
        self.__numerator = numerator // common
        self.__denominator = denominator // common

    @property
    def numerator(self):
        return self.__numerator

    @property
    def denominator(self):
        return self.__denominator

    def __repr__(self):
        return f"{self.numerator}/{self.denominator}"

    def __add__(self, other):
        if isinstance(other, (int, float)):
            other = Fraction(other)
        num = self.numerator * other.denominator + other.numerator * self.denominator
        den = self.denominator * other.denominator
        return Fraction(num, den)

    __radd__ = __add__

    def __sub__(self, other):
        if isinstance(other, (int, float)):
            other = Fraction(other)
        num = self.numerator * other.denominator - other.numerator * self.denominator
        den = self.denominator * other.denominator
        return Fraction(num, den)

    def __rsub__(self, other):
        return Fraction(other) - self

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            other = Fraction(other)
        num = self.numerator * other.numerator
        den = self.denominator * other.denominator
        return Fraction(num, den)

    __rmul__ = __mul__

    def __truediv__(self, other):
        if isinstance(other, (int, float)):
            other = Fraction(other)
        if other.numerator == 0:
            raise ZeroDivisionError("No se puede dividir entre cero.")
        num = self.numerator * other.denominator
        den = self.denominator * other.numerator
        return Fraction(num, den)

    def __rtruediv__(self, other):
        return Fraction(other) / self

    def __eq__(self, other):
        if isinstance(other, (int, float)):
            other = Fraction(other)
        return self.numerator * other.denominator == other.numerator * self.denominator

    def __lt__(self, other):
        if isinstance(other, (int, float)):
            other = Fraction(other)
        return self.numerator * other.denominator < other.numerator * self.denominator

    def __le__(self, other):
        return self < other or self == other

    def __gt__(self, other):
        return not self <= other

    def __ge__(self, other):
        return not self < other

    def __ne__(self, other):
        return not self == other

    def __float__(self):
        return self.numerator / self.denominator


def main():
    print("=== PRUEBAS DE LA CLASE FRACTION ===\n")

    f1 = Fraction(2, 3)
    f2 = Fraction(3, 4)
    f3 = Fraction(1, 2)
    f4 = Fraction(2, 4)

    print("Fracciones creadas:")
    print(f"f1 = {f1}")
    print(f"f2 = {f2}")
    print(f"f3 = {f3}")
    print(f"f4 = {f4}\n")

    print("Operaciones entre fracciones:")
    print(f"{f1} + {f2} = {f1 + f2}")
    print(f"{f3} + {f4} = {f3 + f4}")
    print(f"{f1} - {f2} = {f1 - f2}")
    print(f"{f1} * {f2} = {f1 * f2}")
    print(f"{f1} / {f2} = {f1 / f2}\n")

    print("Operaciones con enteros y flotantes:")
    print(f"{f1} + 1 = {f1 + 1}")
    print(f"5 * {f2} = {5 * f2}")
    print(f"{f3} / 2 = {f3 / 2}")
    print(f"1 / {f3} = {1 / f3}\n")

    print("Comparaciones:")
    print(f"{f3} == {f4} → {f3 == f4}")  # 1/2 == 2/4
    print(f"{f1} < {f2} → {f1 < f2}")
    print(f"{f2} > {f1} → {f2 > f1}")
    print(f"{f1} <= {f3} → {f1 <= f3}")
    print(f"{f3} >= {f4} → {f3 >= f4}")
    print(f"{f1} != {f2} → {f1 != f2}\n")

    print("Comparaciones con enteros:")
    print(f"1 < {f3} → {1 < f3}")
    print(f"{f3} < 1 → {f3 < 1}")
    print(f"{f3} == 0.5 → {f3 == 0.5}")

if __name__ == '__main__':
    main()
