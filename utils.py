import pygame
import pandas as pd
import os
from settings import BLANCO, ARCHIVO

def mostrar_texto(ventana, texto, fuente, x, y):
    imagen = fuente.render(texto, True, BLANCO)
    ventana.blit(imagen, (x, y))

def guardar_partida(j1, j2, s1, s2):
    datos_nuevos = pd.DataFrame({
        "Jugador1": [j1],
        "Jugador2": [j2],
        "Puntaje1": [s1],
        "Puntaje2": [s2]
    })

    if os.path.exists(ARCHIVO):
        datos_viejos = pd.read_csv(ARCHIVO)
        datos_finales = pd.concat([datos_viejos, datos_nuevos], ignore_index=True)
        datos_finales.to_csv(ARCHIVO, index=False)
    else:
        datos_nuevos.to_csv(ARCHIVO, index=False)
