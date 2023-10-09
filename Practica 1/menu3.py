from functions import *
pygame.init()

# Configuración de la pantalla
ANCHO, ALTO = 800, 600
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Maze Runner")
laberinto =[]

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
ESTADO_MAPA = 3
ESTADO_CREAR_MAPA = 4
ESTADO_OPCIONES = 5
ESTADO_SECRETO = 6
estado_actual = ESTADO_INICIO

# Bucle principal
reloj = pygame.time.Clock()

mostrar_mensaje = True
tiempo_anterior = pygame.time.get_ticks()
intervalo_parpadeo = 500  # Intervalo de parpadeo en milisegundos

while True:
    pantalla.fill(NEGRO)
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
                        estado_actual = ESTADO_MAPA
                    elif event.key == pygame.K_3:
                        print("Crear mapa nuevo")
                        estado_actual = ESTADO_CREAR_MAPA
                    elif event.key == pygame.K_4:
                        print("Ver opciones")
                        estado_actual = ESTADO_CREAR_MAPA
                    elif event.key == pygame.K_5:
                        pygame.quit()
                        sys.exit()
                    elif event.key == pygame.K_6:
                        print("Juego secreto")
                        estado_actual = ESTADO_SECRETO

    # Lógica de parpadeo del mensaje
    
    tiempo_actual = pygame.time.get_ticks()
    if(estado_actual == ESTADO_INICIO):
        if tiempo_actual - tiempo_anterior >= intervalo_parpadeo:
            mostrar_mensaje = not mostrar_mensaje
            tiempo_anterior = tiempo_actual
        if mostrar_mensaje:
            mensaje = "Presiona cualquier tecla para comenzar"
            texto = fuente_menus.render(mensaje, True, VERDE)
            pantalla.blit(texto, (ANCHO // 2 - texto.get_width() // 2, ALTO // 1 - texto.get_height() // 0.5))

    elif estado_actual == ESTADO_MENU:
        imprimir_menu(ALTO,ANCHO,pantalla,fuente_menus)

    elif estado_actual == ESTADO_SECRETO:
        # Lógica y dibujo del juego
        pygame.mouse.set_visible(0)
        pantalla.fill(BLANCO)
        mouse_pos = pygame.mouse.get_pos()
        x = mouse_pos[0]
        y = mouse_pos[1]
        pygame.draw.rect(pantalla,VERDE,(x,y,100,100))
    elif estado_actual == ESTADO_MAPA:
        laberinto = crear_laberinto(laberinto)
        estado_actual = ESTADO_JUEGO
    #elif estado_actual == ESTADO_CREAR_MAPA:


    pygame.display.flip()
    reloj.tick(60)
