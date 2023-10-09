import pygame

cantidad_largo = 15
cantidad_ancho = 15
proporcion = 90

# Definir colores
FONDO = (173, 173, 173)
GRIS_OX = (85, 85, 85)
NEGRO = (0, 0, 0)


# Tamaño de los cuadrados
ancho_cuadrado = .6
alto_cuadrado = .4
cuadrado = (ancho_cuadrado, alto_cuadrado)

# Separación entre cuadrados
separacion = (ancho_cuadrado*10 - alto_cuadrado*10)

def calcular_alto_ancho(c_largo, c_ancho, tamaño, cuadrado):
    ancho, alto = cuadrado
    cuadrado_ancho = ancho * tamaño
    cuadrado_alto = alto * tamaño

    AL = (cuadrado_alto * c_largo) + (separacion*(c_largo+1))
    AN = (cuadrado_ancho * c_ancho) + (separacion*(c_ancho+1))
    return AL,AN

# Definir el tamaño de la ventana
AL, AN = calcular_alto_ancho(cantidad_largo, cantidad_ancho,proporcion, cuadrado)

ancho_cuadrado *= proporcion
alto_cuadrado *= proporcion
# Inicializar Pygame
pygame.init()

# Crear la ventana
ventana = pygame.display.set_mode((AN, AL))

'''# Calcular la cantidad de cuadrados que caben en la ventana
filas = ventana_alto // (alto_cuadrado + separacion)
columnas = ventana_ancho // (ancho_cuadrado + separacion)'''

# Bucle principal
ejecutando = True
while ejecutando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ejecutando = False
        else:
            ventana.fill(FONDO)
            # Bucle para dibujar los cuadrados
            for fila in range(cantidad_largo):
                for columna in range(cantidad_ancho):
                    x = (columna * (ancho_cuadrado+separacion))+separacion
                    y = (fila * (alto_cuadrado+separacion))+separacion
                    pygame.draw.rect(ventana, NEGRO, (x, y, ancho_cuadrado, alto_cuadrado))


    # Actualizar la pantalla
    pygame.display.flip()

# Salir de Pygame
pygame.quit()