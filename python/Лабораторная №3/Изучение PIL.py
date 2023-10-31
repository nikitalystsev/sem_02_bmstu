from PIL import Image

# # открытие изображения и получение информации
# img = Image.open("picture.png")
# img.show()
# print(img.size)
# print(img.format)
# print(img.mode)
# print(img.histogram)

# # сохранение изображения и создание миниатюр
# img = Image.open("picture.png")
# img.thumbnail((200, 200))
# img.save('mini_img.png')
# img.show()

# # обрезка изображения
# img = Image.open('picture.png')
# crop_img = img.crop((0, 100, 200, 200))  # 4 координаты: левый верхний, правый верхний, левый нижний, правый нижний
# crop_img.save('cropped.png')
# crop_img.show()

# # поворот изображения
# img = Image.open('picture.png')
# r_img = img.rotate(180)  # указываются градусы
# r_img.save('rotated.png')
# r_img.show()

# # фильтры для изображения,
# # чтобы использовать фильтры, нужно из этой же библиотеки импортировать класс ImageFilter
# from PIL import ImageFilter
#
# img = Image.open('picture.png')
# img.show()
#
# blurred_img = img.filter(ImageFilter.BLUR)
# blurred_img.save('blurred.png')
# blurred_img.show()
#
# contour_img = img.filter(ImageFilter.CONTOUR)
# contour_img.save('contour.png')
# contour_img.show()

# # создание холста и рисование фигур,
# # чтобы рисовать, нужно импортировать класс ImageDraw
# from PIL import ImageDraw
#
# img = Image.new('RGBA', (400, 200), 'gray')  # С помошью метода new создается новый холст.
# # Сначала в кавычках пишется метод RGBA,
# # далее указываются размеры изображения (ширина, высота), далее указывается цвет холста
# idraw = ImageDraw.Draw(img)
# idraw.rectangle((20, 20, 100, 100), fill='white')  # 4 координаты: первые две отвечают за позицию левой верхней точки,
# # вторые две отвечают за размеры; fill - заливка
# # idraw.ellipse((20, 20, 150, 150), fill='white')
# img.save('canvas.png')
# img.show()

# # создание текста на изображениях,
# # чтобы рисовать, нужно импортировать класс ImageDraw
# from PIL import ImageDraw, ImageFont
#
# img = Image.new('RGBA', (400, 200), 'gray')  # С помошью метода new создается новый холст.
# # Сначала в кавычках пишется метод RGBA,
# # далее указываются размеры изображения (ширина, высота), далее указывается цвет холста
# idraw = ImageDraw.Draw(img)
# idraw.rectangle((20, 20, 100, 100), fill='white')  # 4 координаты: первые две отвечают за позицию левой верхней точки,
# # вторые две отвечают за размеры; fill - заливка
#
# # чтобы в headline поместить настройки шрифта, нужно импортировать класс ImageFont
#
# headline = ImageFont.truetype('arial.ttf', size=30)  # записывается название шрифта, но с расширением,
# # size - размер шрифта в пикселях
# text = 'Hello, world!'
# idraw.text((110, 20), text, font=headline)  # сначала указываетя позиция текста, потом сам текст, потом ставим шрифт
# img.save('canvas.png')
# img.show()

# загрузка изображения по URL с интернета
# для этого понадобится библиотека requests
import requests
url = input(':::> ')
response = requests.get(url, stream=True).raw  # stream=True позволяет работать с большим объемом информации.
# raw - это строчка, то есть мы как бы работаем с объектом нашего изображения
img = Image.open(response)
img.save('sid.jpg', 'jpeg')  # вторым параметром можем указывать расширение
img.show()
