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

def actualizar_cuadro_texto(texto, ventana, AL,fuente):
    texto = fuente.render(texto, True, NEGRO)
    ventana.blit(texto, (10, AL - 50))

'''Con las siguientes 2 fucniones podemos calcular el tamaño de la pagina dependiendo del tamaño del laberinto'''
def calcular_alto_ancho(cuadrado,separacion,proporcion,c_list):
    c_ancho, c_largo = c_list
    ancho, alto = cuadrado
    cuadrado_ancho = ancho * proporcion
    cuadrado_alto = alto * proporcion

    AL = (cuadrado_alto * c_largo) + (separacion * (c_largo + 1))+60
    AN = (cuadrado_ancho * c_ancho) + (separacion * (c_ancho + 1))
    return AN, AL

'''Con esta función podemos abrir el archivo de laberinto que nosotros queramos'''
def pedir_laberinto(file_path):
    if not file_path:
        # Crear una ventana principal
        root = tk.Tk()
        root.withdraw()  # Ocultar la ventana principal

        # Abrir el cuadro de diálogo para seleccionar un archivo TXT
        file_path = filedialog.askopenfilename(filetypes=[("Archivos TXT", "*.txt")])
        print(file_path)

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
def crear_laberinto(laberinto,direccion):
    if not laberinto:
        laberinto = pedir_laberinto(direccion)

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
def dibujar_laberinto(laberinto,screen, start, end, x, y,fuente,dim_cuadrado,separacion,ancho_alto):
    ANCHO, ALTO = ancho_alto
    ancho_cuadrado, alto_cuadrado = dim_cuadrado
    Sx, Sy = start
    Sx = calcular_posicion(Sx,ancho_cuadrado,separacion)
    Sy = calcular_posicion(Sy, alto_cuadrado,separacion)
    Ex, Ey = end
    Ex = calcular_posicion(Ex,ancho_cuadrado,separacion)
    Ey = calcular_posicion(Ey,alto_cuadrado,separacion)
    for fila in range(len(laberinto)):
        for columna in range(len(laberinto[0])):
            if (fila == 0) | (columna == 0):

                #pygame.draw.rect(screen, GRIS, (columna * 40, fila * 40, 40, 40))  
                #if isinstance(laberinto[fila][columna], str):
                # Si el contenido en laberinto[fila][columna] es una letra, imprímela
                col = calcular_posicion(columna,ancho_cuadrado,separacion)
                fil = calcular_posicion(fila,alto_cuadrado,separacion)
                coord = str(laberinto[fila][columna])
                pygame.draw.rect(screen, NEGRO, (col,fil, ancho_cuadrado, alto_cuadrado))
                font = fuente
                texto = font.render(coord, True, BLANCO)  # Color del texto (negro)
                text_rect = texto.get_rect()
                text_rect.center = (col+(ancho_cuadrado/2),fil+(alto_cuadrado/2))  # Centro del rectángulo
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
                _x = calcular_posicion(columna,ancho_cuadrado,separacion)
                _y = calcular_posicion(fila,alto_cuadrado,separacion)
                pygame.draw.rect(screen, color, (_x, _y, ancho_cuadrado, alto_cuadrado))
    if(x == 15)&(y == 2):
        texto_coordenadas = "FELICIDADES!! ACABAS DE SALIR DE LA FRIENDZONE"
    else:
        texto_coordenadas = f"Coordenadas del mouse: Fila {y}, Columna {x}"
    actualizar_cuadro_texto(texto_coordenadas,screen,ALTO,fuente)

    x = calcular_posicion(x,ancho_cuadrado,separacion)
    y = calcular_posicion(y,alto_cuadrado,separacion)
    # Dibujar la entrada (azul) en [14][3]
    pygame.draw.rect(screen, AZUL, (Sx,Sy, ancho_cuadrado, alto_cuadrado))

    # Dibujar la salida (rojo) en [14][1]
    pygame.draw.rect(screen, ROJO, (Ex,Ey, ancho_cuadrado, alto_cuadrado))

    # Dibujar el punto amarillo en la posición actual
    pygame.draw.rect(screen, NARANJA, (x, y, ancho_cuadrado, alto_cuadrado))
    

'''Funcion para poder pintar los cuadros'''
def pintar_cuadrado(laberinto, x, y,dim_cuadrado,separacion,c_list):
    c_ancho, c_largo = c_list
    ancho_cuadrado, alto_cuadrado = dim_cuadrado
    fila = y // int(alto_cuadrado + separacion)
    columna = x // int(ancho_cuadrado + separacion)
    
    if (0 < fila < c_largo+1) and (0 < columna < c_ancho):
        laberinto[fila][columna] = 1

'''Funcion pintar los cuadros de negro otra vez'''
def restaurar_cuadrado(laberinto, x, y, dim_cuadrado,separacion,c_list):
    c_ancho, c_largo = c_list
    ancho_cuadrado, alto_cuadrado = dim_cuadrado
    fila = y // int(alto_cuadrado + separacion)
    columna = x // int(ancho_cuadrado + separacion)
    
    if (0 < fila < c_largo+1) and (0 < columna < c_ancho):
        laberinto[fila][columna] = 0

'''Funcion para transformar una posicion entera en una coordenada de panatalla'''
def calcular_posicion(coord, tamaño,separacion):
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