import tkinter as tk

canvas_width = 1000
canvas_height = 500

list_points_center = []
list_count_insertion = []
list_radius = []


def get_point_center():
    return ent_get_point.get()


def get_radius():
    return ent_get_radius.get()


def draw_circle():
    r = int(get_radius())
    x, y = map(int, get_point_center().split(","))
    list_points_center.append((x, y))
    list_radius.append(r)
    canvas.create_oval(x - r, y - r, x + r, y + r)


def print_list(event):
    print(list_points_center)
    print(list_count_insertion)
    print(list_radius)


def get_insertion():
    for i in range(len(list_points_center)):
        count = 0
        for j in range(i + 1, len(list_points_center)):
            center1 = list_points_center[i]
            radius1 = list_radius[i]
            center2 = list_points_center[j]
            radius2 = list_radius[j]

            dist = ((center1[0] - center2[0]) ** 2 + (center1[1] - center2[1]) ** 2) ** 0.5
            sum_radius = radius1 + radius2
            if dist < sum_radius:
                count += 1
        list_count_insertion.append(count)

    max_elem = float('-inf')
    max_ind = 0
    for i in range(len(list_count_insertion)):
        if list_count_insertion[i] > max_elem:
            max_elem = list_count_insertion[i]
            max_ind = i
    x, y = list_points_center[max_ind]
    r = list_radius[max_ind]
    canvas.create_oval(x - r, y - r, x + r, y + r, fill='red')


def clean_canvas():
    """
    Функция очищает холст и список с точками
    """
    canvas.delete('all')
    list_points_center.clear()
    list_radius.clear()
    list_count_insertion.clear()


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


get_radius_frame = tk.Frame(main_frame, bg='#FFD700')
get_radius_frame.pack(fill=tk.X)

lbl_frame = tk.Frame(get_radius_frame)
lbl_frame.pack(side=tk.LEFT, fill=tk.X)

lbl_get_radius = tk.Label(
    lbl_frame,
    text='Введите радиус окружности:',
    bg='yellow',
    width=30,
    borderwidth=5
)
lbl_get_radius.pack(expand=True, side=tk.LEFT)

ent_frame = tk.Frame(get_radius_frame)
ent_frame.pack(fill=tk.X)

ent_get_radius = tk.Entry(ent_frame, width=47, relief=tk.SUNKEN, borderwidth=5)
ent_get_radius.pack(expand=True, side=tk.LEFT, fill=tk.X)

get_point_frame = tk.Frame(main_frame, bg='#FFD700')
get_point_frame.pack(fill=tk.X)

lbl_frame = tk.Frame(get_point_frame)
lbl_frame.pack(side=tk.LEFT, fill=tk.X)

lbl_get_point = tk.Label(
    lbl_frame,
    text='Введите координаты центра:',
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
    text='Добавить окружность',
    bg='#3CB371',
    command=draw_circle,
    relief=tk.FLAT
)
btn_get_point.pack(fill=tk.X)

btn_find_triangle = tk.Button(
    main_frame,
    text='Поиск окружности',
    bg='#00CED1',
    command=get_insertion,
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
