from pygame import *
init()

ANCHO, ALTO = 753, 553
COLOR_FONDO = (179, 224, 230)
FPS = 120
PLAYER_IMG = 'racket.png'

screen = display.set_mode((ANCHO, ALTO))
display.set_caption('PING_PONG') 

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


player_1 = Player(PLAYER_IMG, 5, 250, 30, 80, 5)

clok = time.Clock()
finish = False
run = True
while run:
    for e in event.get():
        if e.type == QUIT:
            run = False 

    screen.fill(COLOR_FONDO)
    player_1.reset()
    player_1.update_1()
          
    display.update()
    clok.tick(FPS)

quit()