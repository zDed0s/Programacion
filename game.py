import pygame
import sys
import matplotlib.pyplot as plt
from settings import *
from utils import mostrar_texto, guardar_partida

def jugar():

    ventana = pygame.display.set_mode((ANCHO, ALTO))
    pygame.display.set_caption("Pong Retro - Proyecto Final")
    clock = pygame.time.Clock()

    jugador1 = input("Nombre del jugador 1: ")
    jugador2 = input("Nombre del jugador 2: ")

    paleta_ancho = 15
    paleta_alto = 100
    paleta_vel = 9

    p1_x = 25
    p1_y = ALTO // 2 - paleta_alto // 2

    p2_x = ANCHO - 25 - paleta_ancho
    p2_y = ALTO // 2 - paleta_alto // 2

    pelota_x = ANCHO // 2
    pelota_y = ALTO // 2
    pelota_size = 20
    pelota_vel_x = 3
    pelota_vel_y = 3

    p1_score = 0
    p2_score = 0
    META = 25

    jugando = True

    while jugando:
        ventana.fill(NEGRO)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        teclas = pygame.key.get_pressed()

        if teclas[pygame.K_w] and p1_y > 0:
            p1_y -= paleta_vel
        if teclas[pygame.K_s] and p1_y < ALTO - paleta_alto:
            p1_y += paleta_vel

        if teclas[pygame.K_UP] and p2_y > 0:
            p2_y -= paleta_vel
        if teclas[pygame.K_DOWN] and p2_y < ALTO - paleta_alto:
            p2_y += paleta_vel

        pelota_x += pelota_vel_x
        pelota_y += pelota_vel_y

        if pelota_y <= 0 or pelota_y >= ALTO - pelota_size:
            pelota_vel_y *= -1

        if pelota_x <= p1_x + paleta_ancho and p1_y < pelota_y < p1_y + paleta_alto:
            pelota_vel_x *= -1

        if pelota_x + pelota_size >= p2_x and p2_y < pelota_y < p2_y + paleta_alto:
            pelota_vel_x *= -1

        if pelota_x <= 0:
            p2_score += 1
            pelota_x, pelota_y = ANCHO//2, ALTO//2
            pelota_vel_x *= -1

        if pelota_x >= ANCHO:
            p1_score += 1
            pelota_x, pelota_y = ANCHO//2, ALTO//2
            pelota_vel_x *= -1

        pygame.draw.rect(ventana, BLANCO, (p1_x, p1_y, paleta_ancho, paleta_alto))
        pygame.draw.rect(ventana, BLANCO, (p2_x, p2_y, paleta_ancho, paleta_alto))
        pygame.draw.rect(ventana, BLANCO, (pelota_x, pelota_y, pelota_size, pelota_size))

        marcador = f"{p1_score}   -   {p2_score}"
        mostrar_texto(ventana, marcador, fuente_grande, ANCHO//2 - fuente_grande.size(marcador)[0] // 2, 20)

        pygame.display.update()
        clock.tick(FPS)

        if p1_score == META or p2_score == META:
            jugando = False

    pygame.quit()

    guardar_partida(jugador1, jugador2, p1_score, p2_score)

    plt.bar([jugador1, jugador2], [p1_score, p2_score])
    plt.title("Puntaje Final de la Partida")
    plt.ylabel("Puntajes")
    plt.show()
