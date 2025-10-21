"""
    Programa: Ejercicios_de_estructuras_secuenciales.py
    Propósito: Este programa es un conjunto de ejercicios de estructuras simples
    Autor: Javier Acedo Caballero
    Fecha: 16/10/2025
"""
SCORE_BLANK = 0
SCORE_WRONG = -1
SCORE_RIGHT = 5


def greeting():
    name = input("Ingrese su nombre: ")

    print(f"Hola {name}, encantado de conocerte!")


def calculate_hypotenuse():
    cathetus1 = float(input("Ingrese la longitud del primer cateto (cm): "))
    cathetus2 = float(input("Ingrese la longitud del segundo cateto (cm): "))

    hypotenuse = (cathetus1 ** 2 + cathetus2 ** 2) ** 0.5

    print(f"La longitud de la hipotenusa es: {hypotenuse:.2f} cm")


def calculate_time_by_minutes():
    minutes = int(input("Ingrese el tiempo en minutos: "))

    hours = minutes // 60
    remaining_minutes = minutes % 60

    print(f"Tiempo ingresado: {hours} horas y {remaining_minutes} minutos")


def reverse_number():
    number = int(input("Ingrese un número de dos cifras: "))

    part1 = number % 10
    part2 = number // 10

    print(f"El número invertido es: {part1}{part2}")


def calculate_arrive_time():
    hours = int(input("Ingrese la hora de salida (HH): "))
    minutes = int(input("Ingrese los minutos de salida (MM): "))
    seconds = int(input("Ingrese los segundos de salida (SS): "))
    travel_time = int(input("Ingrese el tiempo de viaje en segundos (T): "))

    total_seconds = hours * 3600 + minutes * 60 + seconds + travel_time
    arrival_hours = (total_seconds // 3600) % 24
    arrival_minutes = (total_seconds % 3600) // 60
    arrival_seconds = total_seconds % 60

    print(
        f"Hora de llegada a la ciudad B: {arrival_hours:02}:{arrival_minutes:02}:{arrival_seconds:02}")


def calculate_mark():
    right_questions = int(input("Cantidad de respuestas correctas: "))
    wrong_questions = int(input("Cantidad de respuestas incorrectas: "))
    blank_questions = int(input("Cantidad de respuestas en blanco: "))

    total_questions = right_questions + wrong_questions + blank_questions

    if right_questions < 0 or wrong_questions < 0 or blank_questions < 0 or total_questions <= 0 :
        print("No puede haber valores negativos y debe de haber al menos una pregunta")
    else:
        total_score = right_questions * SCORE_RIGHT + wrong_questions * SCORE_WRONG + blank_questions * SCORE_BLANK
        mark = float(total_score / float(total_questions * SCORE_RIGHT)) * 10

        print(f"\nPuntuación total: {total_score} de {total_questions * SCORE_RIGHT}")
        print(f"Nota final (normalizada de 0 a 10): {mark:.2f}")


def main():
    while True:
        print("\n=============MENU=================")
        print("\nSeleccione un ejercicio para ejecutar (1-6) o 0 para salir:")
        print("1. Saludo personalizado")
        print("2. Calcular hipotenusa")
        print("3. Convertir minutos a horas y minutos")
        print("4. Invertir número de dos cifras")
        print("5. Calcular hora de llegada")
        print("6. Calcular nota de examen")
        print("0. Salir")

        choice = input("Ingrese su elección: ")
        print('\n')

        if choice == '1':
            greeting()
        elif choice == '2':
            calculate_hypotenuse()
        elif choice == '3':
            calculate_time_by_minutes()
        elif choice == '4':
            reverse_number()
        elif choice == '5':
            calculate_arrive_time()
        elif choice == '6':
            calculate_mark()
        elif choice == '0':
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida, por favor intente de nuevo.")

if __name__ == '__main__':
    main()

