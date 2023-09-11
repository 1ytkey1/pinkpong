from typing import Any
from pygame import*
init()

W = 800
H = 500

window = display.set_mode((W, H))
display.set_caption('Pingpong')
display.set_icon(image.load('tenis_ball.png'))

back = (200, 69, 20)

font.init()
f1 = font.SysFont(None, 70, bold=True)
f2 = font.SysFont(None, 50)

class GameSprite(sprite.Sprite):
    # конструктор класу
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        # викликаємо конструктор класу (Sprite):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y)) # створюємо картинку
        self.size_x = size_x
        self.size_y = size_y
        self.speed = player_speed
        self.rect = self.image.get_rect() # повертає прямокутник під картинкою
        self.rect.x = player_x
        self.rect.y = player_y
    
    def reset(self):
       window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):

    def update_l(self):
        key_pressed = key.get_pressed()
        if key_pressed[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if key_pressed[K_s] and self.rect.y < H-self.size_y:
            self.rect.y += self.speed

    def update_r(self):
        key_pressed = key.get_pressed()
        if key_pressed[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        if key_pressed[K_DOWN] and self.rect.y < H-self.size_y:
            self.rect.y += self.speed

racket1 = Player('racket.png', 15, H/4, 50, 150, 5)
racket2 = Player('racket.png', W-65, H/2, 50, 150, 5)
ball = GameSprite('tenis_ball.png', W/2, H/2, 50, 50, 6)

finish = False
game = True
speed_x = 4
speed_y = 4

while game:
    window.fill(back)
    time.delay(5)
    for e in event.get():
        if e.type == QUIT:
            game = False
    if not finish:
        racket1.reset()
        racket2.reset()
        racket1.update_l()
        racket2.update_r()
        ball.reset()
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        if ball.rect.y <= 0:
            speed_y *= -1
        if ball.rect.y >= H-50:
            speed_y *= -1
        if sprite.collide_rect(racket1, ball):
            speed_x *= -1
        if sprite.collide_rect(racket2, ball):
            speed_x *= -1  
        if ball.rect.x <= 0:
            ball.rect.x = W/2
            ball.rect.y = H/2
        if ball.rect.x >= W-50:
            ball.rect.x = W/2
            ball.rect.y = H/2

    display.update() 