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

pygame.mouse.set_visible(0)

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    #Color del fondo
    mouse_pos = pygame.mouse.get_pos()
    x = mouse_pos[0]
    y = mouse_pos[1]
    screen.fill(BLANCO)

    #ZONA DE JUEGOS
    
    pygame.draw.rect(screen,ROJO,(x,y,100,100))

    #FIN DE LA ZONA DE JUEGOS
    #Actualizar pantalla
    pygame.display.flip()
    clock.tick(60)