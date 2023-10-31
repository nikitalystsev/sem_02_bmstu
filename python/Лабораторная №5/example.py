import pygame

size = 600, 400
pygame.init()  # инициализация экрана
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Моя программа")
img = pygame.image.load("creature (1).gif")
# pygame.display.set_icon(img)

font = pygame.font.SysFont("Arial", 32)
RED = (255, 0, 0)  # цвет текста
GREEN = (0, 255, 0)  # цвет фона
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

follow = font.render("подписка", 0, RED, GREEN)  # 1 - сглаживание
like = font.render("подписка", 1, GREEN, BLUE)
width, height = like.get_size()  # возвращает длину и ширину объекта
x, y = 32, 300
x2, y2 = 54, 0
direct_like_x = 1
direct_like_y = 1

direct_follow_x = 1
direct_follow_y = 1

FPS = 180
clock = pygame.time.Clock()  # задаем fps

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
    clock.tick(FPS)  # параметр - количество кадров, которое мы хотим отрисовать в одну секунду

    screen.fill(BLACK)  # каждый раз надо перерисовывать экран, чтобы синей полоски не было
    # screen.blit(follow, (0, 0))  # (x, y) - координаты левого верхнего угла, blid - прикрепляет к экрану
    # screen.blit(like, (0, 300)) если статично
    screen.blit(like, (x, y))
    # порядок трех команд выше важен, если перместить вниз покраску черного, то весь экран будет черным
    screen.blit(img, (50, 50))
    x += direct_like_x
    if x + width >= 600 or x < 0:  # меняем направление
        direct_like_x = -direct_like_x

    y += direct_like_y
    if y + height >= 400 or y < 0:  # меняем направление
        direct_like_y = -direct_like_y

    screen.blit(follow, (x2, y2))
    x2 += direct_follow_x
    if x2 + width >= 600 or x2 < 0:  # меняем направление
        direct_follow_x = -direct_follow_x

    y2 += direct_follow_y
    if y2 + height >= 400 or y2 < 0:  # меняем направление
        direct_follow_y = -direct_follow_y

    pygame.display.update()
