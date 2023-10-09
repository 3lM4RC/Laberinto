import random
import pygame
import sys


#Definimos los colores
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
VERDE = (0, 255, 0)
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)
GRIS = (128, 128, 128)

size = (800, 500)

pygame.init()
#creamos una ventana
screen = pygame.display.set_mode(size)
game_over = False
clock = pygame.time.Clock()

coord_list = []
for i in range(60):
        x = random.randint(0,800)
        y = random.randint(0,500)
        coord_list.append([x,y])

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    #Color del fondo
    screen.fill(BLANCO)

    #ZONA DE JUEGOS
    for coord in coord_list:
        x = coord[0]
        y = coord[1]
        pygame.draw.circle(screen, NEGRO, coord, 2)
        coord[1] += 1
        if coord[1] > 500:
             coord[1] = 0

    #FIN DE LA ZONA DE JUEGOS
    #Actualizar pantalla
    pygame.display.flip()
    clock.tick(30)