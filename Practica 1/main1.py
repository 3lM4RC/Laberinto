from functions import *

laberinto = crear_laberinto()

# Dimensiones del laberinto (ancho y alto)
ANCHO = calcular_ancho(laberinto)
ALTO = calcular_alto(laberinto)

pygame.init()
screen = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Maze")

reloj = pygame.time.Clock()

# Coordenadas iniciales del punto amarillo (entrada)
x = 4 * 40
y = 15 * 40
ex = 15 * 40
ey = 2 * 40

Start = (x, y)
End = (ex, ey)
game_over = False

'''Aqui e donde el juego comienza'''
while not game_over:
    screen.fill(BLANCO)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: ##Si presionamos la X o quitamos el juego:
            pygame.quit() #Abortamos el pygame
            sys.exit() #Sliamos del programa
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                if x - 40 >= 0 and laberinto[y // 40][x // 40 - 1] == 1:
                    x -= 40
            elif event.key == pygame.K_RIGHT:
                if x + 40 < ANCHO and laberinto[y // 40][x // 40 + 1] == 1:
                    x += 40
            elif event.key == pygame.K_UP:
                if y - 40 >= 0 and laberinto[y // 40 - 1][x // 40] == 1:
                    y -= 40
            elif event.key == pygame.K_DOWN:
                if y + 40 < ALTO and laberinto[y // 40 + 1][x // 40] == 1:
                    y += 40
    
    dibujar_laberinto(laberinto, screen, Start, End, x, y)
    reloj.tick(60)

    # Verificar si el cuadro amarillo llega al cuadro rojo
    if (x, y) == (ex, ey):
        game_over = True

print("¡Laberinto resuelto!")