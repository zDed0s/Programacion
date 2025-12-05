import pygame

pygame.init()

ANCHO = 1360
ALTO = 768

BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)

FPS = 120

fuente_grande = pygame.font.SysFont("terminal", 80)
fuente_mediana = pygame.font.SysFont("terminal", 40)
fuente_chica = pygame.font.SysFont("terminal", 28)

ARCHIVO = "data/historial_pong.csv"
