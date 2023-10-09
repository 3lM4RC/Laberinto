import pygame
import sys

pygame.init()

# Configuración de la pantalla
ANCHO, ALTO = 800, 600
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Mi Juego")

# Colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
VERDE = (0, 255, 0)
AZUL = (0, 255, 255)
AMARILLO = (255, 255, 0)

# Fuente para el texto
fuente_menus = pygame.font.Font("C:/Windows/Fonts/arial.ttf", 20)

# Estados del juego
ESTADO_INICIO = 0
ESTADO_MENU = 1
ESTADO_JUEGO = 2
estado_actual = ESTADO_INICIO

# Bucle principal
reloj = pygame.time.Clock()

mostrar_mensaje = True
tiempo_anterior = pygame.time.get_ticks()
intervalo_parpadeo = 500  # Intervalo de parpadeo en milisegundos

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif (event.type == pygame.KEYDOWN)or(event.type == pygame.MOUSEBUTTONDOWN):
            if estado_actual == ESTADO_INICIO:
                estado_actual = ESTADO_MENU
            elif estado_actual == ESTADO_MENU:
                if(event.type == pygame.KEYDOWN):
                    if event.key == pygame.K_1:
                        print("Comenzar el juego")
                        estado_actual = ESTADO_JUEGO
                    elif event.key == pygame.K_2:
                        print("Cargar un mapa")
                    elif event.key == pygame.K_3:
                        print("Crear mapa nuevo")
                    elif event.key == pygame.K_4:
                        print("Ver opciones")
                    elif event.key == pygame.K_5:
                        pygame.quit()
                        sys.exit()

    pantalla.fill(NEGRO)

    # Lógica de parpadeo del mensaje
    tiempo_actual = pygame.time.get_ticks()
    if tiempo_actual - tiempo_anterior >= intervalo_parpadeo:
        mostrar_mensaje = not mostrar_mensaje
        tiempo_anterior = tiempo_actual

    if mostrar_mensaje and (estado_actual == ESTADO_INICIO):
        mensaje = "Presiona cualquier tecla para comenzar"
        texto = fuente_menus.render(mensaje, True, VERDE)
        pantalla.blit(texto, (ANCHO // 2 - texto.get_width() // 2, ALTO // 2 - texto.get_height() // 2))

    elif estado_actual == ESTADO_MENU:
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

    elif estado_actual == ESTADO_JUEGO:
        # Lógica y dibujo del juego
        pygame.mouse.set_visible(0)
        pantalla.fill(BLANCO)
        mouse_pos = pygame.mouse.get_pos()
        x = mouse_pos[0]
        y = mouse_pos[1]
        pygame.draw.rect(pantalla,VERDE,(x,y,100,100))
    pygame.display.flip()
    reloj.tick(60)
