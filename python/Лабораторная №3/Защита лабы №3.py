import tkinter as tk
from tkinter import filedialog

from PIL import Image


def get_image():
    filetypes = (("Изображение", "*.bmp"), ("Изображение", "*.bmp"))
    img = filedialog.askopenfilename(title='Выберите файл', initialdir='.', filetypes=filetypes)
    return img


def get_name_image(image):
    char = image[-1]
    i = len(image) - 1
    name = ''
    while char != '/':
        char = image[i]
        name += image[i]
        i -= 1

    name = name[:-1][::-1]
    return name


def red_mesh():
    image = get_image()
    img = Image.open(image)
    width, height = img.size
    obj = img.load()
    for i in range(0, width):
        for j in range(0, height, 50):
            obj[i, j] = (255, 0, 0)
    for j in range(0, height):
        for i in range(0, width, 70):
            obj[i, j] = (255, 0, 0)
    image = get_name_image(image)
    image = 'red_mesh_' + image
    img.save(image)


def show_image():
    filetypes = (("Изображение", "*.png"), ("Изображение", "*.bmp"))
    img = filedialog.askopenfilename(title='Выберите файл', initialdir='.', filetypes=filetypes)
    img = Image.open(img)
    img.show()


root = tk.Tk()

main_frame = tk.Frame(root)
main_frame.pack()

btn_encrypt_message = tk.Button(main_frame, text='Красная сетка', command=red_mesh, bg='#00FA9A')
btn_encrypt_message.pack(fill=tk.X)

btn_show_image = tk.Button(main_frame, text='Посмотреть изображение', command=show_image, bg='#00FFFF')
btn_show_image.pack(fill=tk.X)

root.mainloop()
