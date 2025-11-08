"""
    Programa: Ejercicio_1.py
    Propósito: Este programa manipula duraciones a través de una clase inmutable
    Autor: Javier Acedo Caballero
    Fecha: 04/11/2025
"""


class Duration:
    def __init__(self, hour=0, minute=0, second=0):
        self.__hour, self.__minute, self.__second = hour, minute, second
        self.__normalize()

    def __normalize(self):
        # Calculamos el total de segundos que son
        total_seconds = self.total_seconds()

        # Normalizamos la duración introducida y la guardamos
        self.__hour = total_seconds // 3600
        remaining = total_seconds % 3600
        self.__minute = remaining // 60
        self.__second = remaining % 60

    @property
    def hour(self):
        return self.__hour

    @property
    def minute(self):
        return self.__minute

    @property
    def second(self):
        return self.__second

    def total_seconds(self):
        return self.__hour * 3600 + self.__minute * 60 + self.__second

    def __str__(self):
        return f"{self.__hour}h {self.__minute}m {self.__second}s"

    def __eq__(self, other):
        return self.total_seconds() == other.total_seconds()

    def __ne__(self, other):
        return not self == other

    def __gt__(self, other):
        return self.total_seconds() > other.total_seconds()

    def __ge__(self, other):
        return self.total_seconds() >= other.total_seconds()

    def __lt__(self, other):
        return not self >= other

    def __le__(self, other):
        return not self > other

    def __add__(self, other):
        if isinstance(other, Duration):
            return Duration(self.__hour + other.__hour, self.__minute + other.__minute, self.__second + other.__second)
        else:
            return Duration(self.__hour, self.__minute, self.__second + other)

    def __sub__(self, other):
        if isinstance(other, Duration):
            return Duration(self.__hour - other.__hour, self.__minute - other.__minute, self.__second - other.__second)
        else:
            return Duration(self.__hour, self.__minute, self.__second - other)


def main():
    print("=== DEMOSTRACIÓN DE LA CLASE Duration ===\n")

    d1 = Duration(1, 20, 30)
    d2 = Duration(0, 45, 70)
    d3 = Duration(2, 15, 10)

    print(f"d1 = {d1}")
    print(f"d2 = {d2}")
    print(f"d3 = {d3}\n")

    print("=== COMPARACIONES ===")
    print(f"d1 == d2 → {d1 == d2}")
    print(f"d1 > d2  → {d1 > d2}")
    print(f"d1 < d3  → {d1 < d3}")
    print(f"d3 >= d1 → {d3 >= d1}")
    print(f"d2 <= d3 → {d2 <= d3}\n")

    print("=== OPERACIONES ARITMÉTICAS ===")

    sum_ = d1 + d2
    sub_ = d3 - d1

    print(f"{d1} + {d2} = {sum_}")
    print(f"{d3} - {d1} = {sub_}")
    print(f"{d1} + 500s = {d1 + 500}")
    print(f"{d2} - 100s = {d2 - 100}\n")

    print("=== CASO DE ERROR ===")

    result = d2 - d3

    print(f"{d2} - {d3} = {result}")


if __name__ == '__main__':
    main()
