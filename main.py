import sys
from colorama import Fore, Style
from game import jugar
from history import ver_historial

def menu():
    while True:
        print(Fore.CYAN + "\n========= MENÚ PRINCIPAL =========" + Style.RESET_ALL)
        print("1. Jugar partida")
        print("2. Ver historial")
        print("3. Salir")
        print("==================================")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            jugar()
        elif opcion == "2":
            ver_historial()
        elif opcion == "3":
            print("Saliendo del programa...")
            sys.exit()
        else:
            print(Fore.RED + "Opción inválida, intenta de nuevo." + Style.RESET_ALL)

menu()
