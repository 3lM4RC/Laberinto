import pygame
import sys

pygame.init()

# Configuración de la pantalla
ANCHO, ALTO = 800, 600
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Maze Runner")

# Colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
VERDE = (0, 255, 0)

# Fuente para el texto
fuente = pygame.font.Font(None, 36)

# Estados del juego
ESTADO_INICIO = 0
ESTADO_MENU = 1
ESTADO_JUEGO = 2
estado_actual = ESTADO_INICIO

# Bucle principal
reloj = pygame.time.Clock()
mostrar_mensaje = True
tiempo_anterior = pygame.time.get_ticks()
intervalo_parpadeo = 600

pygame.mouse.set_visible(0)
while True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if estado_actual == ESTADO_INICIO:
                estado_actual = ESTADO_MENU
            elif estado_actual == ESTADO_MENU:
                if event.key == pygame.K_1:
                    print("Comenzar el juego")
                    estado_actual = ESTADO_JUEGO
                elif event.key == pygame.K_2:
                    print("Ver opciones")
                elif event.key == pygame.K_3:
                    pygame.quit()
                    sys.exit()
            #elif event.type == ESTADO_JUEGO:
                # Lógica del juego

        pantalla.fill(BLANCO)        
        #ZONA DE JUEGOS

        if estado_actual == ESTADO_MENU:
            mensaje1 = "1. Comenzar juego"
            mensaje2 = "2. Ver opciones"
            mensaje3 = "3. Salir del juego"
            texto1 = fuente.render(mensaje1, True, NEGRO)
            texto2 = fuente.render(mensaje2, True, NEGRO)
            texto3 = fuente.render(mensaje3, True, NEGRO)
            pantalla.blit(texto1, (ANCHO // 2 - texto1.get_width() // 2, 200))
            pantalla.blit(texto2, (ANCHO // 2 - texto2.get_width() // 2, 300))
            pantalla.blit(texto3, (ANCHO // 2 - texto3.get_width() // 2, 400))

        elif estado_actual == ESTADO_JUEGO:
            # Lógica y dibujo del juego
            pantalla.fill(NEGRO)
            mouse_pos = pygame.mouse.get_pos()
            x = mouse_pos[0]
            y = mouse_pos[1]
            pygame.draw.rect(pantalla,VERDE,(x,y,100,100))
    tiempo_actual = pygame.time.get_ticks()
    if tiempo_actual - tiempo_anterior >= intervalo_parpadeo:
            mostrar_mensaje = not mostrar_mensaje
            tiempo_anterior = tiempo_actual
    if mostrar_mensaje and ((estado_actual == ESTADO_INICIO)or(estado_actual == ESTADO_MENU)):
            mensaje = "Presiona cualquier tecla para comenzar"
            texto = fuente.render(mensaje, True, NEGRO)
            pantalla.blit(texto, (ANCHO // 2 - texto.get_width() // 2, ALTO // 2 - texto.get_height() // 2))
        
        
        
    pygame.display.flip()
    reloj.tick(60)