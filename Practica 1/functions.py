import pygame
import tkinter as tk
from tkinter import filedialog
import sys
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
AMARILLO = (255, 255, 0)

# Tamaño de los cuadrados
ancho_cuadrado = .6
alto_cuadrado = .4
cuadrado = (ancho_cuadrado, alto_cuadrado)

#Cantidad de cuardados
c_largo = 15
c_ancho = 15
proporcion = 100

# Tamaño de la separación
separacion = (ancho_cuadrado * 10 - alto_cuadrado * 10)

def actualizar_cuadro_texto(texto_coordenadas, ventana, AL,fuente):
    texto = fuente.render(texto_coordenadas, True, NEGRO)
    ventana.blit(texto, (20, AL - 50))

'''Con las siguientes 2 fucniones podemos calcular el tamaño de la pagina dependiendo del tamaño del laberinto'''
def calcular_alto_ancho():
    ancho, alto = cuadrado
    cuadrado_ancho = ancho * proporcion
    cuadrado_alto = alto * proporcion

    AL = (cuadrado_alto * c_largo) + (separacion * (c_largo + 1))+60
    AN = (cuadrado_ancho * c_ancho) + (separacion * (c_ancho + 1))
    return AN, AL

'''Con esta función podemos abrir el archivo de laberinto que nosotros queramos'''
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

'''Con esta función usamos el archivo consultado y cremos una lista bidimensional con las coordenadas impresas'''
def crear_laberinto(laberinto):
    if not laberinto:
        laberinto = pedir_laberinto()

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


ancho_cuadrado *= proporcion
alto_cuadrado *= proporcion

'''Con esta función imprimios el laberinto constantemente'''
def dibujar_laberinto(laberinto,screen, start, end, x, y):
    Sx, Sy = start
    Ex, Ey = end
    for fila in range(len(laberinto)):
        for columna in range(len(laberinto[0])):
            if (fila == 0) | (columna == 0):

                #pygame.draw.rect(screen, GRIS, (columna * 40, fila * 40, 40, 40))  
                #if isinstance(laberinto[fila][columna], str):
                # Si el contenido en laberinto[fila][columna] es una letra, imprímela

                coord = str(laberinto[fila][columna])
                pygame.draw.rect(screen, NEGRO, (columna * 60, fila * 40, ancho_cuadrado, alto_cuadrado))
                font = pygame.font.Font("C:/Windows/Fonts/arial.ttf", 18)  # Fuente y tamaño de la letra
                texto = font.render(coord, True, BLANCO)  # Color del texto (negro)
                text_rect = texto.get_rect()
                text_rect.center = (columna * 60 + 20, fila * 40 + 20)  # Centro del rectángulo
                screen.blit(texto, text_rect)  # Dibuja el texto en el centro del rectángulo
            else: 
                if laberinto[fila][columna] == 0:
                    color = NEGRO
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
                _x = (columna * (ancho_cuadrado + separacion)) + separacion
                _y = (fila * (alto_cuadrado + separacion)) + separacion
                pygame.draw.rect(screen, color, (_x, _y, ancho_cuadrado, alto_cuadrado))

    # Dibujar la entrada (azul) en [14][3]
    pygame.draw.rect(screen, AZUL, (Sx,Sy, ancho_cuadrado, alto_cuadrado))

    # Dibujar la salida (rojo) en [14][1]
    pygame.draw.rect(screen, ROJO, (Ex,Ey, ancho_cuadrado, alto_cuadrado))

    # Dibujar el punto amarillo en la posición actual
    pygame.draw.rect(screen, NARANJA, (x, y, ancho_cuadrado, alto_cuadrado))

'''Funcion para poder pintar los cuadros'''
def pintar_cuadrado(laberinto, x, y):
    fila = y // int(alto_cuadrado + separacion)
    columna = x // int(ancho_cuadrado + separacion)
    
    if (0 < fila < c_largo) and (0 < columna < c_ancho):
        laberinto[fila][columna] = 1

def restaurar_cuadrado(laberinto, x, y):
    fila = y // int(alto_cuadrado + separacion)
    columna = x // int(ancho_cuadrado + separacion)
    
    if (0 < fila < c_largo) and (0 < columna < c_ancho):
        laberinto[fila][columna] = 0

def calcular_posicion(coord, tamaño):
    value = coord * (tamaño + separacion) + separacion
    return value

def imprimir_menu(ALTO,ANCHO,pantalla,fuente_menus):
    opciones = ["1. Comenzar juego", "2. Cargar un mapa", "3. Crear mapa nuevo", "4. Ver opciones", "5. Salir del juego"]
    boton_alto = 80  # Altura de cada botón
    espacio_entre_botones = 10  # Espacio entre botones
    total_botones = len(opciones)
    alto_total_botones = total_botones * (boton_alto + espacio_entre_botones) - espacio_entre_botones
    y_inicial = (ALTO - alto_total_botones) // 2
    
    for i, opcion in enumerate(opciones):
        texto_opcion = fuente_menus.render(opcion, True, BLANCO)
        cuadro_opcion = pygame.Rect((ANCHO-300) // 2, y_inicial + i * (boton_alto + espacio_entre_botones), 300, boton_alto)
        pygame.draw.rect(pantalla, NEGRO, cuadro_opcion)
        pygame.draw.rect(pantalla, AMARILLO, cuadro_opcion, 5)  # Cuadro de opción
        text_rect = texto_opcion.get_rect()
        text_rect.center = cuadro_opcion.center
        pantalla.blit(texto_opcion, text_rect)