from pygame import *


GREEN = (0, 255, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
YELLOW = (239, 228, 176)
LIME = (204, 255, 0)

init()

backgroud = transform.scale(image.load('media/table.png'), (700, 500))

clock = time.Clock()
FPS = 60

W = 700
H = 500

x1 = 50
y1 = 250

x2 = 550
y2 = 250


class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, player_weight, player_height):
        super().__init__()
        self.weight = player_weight
        self.height = player_height
        self.image = transform.scale(image.load(player_image), (self.weight, self.height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def colliderect(self, sprite1):
        return self.rect.colliderect(sprite1.rect)

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

    def collidepoint(self, x, y):
        return self.rect.collidepoint(x, y)


speed = 5

platforms = list()
losser = None

start_time = 0
now_time = 0

speed_x = -3
speed_y = 3

score1 = 0
score2 = 0

total_time = None
total_winner = None

window = display.set_mode((W, H))
display.set_caption('Ping-Pong(Игра до трёх очков)')

ball = GameSprite('media/ping_pong.png', 250, 250, 6, 50, 50)
platform1 = GameSprite('media/platform.png', 170, 350, 5, 30, 100)
platform2 = GameSprite('media/platform.png', 500, 50, 5, 30, 100)

w = font.SysFont('Arial', 25)
total = font.SysFont('Arial', 40)

lose_text = w.render(losser, 1, RED)
player_score1 = w.render('СЧЕТ ПЕРВОГО ИГРОКА:' + str(score1), 1, LIME)
player_score2 = w.render('СЧЕТ ВТОРОГО ИГРОКА:' + str(score2), 1, LIME)
times = w.render(total_time, 1, RED)
winner = total.render(total_winner, 1, YELLOW)

pos = lose_text.get_rect(center=(W//2-100, H//2))
pos2 = player_score1.get_rect(center=(160, 50))
pos3 = player_score2.get_rect(center=(530, 50))
pos4 = times.get_rect(center=(W//2, H//2+100))
pos5 = winner.get_rect(center=(W//2-200, H//2))

platforms.append(platform1)
platforms.append(platform2)

from time import *
a = True
b = True
while a:
    for e in event.get():
        if e.type == QUIT:
            exit()
    while b:
        now_time = time()
        if now_time - start_time >= 3:
            ball.rect.x += speed_x
            ball.rect.y += speed_y
            lose_text = w.render(None, 1, RED)
            times = w.render(None, 1, RED)

        else:
            times = w.render(str(round(now_time - start_time, 1)), 1, RED)
            window.blit(times, pos4)
        window.blit(backgroud, (0, 0))

        for e in event.get():
            if e.type == QUIT:
                exit()
        key_pressed = key.get_pressed()

        if key_pressed[K_UP] and platform2.rect.y > 5:
            platform2.rect.y -= speed
        if key_pressed[K_DOWN] and platform2.rect.y < 400:
            platform2.rect.y += speed

        if key_pressed[K_w] and platform1.rect.y > 5:
            platform1.rect.y -= speed
        if key_pressed[K_s] and platform1.rect.y < 400:
            platform1.rect.y += speed

        if ball.colliderect(platform1):
            speed_x *= -1
            losser = 'Партию проиграл игрок 2!'
        elif ball.colliderect(platform2):
            speed_x *= -1
            losser = 'Партию проиграл игрок 1!'
        elif ball.rect.x >= 650:
            speed_x *= -1
        elif ball.rect.x <= 5:
            speed_x *= -1
        elif ball.rect.y <= 5:
            speed_y *= -1
        elif ball.rect.y >= 450:
            speed_y *= -1

        if ball.rect.x <= 100 or ball.rect.x >= 510:
            lose_text = w.render(losser, 1, RED)
            start_time = time()
            if losser == 'Проиграл игрок 2!':
                score1 += 1
            elif losser == 'Проиграл игрок 1!':
                score2 += 1
            ball.rect.x = 250

        if score1 >= 3:
            lose_text = w.render(None, 1, RED)
            winner = total.render('ПОБЕДИЛ ИГРОК 1', 1, RED)
        elif score2 >= 3:
            lose_text = w.render(None, 1, RED)
            winner = total.render('ПОБЕДИЛ ИГРОК 2', 1, RED)

        player_score1 = w.render('СЧЕТ ПЕРВОГО ИГРОКА:' + str(score1), 1, LIME)
        player_score2 = w.render('СЧЕТ ВТОРОГО ИГРОКА:' + str(score2), 1, LIME)
        window.blit(times, pos4)
        window.blit(lose_text, pos)
        window.blit(winner, pos5)
        window.blit(player_score1, pos2)
        window.blit(player_score2, pos3)
        platform2.reset()
        platform1.reset()
        ball.reset()
        clock.tick(FPS)
        display.update()
        if score1 >= 3:
            b = False
        elif score2 >= 3:
            b = False
            print(123)
display.update()