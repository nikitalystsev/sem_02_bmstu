# Лысцев Н. Д. ИУ7-23Б
# Поиск треугольника с наибольшим углом

import tkinter as tk
from tkinter import messagebox

import math as m

import checks as ch

list_points = []

canvas_width = 700
canvas_height = 300

triangle = ''


def paint(event):
    """
    Функция добавляет точку в canvas с помощью клика левой кнопки мыши
    """
    print(event.x, event.y)
    canvas.create_line(event.x, event.y, event.x + 1, event.y, fill="red")
    return event.x, event.y


def get_list_points(event):
    """
    Функция добавляет точку в список
    """
    list_points.append(paint(event))


def calculate_angle(a: tuple, b: tuple, c: tuple):
    """
    Функция ищет максимальный угол в одном треугольнике
    """
    side1 = m.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)
    side2 = m.sqrt((a[0] - c[0]) ** 2 + (a[1] - c[1]) ** 2)
    side3 = m.sqrt((b[0] - c[0]) ** 2 + (b[1] - c[1]) ** 2)

    cos_a = (side1 ** 2 + side2 ** 2 - side3 ** 2) / (2 * side1 * side2)
    cos_b = (side1 ** 2 + side3 ** 2 - side2 ** 2) / (2 * side1 * side3)
    cos_c = (side2 ** 2 + side3 ** 2 - side1 ** 2) / (2 * side2 * side3)

    angle_a = m.acos(cos_a)
    angle_b = m.acos(cos_b)
    angle_c = m.acos(cos_c)

    max_angle = max(angle_a, angle_b, angle_c)

    max_angle = m.degrees(max_angle)
    return max_angle


def find_triangle_with_the_largest_angle():
    """
    Функция ищет треугольник с максимальным углом среди множества точек
    """
    global triangle
    global list_points
    if isinstance(triangle, int):
        canvas.delete(triangle)

    try:
        list_points = list(set(list_points))
        points_triangle = [list_points[0], list_points[1], list_points[2]]
    except IndexError:
        messagebox.showerror('Внимание!', 'Точек для поиска треугольника недостаточно!')
        return
    global_max_angle = 0
    for i in range(len(list_points)):
        for j in range(i + 1, len(list_points)):
            for k in range(j + 1, len(list_points)):
                a = list_points[i]
                b = list_points[j]
                c = list_points[k]

                max_angle = calculate_angle(a, b, c)

                if max_angle > global_max_angle:
                    global_max_angle = max_angle
                    points_triangle = [a, b, c]
    lbl_find_angle.config(text=f'Caмый большой угол: {round(global_max_angle, 3)}')
    lbl_points.config(text=f'Треугольник построен на точках: {points_triangle[0]} '
                           f'{points_triangle[1]} {points_triangle[2]}')
    triangle = canvas.create_polygon(points_triangle[0], points_triangle[1], points_triangle[2])
    return global_max_angle


def get_point_from_keyboard():
    """
    Функция получает точку с клавиатуры
    """
    point = ent_get_point.get()
    try:
        point = point.split(',')
        if len(point) > 2:
            messagebox.showinfo('Оповещение', 'Координата точки состоит из двух чисел')
            return
        point[0] = point[0].strip()
        point[1] = point[1].strip()

        if ch.check_int(point[0]):
            x = int(point[0])
        else:
            x = float(point[0])

        if ch.check_int(point[1]):
            y = int(point[1])
        else:
            y = float(point[1])
        if x < 0 or x > canvas_width or y < 0 or y > canvas_height:
            messagebox.showinfo('Оповещение',
                                f'Полученная точка выходит за пределы холста\n'
                                f'Размеры холста: {canvas_width}x{canvas_height} пикселей')
            return
        point = (x, y)
        list_points.append(point)
        canvas.create_line(x, y, x + 1, y, fill="#000080")
        ent_get_point.delete(0, tk.END)
    except:
        messagebox.showinfo('Оповещение', 'Координата точки состоит из двух чисел')
        return


def print_list(event):
    """
    Функция выводит в консоль список с точками
    """
    print(list_points)


def clean_canvas():
    """
    Функция очищает холст и список с точками
    """
    canvas.delete('all')
    list_points.clear()


root = tk.Tk()
root.title("Треугольник с наибольним углом")

root.config(bg='#FF1493', padx=5, pady=5, relief=tk.FLAT)
root.resizable(False, False)

root.bind('<Button-3>', print_list)

main_menu = tk.Menu(root, tearoff=0)
menu = tk.Menu(main_menu, tearoff=0)
main_menu.add_cascade(label="Меню", menu=menu)
root.config(menu=main_menu)

infomenu = tk.Menu(menu, tearoff=0)
information = (
    'Лысцев Н. Д. ИУ7-23Б',
    'Поиск треугольника с наибольним углом'
)
for info in information:
    infomenu.add_command(label=info)
menu.add_cascade(label='Информация о программе и авторе', menu=infomenu)

main_frame = tk.Frame(root)
main_frame.pack()

canvas = tk.Canvas(main_frame, width=canvas_width, height=canvas_height, bg='white')
canvas.pack(expand=tk.YES, fill=tk.BOTH)

canvas.bind('<Button-1>', get_list_points)

get_point_frame = tk.Frame(main_frame, bg='#FFD700')
get_point_frame.pack(fill=tk.X)

lbl_frame = tk.Frame(get_point_frame)
lbl_frame.pack(side=tk.LEFT, fill=tk.X)

lbl_get_point = tk.Label(
    lbl_frame,
    text='Введите координаты одной точки:',
    bg='yellow',
    width=30,
    borderwidth=5
)
lbl_get_point.pack(expand=True, side=tk.LEFT)

ent_frame = tk.Frame(get_point_frame)
ent_frame.pack(fill=tk.X)

ent_get_point = tk.Entry(ent_frame, width=47, relief=tk.SUNKEN, borderwidth=5)
ent_get_point.pack(expand=True, side=tk.LEFT, fill=tk.X)

btn_get_point = tk.Button(
    main_frame,
    text='Добавить точку',
    bg='#3CB371',
    command=get_point_from_keyboard,
    relief=tk.FLAT
)
btn_get_point.pack(fill=tk.X)

btn_find_triangle = tk.Button(
    main_frame,
    text='Поиск треугольника',
    bg='#00CED1',
    command=find_triangle_with_the_largest_angle,
    relief=tk.FLAT
)
btn_find_triangle.pack(fill=tk.X)

angle_frame = tk.Frame(main_frame, bg='#FFD700')
angle_frame.pack(expand=True, fill=tk.X)

lbl_find_angle = tk.Label(
    angle_frame,
    text=f'Caмый большой угол: {0}',
    bg='#B0C4DE',
    borderwidth=5
)
lbl_find_angle.pack(expand=True, fill=tk.X)

lbl_points = tk.Label(
    angle_frame,
    bg='#FFD700',
    borderwidth=5
)
lbl_points.pack(expand=True)

btn_find_triangle = tk.Button(
    main_frame,
    text='Очистить холст',
    bg='#00FF00',
    command=clean_canvas,
    relief=tk.FLAT
)
btn_find_triangle.pack(fill=tk.X)

root.mainloop()
