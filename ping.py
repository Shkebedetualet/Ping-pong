from pygame import *
from random import randint
mixer.init()
font.init()

window = display.set_mode((1000,700))
background = transform.scale(image.load('фон.jpg'),(1000,800))
finish = False
game = True

class GameSprite(sprite.Sprite):
    def __init__(self,player_image,player_x,player_y,player_speed,shir,vis):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(shir,vis))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
    
class Player(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < 400:
            self.rect.y += self.speed
    def update2(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < 800:
            self.rect.y += self.speed

player1 = Player('ракетка.png',10,100,20,200,300)








while game: 
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        window.blit(background,(0,0))
        player1.reset()
        player1.update()
        display.update()
    time.delay(1)
