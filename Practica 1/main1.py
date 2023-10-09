from functions import *

'''laberinto = [
    [0,0,0,0,0,0,0,0,1,0,0,0,0,0,0],
    [0,1,1,1,1,0,1,1,1,1,1,1,1,1,1],
    [0,1,0,1,0,0,1,0,1,0,0,0,0,0,0],
    [0,0,1,1,1,1,1,0,1,0,0,0,0,0,0],
    [0,0,0,1,0,1,0,0,1,0,0,0,0,0,0],
    [0,0,0,1,0,0,0,0,1,0,0,0,0,0,0],
    [0,1,1,1,1,1,1,0,1,0,0,0,0,0,0],
    [0,1,0,1,0,0,0,0,0,0,0,0,0,0,0],
    [0,1,0,1,1,1,1,1,1,0,0,0,0,0,0],
    [1,1,0,1,0,0,0,1,0,0,0,0,0,0,0],
    [0,0,0,1,0,0,0,1,0,0,0,0,0,0,0],
    [0,0,0,1,0,0,0,1,0,0,0,0,0,0,0],
    [0,0,0,1,0,0,0,1,0,0,0,0,0,0,0],
    [0,0,0,1,0,0,0,1,0,0,0,0,0,0,0],
    [0,0,0,1,0,0,0,1,0,0,0,0,0,0,0]
]'''
laberinto = []
direccion = "C:/Users/marca/Documents/Séptimo Semestre/Inteligencia Artificial/Repositorio/Laberinto/Practica 1/Laberintos/Laberinto1.txt"
#direccion = ""

laberinto = crear_laberinto(laberinto,direccion)# Creamos el laberinto


c_ancho = 16
c_largo = 16
c_list = (c_ancho, c_largo)
ancho_cuadrado = .5 # Ancho de los cuadrados
alto_cuadrado = .3 # Alto de los cuadrados
cuadrado = (ancho_cuadrado, alto_cuadrado)
separacion = (ancho_cuadrado * 10 - alto_cuadrado * 10)# Tamaño de la separación
proporcion = 70# Proporcion

# Dimensiones del laberinto (ancho y alto)
ANCHO, ALTO = calcular_alto_ancho(cuadrado,separacion,proporcion, c_list)

ancho_cuadrado *= proporcion
alto_cuadrado *= proporcion
dim_cuadrado = (ancho_cuadrado, alto_cuadrado)

#Iniciamos el pygame
pygame.init()
screen = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Maze")
reloj = pygame.time.Clock()

# Coordenadas iniciales del jugador, y coordenadas finales
x = 4
y = 15
ex = 15
ey = 2

#Tuplas para indicar el inicio y el final
Start = (x, y)
End = (ex, ey)

game_over = False
ejecutando = True

# Cuadro de texto para mostrar las coordenadas
fuente = pygame.font.Font("C:/Windows/Fonts/arial.ttf", 20)
texto_coordenadas = ""

'''Aqui es donde podemos pintar el laberinto'''
while ejecutando:
    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            ejecutando = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Clic izquierdo (pintar gris)
                pintar_cuadrado(laberinto, *event.pos,dim_cuadrado,separacion,c_list)
            elif event.button == 3:  # Clic derecho (restaurar a negro)
                restaurar_cuadrado(laberinto, *event.pos,dim_cuadrado,separacion,c_list)
        elif (event.type == pygame.KEYDOWN):
            if event.key == pygame.K_SPACE:
                ejecutando = False

    # Mostrar las coordenadas del mouse en la consola
    _x, _y = pygame.mouse.get_pos()
    fila = _y // int(alto_cuadrado + separacion)
    columna = _x // int(ancho_cuadrado + separacion)
    if 0 < fila < 16 and 0 < columna < 16:
        texto_coordenadas = f"Coordenadas del mouse: Fila {fila}, Columna {columna}"

    # Actualizar la screen
    screen.fill(FONDO)
    for fila in range(len(laberinto)):
        for columna in range(len(laberinto[0])):
            color = BLANCO if laberinto[fila][columna] else NEGRO
            _x = calcular_posicion(columna, ancho_cuadrado)
            _y = calcular_posicion(fila, alto_cuadrado)
            pygame.draw.rect(screen, color, (_x, _y, ancho_cuadrado, alto_cuadrado))

    actualizar_cuadro_texto(texto_coordenadas,screen,ALTO,fuente)
    pygame.display.flip()

'''Aqui e donde el juego comienza'''
while not game_over:
    screen.fill(FONDO)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: ##Si presionamos la X o quitamos el juego:
            pygame.quit() #Abortamos el pygame
            sys.exit() #Sliamos del programa
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                if x-1 >= 0 and laberinto[y][x-1] == 1:
                    x-=1
            elif event.key == pygame.K_RIGHT:
                if x+1 <= 15 and laberinto[y][x+1] == 1:
                    x+=1
            elif event.key == pygame.K_UP:
                if y-1 >= 0 and laberinto[y-1][x] == 1:
                    y-=1
            elif event.key == pygame.K_DOWN:
                if y+1 <= 15 and laberinto[y+1][x] == 1:
                    y+=1
    
    dibujar_laberinto(laberinto, screen, Start, End, x, y,fuente,dim_cuadrado)
    reloj.tick(60)
    pygame.display.flip()

    # Verificar si el cuadro amarillo llega al cuadro rojo
    if (x, y) == (ex, ey):
        time.sleep(1)
        game_over = True

print("¡Laberinto resuelto!")