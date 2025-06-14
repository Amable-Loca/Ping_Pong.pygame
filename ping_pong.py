from pygame import *
init()
font.init()

ANCHO, ALTO = 753, 553
COLOR_FONDO = (179, 224, 230)
BLANCO = (255, 255, 255)
FPS = 120
PLAYER_IMG = 'racket.png'
PELOTA = 'pelota.png'
FUENTE = 'Pixelcraft.ttf'

screen = display.set_mode((ANCHO, ALTO))
display.set_caption('PING_PONG')

font_1 = font.Font(FUENTE, 50)

class GameSprite(sprite.Sprite):
    def __init__(self,img ,cor_x, cor_y, width, height , speed=0):
        super().__init__()
        self.width = width
        self.height = height
        self.image = transform.scale(image.load(img), (self.width, self.height))
        self.rect = self.image.get_rect()
        self.rect.x = cor_x
        self.rect.y = cor_y
        self.speed = speed

    def reset(self):
        screen.blit(self.image, (self.rect.x, self.rect.y))

        
class Player(GameSprite):
    def update_1(self):
        llaves = key.get_pressed()
        if llaves[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed

        if llaves[K_s] and self.rect.y < ALTO - self.height:
            self.rect.y += self.speed

    def update_2(self):
        llaves = key.get_pressed()
        if llaves[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed

        if llaves[K_DOWN] and self.rect.y < ALTO - self.height:
            self.rect.y += self.speed


player_1 = Player(PLAYER_IMG, 5, 250, 30, 100, 5)
player_2 = Player(PLAYER_IMG, 715, 250, 30, 100, 5)
pelota = GameSprite(PELOTA, 50, 50, 40, 40, 1)

speed_x, speed_y = 5, 5


clok = time.Clock()
finish = False
run = True
while run:
    for e in event.get():
        if e.type == QUIT:
            run = False 

    if not finish:
        screen.fill(COLOR_FONDO)
        player_1.reset()
        player_1.update_1()
        player_2.reset()
        player_2.update_2()
        pelota.reset()

        pelota.rect.x += speed_x
        pelota.rect.y += speed_y

        if pelota.rect.y >= ALTO - pelota.height:
            speed_y *= -1
        if pelota.rect.y <= 0:
            speed_y *= -1
        if sprite.collide_rect(pelota, player_1):
            speed_x *= -1
        if sprite.collide_rect(pelota, player_2):
            speed_x *= -1
        

        if pelota.rect.x > ANCHO:
            win_p1 = font_1.render('GANADOR JUGADOR 1', 1, BLANCO)
            screen.blit(win_p1, (100, 250))
            finish = True
   
        if pelota.rect.x <= -50:
            win_p2 = font_1.render('GANADOR JUGADOR 2', 1, BLANCO)
            screen.blit(win_p2, (100, 250))
            finish = True
   
    display.update()
    clok.tick(FPS)

quit()
