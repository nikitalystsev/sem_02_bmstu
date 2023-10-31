# Лысцев Н. Д. ИУ7-23Б'
# Стеганография, метод наименее значащих битов

import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image

root = tk.Tk()

root.title('Стеганография')
root.geometry("590x125+100+200")
root.config(bg='#DC143C')

main_frame = tk.Frame(root)
main_frame.pack()

get_message_frame = tk.Frame(main_frame)
get_message_frame.pack(fill=tk.BOTH, expand=True)
lbl_get_message = tk.Label(get_message_frame, text='Введите сообщение', width=30, bg='yellow')
lbl_get_message.pack(side=tk.LEFT)
ent_get_message = tk.Entry(get_message_frame, width=60)
ent_get_message.pack(side=tk.LEFT)

get_decrypt_message_frame = tk.Frame(main_frame)
get_decrypt_message_frame.pack(fill=tk.BOTH, expand=True)
lbl_get_decrypt_message = tk.Label(get_decrypt_message_frame, text='Расшифрованное сообщение:', width=30, bg='#3CB371')
lbl_get_decrypt_message.pack(side=tk.LEFT)
ent_get_encrypt_message = tk.Entry(get_decrypt_message_frame, width=60)
ent_get_encrypt_message.pack(side=tk.LEFT)

main_menu = tk.Menu(root, tearoff=0)
menu = tk.Menu(main_menu, tearoff=0)
main_menu.add_cascade(label="Меню", menu=menu)
root.config(menu=main_menu)

infomenu = tk.Menu(menu, tearoff=0)
a = (
    'Лысцев Н. Д. ИУ7-23Б',
    'Стеганография, метод наименее значащих битов'
)
for info in a:
    infomenu.add_command(label=info)
menu.add_cascade(label='Информация о программе и авторе',
                 menu=infomenu)


def show_image():
    filetypes = (("Изображение", "*.png"), ("Изображение", "*.bmp"))
    img = filedialog.askopenfilename(title='Выберите файл', initialdir='.', filetypes=filetypes)
    try:
        img = Image.open(img)
        img.show()
    except:
        messagebox.showinfo("Оповещение", "Файл не выбран!")
        return


def get_message():
    return ent_get_message.get()


def get_image_encrypt():
    filetypes = (("Изображение", "*.png"), ("Изображение", "*.bmp"))
    img = filedialog.askopenfilename(title='Выберите файл', initialdir='.', filetypes=filetypes)
    return img


def get_image_decrypt():
    filetypes = (("Изображение", "*.bmp"), ("Изображение", "*.bmp"))
    img = filedialog.askopenfilename(title='Выберите файл', initialdir='.', filetypes=filetypes)
    return img


def get_bin_ascii_code(symbol: str):
    return bin(ord(symbol))[2:]


def pad_to_8_bits(bin_ascii_code: str):
    if len(bin_ascii_code) < 8:
        complementary_length = 8 - len(bin_ascii_code)
        bin_ascii_code = '0' * complementary_length + bin_ascii_code
    return bin_ascii_code


def get_list_bin_ascii_codes(message: str):
    list_bin_ascii_codes = []
    for symbol in message:
        bin_ascii_code = get_bin_ascii_code(symbol)
        bin_ascii_code = pad_to_8_bits(bin_ascii_code)
        list_bin_ascii_codes.append(bin_ascii_code)
    return list_bin_ascii_codes


def r_g_b_bin(r, g, b):
    return bin(r)[2:], bin(g)[2:], bin(b)[2:]


def new_color_pixel(bits: str, r, g, b):
    r, g, b = r_g_b_bin(r, g, b)
    first_bit = bits[0]
    second_bit = bits[1]
    try:
        third_bit = bits[2]
        b = b[:-1] + third_bit
    except IndexError:
        pass

    r = r[:-1] + first_bit
    g = g[:-1] + second_bit
    return int(r, 2), int(g, 2), int(b, 2)


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


def encrypt_message():
    print("encrypt_message call")
    message = get_message()
    if len(message) == 0:
        messagebox.showinfo("Оповещение", "Введите сообщение для зашифровки!")
        return
    print('get_message call')
    message = message + '$'
    list_bin_ascii_codes = get_list_bin_ascii_codes(message)
    name_img = get_image_encrypt()
    image = name_img
    index = 0
    for i in range(len(image) - 1, -1, -1):
        if image[i] == '.':
            index = i
            break
    image = image[:index] + '.' + 'bmp'
    img = Image.open(name_img)
    img.save(image)
    try:
        img = Image.open(image)
    except:
        messagebox.showerror("Ошибка", "Файл не выбран!")
        return
    obj = img.load()
    width, height = img.size
    max_capacity = (width * height) / 3
    if len(message) > max_capacity:
        messagebox.showerror("Ошибка", "Сообщение слишком длинное, "
                                       "нельзя закодировать это сообщение в ввыбранном файле!")
        return
    count_elem = 0
    count_symbol = 0
    i = 0
    j = 0
    while i < width and count_elem < len(message):
        while j < height and count_elem < len(message):
            r, g, b = img.getpixel((i, j))
            obj[i, j] = new_color_pixel(list_bin_ascii_codes[count_elem][count_symbol:count_symbol + 3], r, g, b)
            count_symbol += 3
            if count_symbol == 9:
                count_elem += 1
                count_symbol = 0
            j += 1
        i += 1
    encrypt_image = 'encrypt_' + get_name_image(image)
    img.save(encrypt_image)


def decrypt_message():
    message = ''
    char = ''
    bits = ''
    list_bin_ascii_codes = []
    try:
        img = Image.open(get_image_decrypt())
    except:
        messagebox.showerror("Ошибка", "Файл не выбран!")
        return
    width, height = img.size
    count_elem = 0
    count_symbol = 0
    i = 0
    j = 0
    while i < width and char != '$':
        while j < height and char != '$':
            r, g, b = img.getpixel((i, j))
            r, g, b = r_g_b_bin(r, g, b)
            bits += r[-1] + g[-1] + b[-1]
            count_symbol += 3
            if count_symbol == 9:
                bits = bits[:-1]
                list_bin_ascii_codes.append(bits)
                count_elem += 1
                char = chr(int(list_bin_ascii_codes[-1], 2))
                count_symbol = 0
                bits = ''

            j += 1
        i += 1

    for element in list_bin_ascii_codes:
        message += chr(int(element, 2))
    ent_get_encrypt_message.delete(0, tk.END)
    ent_get_encrypt_message.insert(0, message[:-1])


btn_get_image = tk.Button(main_frame, text='Зашифровка', command=encrypt_message, bg='#00CED1')
btn_get_image.pack(fill=tk.X)

btn_encrypt_message = tk.Button(main_frame, text='Расшифровка', command=decrypt_message, bg='#B0C4DE')
btn_encrypt_message.pack(fill=tk.X)

btn_show_image = tk.Button(main_frame, text='Посмотреть изображение', command=show_image, bg='#FFD700')
btn_show_image.pack(fill=tk.X)

root.mainloop()
