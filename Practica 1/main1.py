from functions import *

#Creamos el laberinto
laberinto = crear_laberinto()

# Dimensiones del laberinto (ancho y alto)
ANCHO, ALTO = calcular_alto_ancho()

#Iniciamos el pygame
pygame.init()
screen = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Maze")
reloj = pygame.time.Clock()

# Coordenadas iniciales del jugador, y coordenadas finales
x = calcular_posicion(4, 40)
y = calcular_posicion(15, 60)
ex = calcular_posicion(15,40)
ey = calcular_posicion(2,60)

#Tuplas para indicar el inicio y el final
Start = (x, y)
End = (ex, ey)

game_over = False

# Cuadro de texto para mostrar las coordenadas
fuente = pygame.font.Font("C:/Windows/Fonts/arial.ttf", 24)
texto_coordenadas = ""

'''Aqui es donde podemos pintar el laberinto
while ejecutando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ejecutando = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Clic izquierdo (pintar gris)
                pintar_cuadrado(laberinto, *event.pos)
            elif event.button == 3:  # Clic derecho (restaurar a negro)
                restaurar_cuadrado(laberinto, *event.pos)

    # Mostrar las coordenadas del mouse en la consola
    x, y = pygame.mouse.get_pos()
    fila = y // int(alto_cuadrado + separacion)
    columna = x // int(ancho_cuadrado + separacion)
    if fila < 15 and columna < 15:
        texto_coordenadas = f"Coordenadas del mouse: Fila {fila}, Columna {columna}"

    # Actualizar la screen
    screen.fill(FONDO)
    for fila in range(15):
        for columna in range(15):
            color = BLANCO if laberinto[fila][columna] else NEGRO
            x = (columna * (ancho_cuadrado + separacion)) + separacion
            y = (fila * (alto_cuadrado + separacion)) + separacion
            pygame.draw.rect(screen, color, (x, y, ancho_cuadrado, alto_cuadrado))

    actualizar_cuadro_texto(texto_coordenadas,screen,ALTO)
    pygame.display.flip()'''

'''Aqui e donde el juego comienza'''
while not game_over:
    screen.fill(BLANCO)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: ##Si presionamos la X o quitamos el juego:
            pygame.quit() #Abortamos el pygame
            sys.exit() #Sliamos del programa
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                if x - 60 >= 0 and laberinto[y // 40][x // 60 - 1] == 1:
                    x -= 60
            elif event.key == pygame.K_RIGHT:
                if x + 60 < ANCHO and laberinto[y // 40][x // 60 + 1] == 1:
                    x += 60
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
        time.sleep(1)
        game_over = True

print("¡Laberinto resuelto!")