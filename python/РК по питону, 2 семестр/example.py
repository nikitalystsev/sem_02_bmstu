import pygame as pg
from math import pi, radians, sin

red = 255, 0, 0
orange = 255, 127, 0
yellow = 255, 255, 0
green = 0, 255, 0
blue = 0, 0, 255
bordov = 75, 0, 130
violet = 143, 0, 255
cyan = 102, 205, 170
magenta = 255, 0, 255


def draw_circle():
    pg.draw.arc(root, red, (x, y, 100, 100), 0 + angle, pi / 4 + angle, 100)
    pg.draw.arc(root, yellow, (x, y, 100, 100), pi / 4 + angle, pi / 2 + angle, 100)
    pg.draw.arc(root, green, (x, y, 100, 100), pi / 2 + angle, 3 * pi / 4 + angle, 100)
    pg.draw.arc(root, blue, (x, y, 100, 100), 3 * pi / 4 + angle, pi + angle, 100)
    pg.draw.arc(root, red, (x, y, 100, 100), pi + angle, 5 * pi / 4 + angle, 100)
    pg.draw.arc(root, yellow, (x, y, 100, 100), 5 * pi / 4 + angle, 3 * pi / 2 + angle, 100)
    pg.draw.arc(root, green, (x, y, 100, 100), 3 * pi / 2 + angle, 7 * pi / 4 + angle, 100)
    pg.draw.arc(root, blue, (x, y, 100, 100), 7 * pi / 4 + angle, 2 * pi + angle, 100)


pg.init()
root = pg.display.set_mode((400, 600))
clock = pg.time.Clock()

fi = 5
fi = radians(fi)

x, y = 400 // 2, 600 // 2
flag = True
angle = 0
FPS = 100
while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            quit()

    pg.draw.rect(root, magenta, (0, 0, 400, 600))

    y = 250 + sin(x / 10) * 100

    if x >= 400 - 100:
        flag = False
    if x <= 0:
        flag = True
    if flag:
        x += 1
        angle -= fi
    else:
        x -= 1
        angle += fi

    y = int(y)

    draw_circle()

    pg.display.update()
    clock.tick(FPS)
