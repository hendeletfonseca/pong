from PPlay.window import *
from PPlay.gameimage import *
from PPlay.sprite import *

window = Window(960, 540)
window.set_title("pong")

clock = pygame.time.Clock()

teclado = Window.get_keyboard()

background = GameImage("./assets/background960-540.jpg")
ball = Sprite("./assets/ball.png")
ball_speed_x = -10
ball_speed_y = -10
ball.set_position(window.width/2 - ball.width/2, window.height/2 - ball.height/2)

bar = Sprite("./assets/bar.png")
bar.set_position(0 - bar.width/2, 0)

bar2 = Sprite("./assets/bar.png")
bar2.set_position(window.width - bar2.width/1.80, 0)
bar2_speed = 5

last_collision = 0

scoreboard = [0, 0]

ponto = 0
while True:
    clock.tick(30)

    ball.move_x(ball_speed_x)
    ball.move_y(ball_speed_y)

    if ball.y <= 0:
        ball_speed_y *= -1
    if ball.y >= window.height - ball.height/2:
        ball_speed_y *= -1
    if ball.x <= 0 - ball.width/2:
        scoreboard[1] += 1
        ball.set_position(0, bar.y + bar.width/3)
        ball_speed_x = 0
        ball_speed_y = 0
        ponto = 2
    if ball.x >= window.width - ball.width / 2:
        scoreboard[0] += 1
        ball.set_position(960 - ball.width, bar2.y + bar2.width/3)
        ball_speed_x = 0
        ball_speed_y = 0
        ponto = 1
    if teclado.key_pressed("W") and bar.y >= -180:
        bar.move_y(-10)
        if ball_speed_y == 0:
            ball.move_y(-10)
    if teclado.key_pressed("S") and bar.y <= window.height - bar.height/2 - 50:
        bar.move_y(10)
        if ball_speed_y == 0:
            ball.move_y(10)

    if ball.collided_perfect(bar) and last_collision != 1:
        ball_speed_y *= -1
        ball_speed_x *= -1
        last_collision = 1

    if ball.collided_perfect(bar2) and last_collision != 2:
        ball_speed_y *= -1
        ball_speed_x *= -1
        last_collision = 2

    if teclado.key_pressed("SPACE") and ball_speed_y == 0 and ball_speed_x == 0:
        if ponto == 1:
            last_collision = 1
            ball_speed_y = 10
            ball_speed_x = 10
        if ponto == 2:
            last_collision = 2
            ball_speed_y = -10
            ball_speed_x = -10

    if ball.y > bar2.y + bar2.height/2:
        bar2.move_y(5)
    elif ball.y < bar2.y + bar2.height/2:
        bar2.move_y(-5)

    background.draw()
    ball.draw()
    bar.draw()
    bar2.draw()
    window.draw_text(f'{scoreboard[0]}X{scoreboard[1]}', window.width/2, 0, size=20, color=(0, 0, 0), font_name="Arial", bold=True, italic=False)
    window.update()
