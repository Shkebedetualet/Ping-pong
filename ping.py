from pygame import *
mixer.init()
font.init()

window = display.set_mode((1000,700))
display.set_caption('Ping')
background = transform.scale(image.load('фон.jpg'),(1000,800))
finish = False
game = True
while game: 
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        window.blit(background,(0,0))
        display.update()
    time.delay(40)