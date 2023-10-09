import pygame
import sys

cantidad_largo = 16
cantidad_ancho = 16
proporcion = 80

# Definir colores
FONDO = (173, 173, 173)
GRIS_OX = (85, 85, 85)
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)

# Tamaño de los cuadrados
ancho_cuadrado = .6
alto_cuadrado = .4
cuadrado = (ancho_cuadrado, alto_cuadrado)

# Separación entre cuadrados
separacion = (ancho_cuadrado * 10 - alto_cuadrado * 10)

def calcular_alto_ancho(c_largo, c_ancho, proporcion, cuadrado):
    ancho, alto = cuadrado
    cuadrado_ancho = ancho * proporcion
    cuadrado_alto = alto * proporcion

    AL = (cuadrado_alto * c_largo) + (separacion * (c_largo + 1))+60
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

# Matriz para el estado de los cuadrados (0 = negro, 1 = blanco)
estado_cuadrados = [[0] * cantidad_ancho for _ in range(cantidad_largo)]

# Cuadro de texto para mostrar las coordenadas
fuente = pygame.font.Font("C:/Windows/Fonts/arial.ttf", 24)
texto_coordenadas = ""

def actualizar_cuadro_texto():
    texto = fuente.render(texto_coordenadas, True, NEGRO)
    ventana.blit(texto, (20, AL - 50))

# Bucle principal
ejecutando = True
pintando = False  # Indica si se está pintando o restaurando
while ejecutando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ejecutando = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Clic izquierdo
                x, y = event.pos
                fila = y // int(alto_cuadrado + separacion)
                columna = x // int(ancho_cuadrado + separacion)
                if (0 <fila < cantidad_largo) and (0 < columna < cantidad_ancho):
                    estado = estado_cuadrados[fila][columna]
                    estado_cuadrados[fila][columna] = 1 - estado  # Alternar entre blanco y negro
                    pintando = estado == 0  # Actualizar el estado de pintado/restauración

    # Mostrar las coordenadas del mouse en el cuadro de texto
    x, y = pygame.mouse.get_pos()
    fila = y // int(alto_cuadrado + separacion)
    columna = x // int(ancho_cuadrado + separacion)
    if (0 <fila < cantidad_largo) and (0 < columna < cantidad_ancho):
        texto_coordenadas = f"Coordenadas: Fila {fila}, Columna {columna}"

    # Actualizar la ventana
    ventana.fill(FONDO)
    for fila in range(cantidad_largo):
        for columna in range(cantidad_ancho):
            color = BLANCO if estado_cuadrados[fila][columna] else NEGRO
            x = (columna * (ancho_cuadrado + separacion)) + separacion
            y = (fila * (alto_cuadrado + separacion)) + separacion
            pygame.draw.rect(ventana, color, (x, y, ancho_cuadrado, alto_cuadrado))

    actualizar_cuadro_texto()
    pygame.display.flip()

# Salir de Pygame
pygame.quit()
sys.exit()
