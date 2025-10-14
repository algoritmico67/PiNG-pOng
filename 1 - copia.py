import pygame
from pygame import * 
from random import randint
back = (200, 255, 255)
win_width = 600
win_height = 500
window = display.set_mode((win_width, win_height))
window.fill(back)

game = True
finish = False
clock = time.Clock()
FPS = 60
speed_y = 3
speed_x = 3
display.set_caption('Ping Pong')
font.init()
font = font.Font(None, 35)
scoretext1 = font.render('el jugador1 anota', True, (180, 0, 0))
scoretext2 = font.render('el jugador2 anota', True, (180, 0, 0))                        
lose1 = font.render('PLAYER 1 LOSES', True, (180, 0, 0))
lose2 = font.render('PLAYER 2 LOSES', True, (180, 0, 0))
score1=0
score2=0
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, width, height):
        self.image = transform.scale(image.load(player_image), (width, height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

def reset_ball(direction=1):
    global speed_x, speed_y
    ball.rect.x = win_width // 2 - ball.rect.width // 2
    ball.rect.y = win_height// 2 - ball.rect.height // 2
    speed_x = 5 * direction
    speed_y = randint(-4, 4)
    if speed_y == 0:
        speed_y = 3

class Player(GameSprite):
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 80:
            self.rect.y += self.speed

 
ball = GameSprite('pelota.png', 200, 200, 4, 50, 50)
bar = Player('descarga.png', 50, 300, 4, 30, 170)
bar2 = Player('descarga.png', 500, 300, 4, 30, 170)

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if finish != True:
        window.fill(back)
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        bar.update_l()
        bar2.update_r()
        if ball.rect.y > win_height-50 or ball.rect.y < 0:
            speed_y *= -1
        if sprite.collide_rect(bar, ball):
            if speed_x < 0:
                speed_x *= -1
                ball.rect.left = bar.rect.right
        if sprite.collide_rect(bar2, ball):
            if speed_x > 0:
                speed_x *= -1
                ball.rect.right = bar2.rect.left
        if ball.rect.x < 0:
            score2 +=1
            finish = True
            window.blit(scoretext1, (200, 200))
        if ball.rect.x > win_width:
            score1 +=1
            finish = True
            window.blit(scoretext2, (200, 200))
        ball.reset()
        bar.reset()
        bar2.reset()
        score_display = font.render(f'{score1}    :    {score2}', True, (50, 50, 50))
        window.blit(score_display, (win_width // 2 - 60, 20))
    else:
        display.update()
        time.delay(2000)
        finish = False
        direction = 1 if ball.rect.x > win_width // 2 else -1
        reset_ball(direction)
    display.update()
    clock.tick(FPS)