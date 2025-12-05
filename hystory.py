import pandas as pd
import os
from colorama import Fore, Style
import matplotlib.pyplot as plt
from settings import ARCHIVO

def ver_historial():
    print(Fore.CYAN + "\n--- HISTORIAL DE PARTIDAS ---" + Style.RESET_ALL)

    if not os.path.exists(ARCHIVO):
        print(Fore.RED + "Todavía no hay partidas guardadas.\n" + Style.RESET_ALL)
        return

    df = pd.read_csv(ARCHIVO)
    print(df)

    plt.figure(figsize=(9,5))
    plt.title("Historial de Puntajes - Pong Retro")
    plt.plot(df.index, df["Puntaje1"], marker="o", label="Jugador 1")
    plt.plot(df.index, df["Puntaje2"], marker="o", label="Jugador 2")
    plt.xlabel("Número de partida")
    plt.ylabel("Puntajes")
    plt.legend()
    plt.grid(True)
    plt.show()
