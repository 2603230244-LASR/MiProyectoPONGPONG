#subir actividad 2
#Luis Alberto Soto Rubio
import pygame

#Configuración inicial
pygame.init()
ANCHO, ALTO = 1000, 700
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("PongPong")
reloj = pygame.time.Clock()
fuente = pygame.font.Font(None, 60)
fuente_titulo = pygame.font.Font(None, 150)
fuente_pequena = pygame.font.Font(None, 40)


#Función para escribir texto centrado en la pantalla
def texto_centrado(texto, fuente_usada, color, y):
    imagen = fuente_usada.render(texto, True, color)
    rectangulo = imagen.get_rect(center=(ANCHO // 2, y))
    pantalla.blit(imagen, rectangulo)


#Objetos del juego
jugador = pygame.Rect(30, ALTO // 2 - 50, 15, 100)
rival = pygame.Rect(ANCHO - 45, ALTO // 2 - 50, 15, 100)
pelota = pygame.Rect(ANCHO // 2 - 10, ALTO // 2 - 10, 20, 20)

#Velocidades
velocidad_jugador = 7
velocidad_rival = 7
vel_pelota_x = 8
vel_pelota_y = 8

#Marcador
puntos_jugador = 0
puntos_rival = 0
PUNTOS_PARA_GANAR = 10  

#Quién ganó 
ganador = ""
color_ganador = (255, 255, 255)

#Estado del juego: "inicio", "jugando", "pausa" o "fin"
estado = "inicio"

#Bucle principal
corriendo = True
while corriendo:

    #Eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False

        #Teclas que se presionan una sola vez
        if evento.type == pygame.KEYDOWN:
            if estado == "inicio" and evento.key == pygame.K_SPACE:
                estado = "jugando"
            elif estado == "jugando" and evento.key == pygame.K_p:
                estado = "pausa"
            elif estado == "pausa" and evento.key == pygame.K_p:
                estado = "jugando"
            elif estado == "fin" and evento.key == pygame.K_SPACE:
                #Reiniciar la partida
                puntos_jugador = 0
                puntos_rival = 0
                pelota.center = (ANCHO // 2, ALTO // 2)
                jugador.centery = ALTO // 2
                rival.centery = ALTO // 2
                estado = "jugando"

    #Lógica del juego solo si estamos jugando
    if estado == "jugando":
        teclas = pygame.key.get_pressed()

        #Movimiento del jugador
        if teclas[pygame.K_w]:
            jugador.y -= velocidad_jugador
        if teclas[pygame.K_s]:
            jugador.y += velocidad_jugador
        jugador.clamp_ip(pantalla.get_rect())

        #Movimiento del rival
        if teclas[pygame.K_UP]:
            rival.y -= velocidad_rival
        if teclas[pygame.K_DOWN]:
            rival.y += velocidad_rival
        rival.clamp_ip(pantalla.get_rect())

        #Movimiento de la pelota
        pelota.x += vel_pelota_x
        pelota.y += vel_pelota_y

        #Rebote arriba y abajo
        if pelota.top <= 0 or pelota.bottom >= ALTO:
            vel_pelota_y *= -1

        #Rebote en las paletas
        if pelota.colliderect(jugador) and vel_pelota_x < 0:
            vel_pelota_x *= -1
        if pelota.colliderect(rival) and vel_pelota_x > 0:
            vel_pelota_x *= -1

        #Puntos: si la pelota sale por un lado
        if pelota.left <= 0:
            puntos_rival += 1
            pelota.center = (ANCHO // 2, ALTO // 2)
            vel_pelota_x *= -1
        if pelota.right >= ANCHO:
            puntos_jugador += 1
            pelota.center = (ANCHO // 2, ALTO // 2)
            vel_pelota_x *= -1

        #Revisar si alguien llegó al límite de puntos
        if puntos_jugador >= PUNTOS_PARA_GANAR:
            ganador = "Jugador 1"
            color_ganador = (255, 0, 0)
            estado = "fin"
        elif puntos_rival >= PUNTOS_PARA_GANAR:
            ganador = "Jugador 2"
            color_ganador = (0, 0, 255)
            estado = "fin"

    #Dibujar
    pantalla.fill((0, 0, 0))

    if estado == "inicio":
        #Pantalla de inicio
        texto_centrado("PongPong", fuente_titulo, (255, 255, 255), 200)
        texto_centrado("Jugador 1", fuente_pequena, (255, 0, 0), 340)
        texto_centrado("Jugador 2", fuente_pequena, (0, 0, 255), 390)
        texto_centrado("Pausa: P", fuente_pequena, (200, 200, 200), 440)
        texto_centrado("Presiona ESPACIO para empezar", fuente, (255, 255, 255), 280)

    else:
        #Juego
        pygame.draw.rect(pantalla, (255, 0, 0), jugador)
        pygame.draw.rect(pantalla, (0, 0, 255), rival)
        pygame.draw.ellipse(pantalla, (255, 255, 255), pelota)
        pygame.draw.line(pantalla, (100, 100, 100), (ANCHO // 2, 0), (ANCHO // 2, ALTO))

        texto_j = fuente.render(str(puntos_jugador), True, (255, 0, 0))
        texto_r = fuente.render(str(puntos_rival), True, (0, 0, 255))
        pantalla.blit(texto_j, (ANCHO // 4, 20))
        pantalla.blit(texto_r, (ANCHO * 3 // 4, 20))

        if estado == "pausa":
            #Capa oscura
            capa = pygame.Surface((ANCHO, ALTO), pygame.SRCALPHA)
            capa.fill((0, 0, 0, 150))
            pantalla.blit(capa, (0, 0))
            texto_centrado("PAUSA", fuente_titulo, (255, 255, 255), ALTO // 2 - 30)
            texto_centrado("Presiona P para continuar", fuente_pequena, (255, 255, 0), ALTO // 2 + 50)

        if estado == "fin":
            #Capa oscura y mensaje del ganador
            capa = pygame.Surface((ANCHO, ALTO), pygame.SRCALPHA)
            capa.fill((0, 0, 0, 180))
            pantalla.blit(capa, (0, 0))
            texto_centrado("¡Ganaste!", fuente_titulo, (255, 255, 255), ALTO // 2 - 80)
            texto_centrado(ganador, fuente_titulo, color_ganador, ALTO // 2 + 40)
            texto_centrado("Presiona ESPACIO para jugar otra vez", fuente_pequena, (255, 255, 0), ALTO // 2 + 140)

    pygame.display.flip()
    reloj.tick(60)