import pygame
import sys
import tkinter as tk
from tkinter import filedialog
import ast
import string
import time

# Colores
FONDO = (173, 173, 173)
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
GRIS = (128,128,128)
GRIS_OX = (85, 85, 85)
VERDE = (150,210,80)
AZUL = (0, 175, 255)
CARNE = (250, 191, 143)
ROJO = (255, 0, 0)
NARANJA = (255, 192, 0)

# Tamaño de los cuadrados
ancho_cuadrado = .6
alto_cuadrado = .4
cuadrado = (ancho_cuadrado, alto_cuadrado)
proporcion =50

# Tamaño de la separación
separacion = (ancho_cuadrado * 10 - alto_cuadrado * 10)

#laberinto = pedir_laberinto()
# Laberinto
laberinto = [
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
]

#Cantidad de cuardados
c_largo = len(laberinto)+1
c_ancho = len(laberinto[0])+1

def pedir_laberinto():

    # Crear una ventana principal
    root = tk.Tk()
    root.withdraw()  # Ocultar la ventana principal

    # Abrir el cuadro de diálogo para seleccionar un archivo TXT
    file_path = filedialog.askopenfilename(filetypes=[("Archivos TXT", "*.txt")])

    if file_path:
        # Leer el contenido del archivo TXT y eliminar comas y paréntesis
        with open(file_path, 'r') as file:
            text = file.read()

        # Convertir el texto en una lista anidada de Python utilizando ast.literal_eval
        try:
            matrix = ast.literal_eval(text)
            # Ahora, 'matrix' contiene la matriz bidimensional de Python
            print("Matriz cargada correctamente en la variable 'matrix'.")
            return matrix
        except Exception as e:
            print(f"Error al cargar la matriz: {str(e)}")
    else:
        print("No se seleccionó ningún archivo TXT.")

def calcular_alto_ancho():
    ancho, alto = cuadrado
    cuadrado_ancho = ancho * proporcion
    cuadrado_alto = alto * proporcion

    AL = (cuadrado_alto * c_largo) + (separacion * (c_largo + 1))+60
    AN = (cuadrado_ancho * c_ancho) + (separacion * (c_ancho + 1))
    return AN, AL
# Dimensiones del laberinto (ancho y alto)
ANCHO, ALTO = calcular_alto_ancho()

def dibujar_botones_inicio():
    # Botón para empezar a jugar
    pygame.draw.rect(screen, AZUL, (150, 200, 300, 50))  # Rectángulo del botón de jugar
    font = pygame.font.Font(None, 36)
    texto_jugar = font.render("Empezar a Jugar", True, BLANCO)
    screen.blit(texto_jugar, (200, 210))

    # Botón para crear niveles
    pygame.draw.rect(screen, VERDE, (150, 300, 300, 50))  # Rectángulo del botón de crear niveles
    texto_niveles = font.render("Crear Niveles", True, BLANCO)
    screen.blit(texto_niveles, (220, 310))

ancho_cuadrado *= proporcion
alto_cuadrado *= proporcion

def crear_laberinto():
    #laberinto = pedir_laberinto()

    #Aqui es donde ponemos las coordenadas laterales con numeros
    cantidad_numeros = len(laberinto[0])
    for i in range(cantidad_numeros):
        laberinto[i] = [i+1] + laberinto[i]

    #Aqui es donde ponemos las coordenadas superiores con letras
    cantidad_letras = len(laberinto)
    letras = list(string.ascii_lowercase)[:cantidad_letras]
    laberinto.insert(0,[" "] + letras)

    # Imprimir el laberinto con la nueva columna
    for fila in laberinto:
        print(fila)
    return laberinto

laberinto = crear_laberinto()




def calcular_posicion(coord,tamaño):
    value = (coord * (tamaño + separacion)) + separacion
    return value


# Coordenadas iniciales del jugador, y coordenadas finales
x = calcular_posicion(4,ancho_cuadrado)
y = calcular_posicion(15,alto_cuadrado)
ex = calcular_posicion(15,ancho_cuadrado)
ey = calcular_posicion(2,alto_cuadrado)

#Tuplas para indicar el inicio y el final
Start = (x, y)
End = (ex, ey)

'''Con esta función imprimios el laberinto constantemente'''
def dibujar_laberinto(start, end,posicion):
    Sx, Sy = start
    Ex, Ey = end
    _x, _y = posicion
    _x = calcular_posicion(_x,ancho_cuadrado)
    _y = calcular_posicion(_y,alto_cuadrado)
    for fila in range(len(laberinto)):
        for columna in range(len(laberinto[0])):
            x = calcular_posicion(columna,ancho_cuadrado)
            y = calcular_posicion(fila,alto_cuadrado)
            if (fila == 0) | (columna == 0):

                #pygame.draw.rect(screen, GRIS, (columna * 40, fila * 40, 40, 40))  
                #if isinstance(laberinto[fila][columna], str):
                # Si el contenido en laberinto[fila][columna] es una letra, imprímela

                coord = str(laberinto[fila][columna])
                pygame.draw.rect(screen, NEGRO, (x, y, ancho_cuadrado, alto_cuadrado))
                font = pygame.font.Font("C:/Windows/Fonts/arial.ttf", 20)  # Fuente y tamaño de la letra
                texto = font.render(coord, True, BLANCO)  # Color del texto (negro)
                text_rect = texto.get_rect()
                text_rect.center = (x+(ancho_cuadrado/2), y+(alto_cuadrado/2))  # Centro del rectángulo
                screen.blit(texto, text_rect)  # Dibuja el texto en el centro del rectángulo
            else: 
                if laberinto[fila][columna] == 0:
                    color = GRIS_OX
                elif laberinto[fila][columna] == 2:
                    color = VERDE
                elif laberinto[fila][columna] == 3:
                    color = CARNE
                elif laberinto[fila][columna] == 4:
                    color = AZUL
                elif laberinto[fila][columna] == 5:
                    color = NARANJA
                else: 
                    color = BLANCO
                pygame.draw.rect(screen, color, (x, y, ancho_cuadrado, alto_cuadrado))

    # Dibujar la entrada (azul) en [14][3]
    pygame.draw.rect(screen, AZUL, (Sx,Sy, ancho_cuadrado, alto_cuadrado))

    # Dibujar la salida (rojo) en [14][1]
    pygame.draw.rect(screen, ROJO, (Ex,Ey, ancho_cuadrado, alto_cuadrado))

    # Dibujar el punto amarillo en la posición actual
    pygame.draw.rect(screen, NARANJA, (_x, _y, ancho_cuadrado, alto_cuadrado))
    pygame.display.flip()



pygame.init()
screen = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Laberinto")
screen.fill(FONDO)

reloj = pygame.time.Clock()

# Coordenadas iniciales del punto amarillo (entrada)
_x = 4
_y = 15
game_over = False

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                if _x - 1 > 0 and laberinto[_y][_x-1] == 1:
                    _x -= 1
            elif event.key == pygame.K_RIGHT:
                if _x + 1 < (c_ancho+1) and laberinto[_y][_x+1] == 1:
                    _x += 1
            elif event.key == pygame.K_UP:
                if _y - 1 > 0 and laberinto[_y-1][_x] == 1:
                    _y -= 1
            elif event.key == pygame.K_DOWN:
                if _y + 1 < (c_largo) and laberinto[_y+1][_x] == 1:
                    _y += 1
    posicion = (_x, _y )
    dibujar_laberinto(Start,End,posicion)

    pygame.display.flip()
    reloj.tick(60)

    # Verificar si el cuadro amarillo llega al cuadro rojo
    if (_x, _y) == (15, 2):
        time.sleep(1)
        game_over = True

print("¡Laberinto resuelto!")

