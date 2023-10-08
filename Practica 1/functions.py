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

'''Con las siguientes 2 fucniones podemos calcular el tamaño de la pagina dependiendo del tamaño del laberinto'''
def calcular_alto(laberinto):
    ALTO = (len(laberinto) * 40)
    return ALTO
def calcular_ancho(laberinto):
    ANCHO = (len(laberinto) * 40)
    return ANCHO

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
def crear_laberinto():
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
                pygame.draw.rect(screen, GRIS, (columna * 40, fila * 40, 40, 40))
                font = pygame.font.Font("C:/Windows/Fonts/arial.ttf", 24)  # Fuente y tamaño de la letra
                texto = font.render(coord, True, NEGRO)  # Color del texto (negro)
                text_rect = texto.get_rect()
                text_rect.center = (columna * 40 + 20, fila * 40 + 20)  # Centro del rectángulo
                screen.blit(texto, text_rect)  # Dibuja el texto en el centro del rectángulo
            else: 
                if laberinto[fila][columna] == 0:
                    color = GRIS
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
                pygame.draw.rect(screen, color, (columna * 40, fila * 40, 40, 40))

    # Dibujar la entrada (azul) en [14][3]
    pygame.draw.rect(screen, AZUL, (Sx,Sy, 40, 40))

    # Dibujar la salida (rojo) en [14][1]
    pygame.draw.rect(screen, ROJO, (Ex,Ey, 40, 40))

    # Dibujar el punto amarillo en la posición actual
    pygame.draw.rect(screen, NARANJA, (x, y, 40, 40))
    pygame.display.flip()