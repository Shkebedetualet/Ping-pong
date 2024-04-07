from pygame import *
from random import *
mixer.init()
font.init()

window = display.set_mode((1000,700))
background = transform.scale(image.load('фон.jpg'),(1000,800))
font4 = font.SysFont('Arial',80)
proigral_left = font4.render('Левый игрок проиграл!', True, (255,0,0))
proigral_right = font4.render('Правый игрок проиграл!', True, (0,222,255))
score1 = 0
score2 = 0
x = 3
y = 3
rx = [3,-3]
ry = [3,-3]
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
        if keys_pressed[K_DOWN] and self.rect.y < 400:
            self.rect.y += self.speed

player1 = Player('ракетка.png',10,100,5,200,300)
player2 = Player('ракетка.png',800,100,5,200,300)
ball = GameSprite('мяч.png',455,400,10,50,50)








while game: 
    for e in event.get():
        if e.type == QUIT:
            game = False
        elif e.type == KEYDOWN:
            if e.key == K_r:
                    if finish == True:
                        finish = False
                        score1 = 0
                        score2 = 0
                        ball.rect.x = 500
                        ball.rect.y = 400                   
    if finish != True:
        window.blit(background,(0,0))
        player1.reset()
        player1.update()
        ball.reset()
        player2.reset()
        player2.update2()
        text_score1 = font4.render(str(score1),True,(255,0,0))
        text_score2 = font4.render(str(score2),True,(255,0,0))
        window.blit(text_score1, (50, 50))
        window.blit(text_score2, (900, 50))
        ball.rect.x += x
        ball.rect.y += y
        if ball.rect.y < 0:
            y*=-1
        elif ball.rect.y > 650:
            y*=-1
        elif ball.rect.colliderect(player2.rect) or ball.rect.colliderect(player1.rect):
            x*= -1
        elif ball.rect.x < 0:
            score1+=1
            ball.rect.x = 500
            ball.rect.y = 400
            x = choice(rx)
            y = choice(ry)
        elif ball.rect.x > 900:
            score2+=1
            ball.rect.x = 500
            ball.rect.y = 400
            x = choice(rx)
            y = choice(ry)
        elif score1 == 5:
            finish = True
            window.blit(proigral_left,(170,300))
        elif score2 == 5:
            finish = True
            window.blit(proigral_right,(170,300))
        
           
        


        display.update()
    time.delay(1)
