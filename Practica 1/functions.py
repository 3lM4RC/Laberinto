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
VERDE_NEON = (0,211,0)
VERDE = (150,210,80)
AZUL = (0, 175, 255)
AZUL_OP = (0, 175, 188)
CARNE = (250, 191, 143)
ROJO = (255, 0, 0)
ROJO_OP = (188, 0, 0)
NARANJA = (255, 192, 0)
AMARILLO = (255, 255, 0)
MORADO = (42,0,53)
TRANSPARENTE = (255, 0, 255, 128)

def definir_inicio_final(screen,laberinto, dim_cuadrado,separacion,c_list,inicio,final,ALTO,fuente):
    ix, iy = inicio
    ejecutando = True
    c_ancho, c_largo = c_list
    ancho, alto = dim_cuadrado
    while ejecutando:
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                ejecutando = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Clic izquierdo (pintar gris)
                    x,y = pygame.mouse.get_pos()
                    fila = y // int(alto + separacion)
                    columna = x // int(ancho + separacion)
                    if (0 < fila < c_largo+1) and (0 < columna < c_ancho):
                        inicio = (columna,fila)
                        laberinto[fila][columna] = "i"
                        laberinto[iy][ix] = "0"
                elif event.button == 3:  # Clic derecho (restaurar a negro)
                    x,y = pygame.mouse.get_pos()
                    fila = y // int(alto + separacion)
                    columna = x // int(ancho + separacion)
                    if (0 < fila < c_largo+1) and (0 < columna < c_ancho):
                        final = (columna,fila)
                        laberinto[fila][columna] = "f"
                        laberinto[iy][ix] = "0"
            elif (event.type == pygame.KEYDOWN):
                if event.key == pygame.K_SPACE:
                    return inicio,final

        # Mostrar las coordenadas del mouse en la consola
        _x, _y = pygame.mouse.get_pos()
        fila = _y // int(alto + separacion)
        columna = _x // int(ancho + separacion)
        if 0 < fila < c_largo+1 and 0 < columna < c_ancho:
            texto_coordenadas = f"Coordenadas del mouse: Fila {fila}, Columna {columna}"
        sx,sy = inicio
        ex,ey = final
        sx = calcular_posicion(sx,ancho,separacion)
        sy = calcular_posicion(sy,alto,separacion)
        ex = calcular_posicion(ex,ancho,separacion)
        ey = calcular_posicion(ey,alto,separacion)
        # Actualizar la screen
        screen.fill(FONDO)
        for fila in range(len(laberinto)):
            for columna in range(len(laberinto[0])):
    
                color = BLANCO if laberinto[fila][columna] else NEGRO
                _x = calcular_posicion(columna, ancho,separacion)
                _y = calcular_posicion(fila, alto,separacion)
                pygame.draw.rect(screen, color, (_x, _y, ancho, alto))
                pygame.draw.rect(screen, ROJO_OP, (ex, ey, ancho, alto))
                pygame.draw.rect(screen, AZUL_OP, (sx, sy, ancho, alto))

        actualizar_cuadro_texto(texto_coordenadas,screen,ALTO,fuente)
        pygame.display.flip()

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
            # Ahora, 'matrix' contiene la malla_oculta bidimensional de Python
            print("malla_oculta cargada correctamente en la variable 'matrix'.")
            return matrix
        except Exception as e:
            print(f"Error al cargar la malla_oculta: {str(e)}")
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
def dibujar_laberinto(laberinto,screen, start, end, x, y,fuente,dim_cuadrado,separacion,ALTO,malla_oculta):
    c_ancho = len(laberinto)
    c_largo = len(laberinto[0])
    
#    ANCHO, ALTO = ancho_alto
    ancho_cuadrado, alto_cuadrado = dim_cuadrado
    Ex, Ey = end
    if(x == Ex)&(y == Ey):
        texto_coordenadas = "FELICIDADES!! ACABAS DE SALIR DE LA FRIENDZONE!"
    else:
        texto_coordenadas = f"Fila {laberinto[y][0]}, Columna {laberinto[0][x]}"

    Sx, Sy = start
    Sx = calcular_posicion(Sx,ancho_cuadrado,separacion)
    Sy = calcular_posicion(Sy, alto_cuadrado,separacion)
    
    Ex = calcular_posicion(Ex,ancho_cuadrado,separacion)
    Ey = calcular_posicion(Ey,alto_cuadrado,separacion)
    for fila in range(c_ancho):
        for columna in range(c_largo):
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
                if laberinto[fila][columna] == "V":
                    _x += ancho_cuadrado/2 
                    _y += alto_cuadrado/2
                    pygame.draw.circle(screen,VERDE_NEON,(_x,_y),8)
                if laberinto[fila][columna] == "O":
                    _x += ancho_cuadrado/2 
                    _y += alto_cuadrado/2
                    pygame.draw.circle(screen,VERDE_NEON,(_x,_y),8)
                    pygame.draw.circle(screen,ROJO,(_x,_y),12,5)

    actualizar_cuadro_texto(texto_coordenadas,screen,ALTO,fuente)

    descubrir_malla(malla_oculta,x,y)
    x = calcular_posicion(x,ancho_cuadrado,separacion)
    y = calcular_posicion(y,alto_cuadrado,separacion)
    # Dibujar la entrada (azul) en [14][3]
    pygame.draw.rect(screen, AZUL, (Sx,Sy, ancho_cuadrado, alto_cuadrado))

    # Dibujar la salida (rojo) en [14][1]
    pygame.draw.rect(screen, ROJO, (Ex,Ey, ancho_cuadrado, alto_cuadrado))

    # Dibujar el punto amarillo en la posición actual
    #pygame.draw.rect(screen, NARANJA, (x+(separacion*5), y, ancho_cuadrado-(separacion*10), alto_cuadrado),border_radius=15)    
    x += ancho_cuadrado/2 
    y += alto_cuadrado/2

    for fila in range(len(malla_oculta)):
        for columna in range(len(malla_oculta[0])):
            if fila != 0 and columna != 0:
                color = TRANSPARENTE if malla_oculta[fila][columna] else NEGRO
                Bx = calcular_posicion(columna, ancho_cuadrado,2)
                By = calcular_posicion(fila, alto_cuadrado,2)
                if color == NEGRO:
                    pygame.draw.rect(screen, color, (Bx, By, ancho_cuadrado, alto_cuadrado))
    pygame.draw.circle(screen,NARANJA,(x,y),15)

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

def imprimir_menu(ALTO,ANCHO,pantalla,fuente_menus,estado):
    boton_alto = 80  # Altura de cada botón
    espacio_entre_botones = 10  # Espacio entre botones
    if not estado:
        opciones = ["1. Comenzar juego", "2. Cargar un mapa", "3. Crear mapa nuevo", "4. Ver opciones", "5. Salir del juego"]
    if estado == 2:
        opciones = ["1. Cargar un mapa", "2. Crear un mapa desde 0"]
    if estado == 3:
        opciones = ["1. Volver a jugar", "2. Guardar el mapa","3. Salir sin guardar el mapa"]
    
    total_botones = len(opciones)
    alto_total_botones = total_botones * (boton_alto + espacio_entre_botones) - espacio_entre_botones
    y_inicial = (ALTO - alto_total_botones) // 2
    
    for i, opcion in enumerate(opciones):
        texto_opcion = fuente_menus.render(opcion, True, BLANCO)
        cuadro_opcion = pygame.Rect((ANCHO-300) // 2, y_inicial + i * (boton_alto + espacio_entre_botones), 300, boton_alto)
        pygame.draw.rect(pantalla, MORADO, cuadro_opcion)
        pygame.draw.rect(pantalla, AMARILLO, cuadro_opcion, 5)  # Cuadro de opción
        text_rect = texto_opcion.get_rect()
        text_rect.center = cuadro_opcion.center
        pantalla.blit(texto_opcion, text_rect)
    

def empezar_juego(datos,reloj):
    game_over = False
    laberinto, pantalla, Start, End, x, y,fuente,dim_cuadrado,separacion,ALTO = datos
    c_ancho = len(laberinto)
    c_largo = len(laberinto[0])+1
    c_list = (c_ancho, c_largo)
    malla_oculta = crear_lab_blanco(c_ancho,c_largo)
    Start, End = definir_inicio_final(pantalla,laberinto, dim_cuadrado,separacion,c_list,Start,End,ALTO,fuente)
    x, y = Start
    ex, ey = End
    while True:
        pantalla.fill(FONDO)
        for event in pygame.event.get():
            if event.type == pygame.QUIT: ##Si presionamos la X o quitamos el juego:
                pygame.quit() #Abortamos el pygame
                sys.exit() #Sliamos del programa
            elif event.type == pygame.KEYDOWN:
                if game_over == True:
                    print("Saliendo")
                    #pygame.time.wait(2000)
                    return 1
                if (event.key == pygame.K_LEFT)or(event.key == pygame.K_a):
                    if x-1 > 0 and laberinto[y][x-1] != 0:
                        if analizar_decision(laberinto,x,y,c_list) == 1:
                            laberinto[y][x] = "O"
                        else:
                            laberinto[y][x] = "V"
                        x-=1
                        laberinto[y][x] = "X"
                elif (event.key == pygame.K_RIGHT)or(event.key == pygame.K_d):
                    if x+1 <= 15 and laberinto[y][x+1] != 0:
                        if analizar_decision(laberinto,x,y,c_list) == 1:
                            laberinto[y][x] = "O"
                        else:
                            laberinto[y][x] = "V"
                        x+=1
                        laberinto[y][x] = "X"
                elif (event.key == pygame.K_UP)or(event.key == pygame.K_w):
                    if y-1 > 0 and laberinto[y-1][x] != 0:
                        if analizar_decision(laberinto,x,y,c_list) == 1:
                            laberinto[y][x] = "O"
                        else:
                            laberinto[y][x] = "V"
                        y-=1
                        laberinto[y][x] = "X"
                elif (event.key == pygame.K_DOWN)or(event.key == pygame.K_s):
                    if y+1 <= 15 and laberinto[y+1][x] != 0:
                        if analizar_decision(laberinto,x,y,c_list) == 1:
                            laberinto[y][x] = "O"
                        else:
                            laberinto[y][x] = "V"
                        y+=1
                        laberinto[y][x] = "X"
                elif event.key == pygame.K_ESCAPE:
                    print("saliendo del juego")
                    return 0

            dibujar_laberinto(laberinto, pantalla, Start, End, x, y,fuente,dim_cuadrado,separacion,ALTO,malla_oculta)
            reloj.tick(60)
            pygame.display.flip()

            # Verificar si el cuadro amarillo llega al cuadro rojo
            if (x, y) == (ex, ey):
                game_over = True
            
def editar_laberinto(datos,c_list):
    texto_coordenadas = ""
    laberinto, pantalla, Start, End, x, y,fuente,dim_cuadrado,separacion,ALTO = datos
    ancho_cuadrado, alto_cuadrado = dim_cuadrado
    while True:
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Clic izquierdo (pintar gris)
                    pintar_cuadrado(laberinto, *event.pos,dim_cuadrado,separacion,c_list)
                elif event.button == 3:  # Clic derecho (restaurar a negro)
                    restaurar_cuadrado(laberinto, *event.pos,dim_cuadrado,separacion,c_list)
            elif (event.type == pygame.KEYDOWN):
                if event.key == pygame.K_SPACE:
                    return 2
                elif event.key == pygame.K_ESCAPE:
                    return 0

        # Mostrar las coordenadas del mouse en la consola
        _x, _y = pygame.mouse.get_pos()
        fila = _y // int(alto_cuadrado + separacion)
        columna = _x // int(ancho_cuadrado + separacion)
        if 0 < fila < 16 and 0 < columna < 16:
            texto_coordenadas = f"Coordenadas del mouse: Fila {fila}, Columna {columna}"

        # Actualizar la screen
        pantalla.fill(FONDO)
        for fila in range(len(laberinto)):
            for columna in range(len(laberinto[0])):
                color = BLANCO if laberinto[fila][columna] else NEGRO
                _x = calcular_posicion(columna, ancho_cuadrado,separacion)
                _y = calcular_posicion(fila, alto_cuadrado,separacion)
                pygame.draw.rect(pantalla, color, (_x, _y, ancho_cuadrado, alto_cuadrado))


        actualizar_cuadro_texto(texto_coordenadas,pantalla,ALTO,fuente)
        pygame.display.flip()

def crear_lab_blanco(rows,columns):
    laberinto_en_blanco = [[0 for i in range(0,columns)] for j in range(0,rows)]
    return laberinto_en_blanco

def analizar_decision(laberinto,x,y,c_list):
    c_ancho, c_largo = c_list
    decision = 0
    if (x < c_ancho-1)and(y < c_largo-2):
        if laberinto[y][x+1] != 0:
            decision+=1
        if laberinto[y][x-1] != 0:
            decision+=1
        if laberinto[y+1][x] != 0:
            decision+=1
        if laberinto[y-1][x] != 0:
            decision+=1
    if decision >2:
        return 1
    else:
        return 0
    
def hacer_calculos(laberinto,datos):
    cuadrado,separacion,proporcion = datos
    c_ancho = len(laberinto)
    c_largo = len(laberinto[0])+1
    c_list = (c_ancho, c_largo)

    # Dimensiones del laberinto (ancho y alto)
    ANCHO, ALTO = calcular_alto_ancho(cuadrado,separacion,proporcion, c_list)
    ancho_alto = (ANCHO, ALTO)

    return c_list, ancho_alto


def preguntar_para_crear_mapa(pantalla,MEDIDAS,fuente_menus,menu_estado):
    ANCHO, ALTO = MEDIDAS
    pantalla.fill(NEGRO)
    while True:
        imprimir_menu(ALTO,ANCHO, pantalla, fuente_menus,menu_estado)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if (menu_estado == 2):
                if(event.type == pygame.KEYDOWN):
                    if event.key == pygame.K_1:
                        print("Cargando mapa")
                        return crear_laberinto([],"")
                    elif event.key == pygame.K_2:
                        print("Crear mapa desde cero")
                        laberinto_en_blanco = crear_lab_blanco(15,15)
                        return crear_laberinto(laberinto_en_blanco,"")
                    elif event.key == pygame.K_ESCAPE:
                        print("regresando al inicio")
                        return 0
            if (menu_estado == 3):
                if(event.type == pygame.KEYDOWN):
                    if event.key == pygame.K_1:
                        print("Comenzar el juego")
                        return 2
                    elif event.key == pygame.K_2:
                        print("Guardando el mapa")
                        '''
                            codigo para guardar el mapa
                        '''
                    elif event.key == pygame.K_3:
                        print("regresando al inicio")
                        return 0
                    elif event.key == pygame.K_ESCAPE:
                        print("Saliendo del juego, nos vemos")
                        pygame.quit()
                        sys.exit()
        pygame.display.flip()

def descubrir_malla(malla_oculta,x,y):
    
    filas = len(malla_oculta)
    columnas = len(malla_oculta[0])
# Coordenadas (x, y) en las que deseas establecer unos

    # Establecer unos en los extremos de la malla_oculta en función de las coordenadas (x, y)
    if 0 <= x < columnas and 0 <= y < filas:
        malla_oculta[y][x] = 1
        if x > 0:
            malla_oculta[y][x - 1] = 1
        if x < columnas - 1:
            malla_oculta[y][x + 1] = 1
        if y > 0:
            malla_oculta[y - 1][x] = 1
        if y < filas - 1:
            malla_oculta[y + 1][x] = 1

        # Extremos superiores
        if y > 0:
            malla_oculta[y - 1][x] = 1
            if x > 0:
                malla_oculta[y - 1][x - 1] = 1
            if x < columnas - 1:
                malla_oculta[y - 1][x + 1] = 1

        # Extremos inferiores
        if y < filas - 1:
            malla_oculta[y + 1][x] = 1
            if x > 0:
                malla_oculta[y + 1][x - 1] = 1
            if x < columnas - 1:
                malla_oculta[y + 1][x + 1] = 1
