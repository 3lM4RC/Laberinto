import pygame

cantidad_largo = 15
cantidad_ancho = 15
proporcion = 50

# Definir colores
FONDO = (173, 173, 173)
GRIS_OX = (85, 85, 85)
NEGRO = (0, 0, 0)

# Tamaño de los cuadrados
ancho_cuadrado = .6
alto_cuadrado = .4
cuadrado = (ancho_cuadrado, alto_cuadrado)

# Separación entre cuadrados
separacion = (ancho_cuadrado * 10 - alto_cuadrado * 10)

def calcular_alto_ancho(c_largo, c_ancho, tamaño, cuadrado):
    ancho, alto = cuadrado
    cuadrado_ancho = ancho * tamaño
    cuadrado_alto = alto * tamaño

    AL = (cuadrado_alto * c_largo) + (separacion * (c_largo + 1))
    AN = (cuadrado_ancho * c_ancho) + (separacion * (c_ancho + 1))
    return AL, AN

# Definir el tamaño de la ventana
AL, AN = calcular_alto_ancho(cantidad_largo, cantidad_ancho, proporcion, cuadrado)

ancho_cuadrado *= proporcion
alto_cuadrado *= proporcion

# Inicializar Pygame
pygame.init()

# Crear la ventana
ventana = pygame.display.set_mode((AN, AL))

# Matriz para el estado de los cuadrados (0 = negro, 1 = gris)
estado_cuadrados = [[0] * cantidad_ancho for _ in range(cantidad_largo)]

# Matriz para las coordenadas del mouse
coordenadas_mouse = [[(0, 0) for _ in range(cantidad_ancho)] for _ in range(cantidad_largo)]

def pintar_cuadrado(x, y):
    fila = y // int(alto_cuadrado + separacion)
    columna = x // int(ancho_cuadrado + separacion)
    
    if fila < cantidad_largo and columna < cantidad_ancho:
        estado_cuadrados[fila][columna] = 1

def restaurar_cuadrado(x, y):
    fila = y // int(alto_cuadrado + separacion)
    columna = x // int(ancho_cuadrado + separacion)
    
    if fila < cantidad_largo and columna < cantidad_ancho:
        estado_cuadrados[fila][columna] = 0

# Bucle principal
ejecutando = True
while ejecutando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ejecutando = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Clic izquierdo (pintar gris)
                pintar_cuadrado(*event.pos)
            elif event.button == 3:  # Clic derecho (restaurar a negro)
                restaurar_cuadrado(*event.pos)

    # Mostrar las coordenadas del mouse en la consola
    x, y = pygame.mouse.get_pos()
    fila = y // int(alto_cuadrado + separacion)
    columna = x // int(ancho_cuadrado + separacion)
    if fila < cantidad_largo and columna < cantidad_ancho:
        print(f"Coordenadas del mouse: Fila {fila}, Columna {columna}")

    # Actualizar la ventana
    ventana.fill(FONDO)
    for fila in range(cantidad_largo):
        for columna in range(cantidad_ancho):
            color = GRIS_OX if estado_cuadrados[fila][columna] else NEGRO
            x = (columna * (ancho_cuadrado + separacion)) + separacion
            y = (fila * (alto_cuadrado + separacion)) + separacion
            pygame.draw.rect(ventana, color, (x, y, ancho_cuadrado, alto_cuadrado))

    pygame.display.flip()

# Salir de Pygame
pygame.quit()
