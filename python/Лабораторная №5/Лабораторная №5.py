# Лысцев Никита ИУ7-23Б
# Анимация

import pygame
import random

y1 = 0
size = 1200, 675
pygame.init()  # инициализация экрана
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Анимация с дождиком, пацаном и машинкой")
img = pygame.image.load("bg.jpg")
screen.blit(img, (0, 0))
icon = pygame.image.load("doctor.png")
pygame.display.set_icon(icon)

numbers = 300
colors = [0] * numbers
location_x = [0] * numbers
location_y = [0] * numbers
sizes = [0] * numbers
speed = [0] * numbers
# Инициализировать дождевые капли радуги
for i in range(numbers):
    colors[i] = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
    # colors[i] = 255, 255, 255
    location_x[i] = random.randint(0, size[0])
    location_y[i] = -random.randint(0, size[1])
    sizes[i] = random.randint(5, 20)
    speed[i] = random.randint(1, 5)

run_list = [pygame.image.load("0.gif"),
            pygame.image.load("1.gif"),
            pygame.image.load("2.gif"),
            pygame.image.load("3.gif"),
            pygame.image.load("4.gif"),
            pygame.image.load("5.gif"),
            pygame.image.load("6.gif"),
            pygame.image.load("7.gif")]

car_left_list = [pygame.image.load("car0.gif"),
                 pygame.image.load("car1.gif"),
                 pygame.image.load("car2.gif"),
                 pygame.image.load("car3.gif"),
                 pygame.image.load("car4.gif"),
                 pygame.image.load("car5.gif")]
car_right_list = [pygame.image.load("rcar0.gif"),
                  pygame.image.load("rcar1.gif"),
                  pygame.image.load("rcar2.gif"),
                  pygame.image.load("rcar3.gif"),
                  pygame.image.load("rcar4.gif"),
                  pygame.image.load("rcar5.gif")]

car_width, car_height = car_left_list[0].get_size()
hero_width, hero_height = car_left_list[0].get_size()
x, y = 0, 400
direct_car_x = 6
x_hero = 0
direct_hero_x = 15
RED = 255, 0, 0  # цвет текста
GREEN = 0, 255, 0  # цвет фона
BLUE = 0, 0, 255
BLACK = 0, 0, 0

FPS = 60
clock = pygame.time.Clock()  # задаем fps
k = 0
j = 0
flag = True
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
    screen.blit(img, (0, 0))
    if flag:
        screen.blit(car_left_list[j], (x, y))
    else:
        screen.blit(car_right_list[j], (x, y))
    screen.blit(run_list[k], (x_hero, 400))

    x += direct_car_x
    if x + car_width >= size[0]:  # меняем направление
        direct_car_x = -direct_car_x
        flag = False
    if x < 0:
        direct_car_x = -direct_car_x
        flag = True

    x_hero += direct_hero_x
    if x_hero >= size[0]:  # меняем направление
        x_hero = -hero_height

    k += 1
    if k >= 7:
        k = 0
    j += 1
    if j >= 5:
        j = 0

    for i in range(numbers):
        pygame.draw.circle(screen, colors[i], (location_x[i], location_y[i]),
                           sizes[i])  # Давайте дождем рисовать капли на экране
        location_y[i] = location_y[i] + speed[i]  # ， направление оси y

        if location_y[i] > size[1]:  # Если капли дождя падают невидимо, это выше высоты экрана
            location_y[i] -= size[1]  # Сбросить параметры дождевой капли
            location_x[i] = random.randint(0, size[0])
            speed[i] = random.randint(1, 5)
    clock.tick(30)  # таймер срабатывает 100 раз в секунду, поэтому частота кадров составляет 100 кадров в секунду
    pygame.display.update()
