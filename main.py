#pegar codigo de actividad uno
import pygame
import sys

#inicio
pygame.init()

#Configuracion de la pantalla
ANCHO = 800
ALTO = 600
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Ejemplo de Colisiones en Pygame")

#Definir Colores (R, G, B)
BLANCO = (255, 255, 255)
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)
VERDE = (0, 255, 0)

#spawn del jugador
jugador = pygame.Rect(100, 250, 50, 50)
velocidad = 5

# meta
meta = pygame.Rect(500, 250, 60, 60)
reloj = pygame.time.Clock()

#Bucle principal del juego
ejecutando = True
while ejecutando:
    
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False

    #asignacion de teclas WASD
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_a]:
        jugador.x -= velocidad
    if teclas[pygame.K_d]:
        jugador.x += velocidad
    if teclas[pygame.K_w]:
        jugador.y -= velocidad
    if teclas[pygame.K_s]:
        jugador.y += velocidad

    color_jugador = AZUL
    
    if jugador.colliderect(meta):
        #cuando se llegue a la meta el jugador se vuelve verde
        color_jugador = VERDE

    #fondo de pantalla en blanco
    pantalla.fill(BLANCO) # Limpiar pantalla con fondo blanco
    
    #meta
    pygame.draw.rect(pantalla, ROJO, meta)
    
    #generacion de o dibujo del jugador segun lo que suceda y actualizacion de pantalla
    pygame.draw.rect(pantalla, color_jugador, jugador)
    pygame.display.flip()

    #FPS 
    reloj.tick(60)

#fin
pygame.quit()
sys.exit()





