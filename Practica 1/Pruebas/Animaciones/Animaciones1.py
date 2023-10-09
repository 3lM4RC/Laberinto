import pygame
import sys

pygame.init()

#Definimos los colores
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
VERDE = (0, 255, 0)
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)
GRIS = (128, 128, 128)

size = (800, 500)

#creamos una ventana
screen = pygame.display.set_mode(size)
game_over = False
clock = pygame.time.Clock()

#coordenadas dle cuadrado
coord_x = 400
coord_y = 200

#velocidad
speed_x = 3
speed_y = 3



while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    
    if (coord_x > 720 or coord_x < 0):
        speed_x *= -1
    if (coord_y > 420 or coord_y < 0):
        speed_y *= -1

    coord_x += speed_x
    coord_y += speed_y
    #Color del fondo
    screen.fill(BLANCO)
    #ZONA DE JUEGOS

    pygame.draw.rect(screen, VERDE, (coord_x, coord_y, 80, 80))

    #FIN DE LA ZONA DE JUEGOS
    #Actualizar pantalla
    pygame.display.flip()
    clock.tick(120)