# Лысцев Никита ИУ7-23Б
# Уточнение корня методом секущих

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

import matplotlib.pyplot as plt

import numpy as np

import sympy as sp

from math import *

root = tk.Tk()

main_frame = tk.Frame(root)
main_frame.pack()

start_frame = tk.Frame(main_frame)
start_frame.pack(fill=tk.BOTH, expand=True)
lbl_input_start = tk.Label(start_frame, text='start')
lbl_input_start.pack(side=tk.LEFT)
ent_input_start = tk.Entry(start_frame, width=60)
ent_input_start.pack(side=tk.RIGHT, padx=50)

end_frame = tk.Frame(main_frame)
end_frame.pack(fill=tk.BOTH, expand=True)
lbl_input_end = tk.Label(end_frame, text='end')
lbl_input_end.pack(side=tk.LEFT)
ent_input_end = tk.Entry(end_frame, width=60)
ent_input_end.pack(side=tk.RIGHT, padx=50)

step_frame = tk.Frame(main_frame)
step_frame.pack(fill=tk.BOTH, expand=True)
lbl_input_step = tk.Label(step_frame, text='step')
lbl_input_step.pack(side=tk.LEFT)
ent_input_step = tk.Entry(step_frame, width=60)
ent_input_step.pack(side=tk.RIGHT, padx=50)

max_iter_frame = tk.Frame(main_frame)
max_iter_frame.pack(fill=tk.BOTH, expand=True)
lbl_input_max_iter = tk.Label(max_iter_frame, text='max iterations')
lbl_input_max_iter.pack(side=tk.LEFT)
ent_input_max_iter = tk.Entry(max_iter_frame, width=60)
ent_input_max_iter.pack(side=tk.RIGHT, padx=50)

eps_frame = tk.Frame(main_frame)
eps_frame.pack(fill=tk.BOTH, expand=True)
lbl_input_eps = tk.Label(eps_frame, text='eps')
lbl_input_eps.pack(side=tk.LEFT)
ent_input_eps = tk.Entry(eps_frame, width=60)
ent_input_eps.pack(side=tk.RIGHT, padx=50)

function_frame = tk.Frame(main_frame)
function_frame.pack(fill=tk.BOTH, expand=True)
lbl_input_function = tk.Label(function_frame, text='function')
lbl_input_function.pack(side=tk.LEFT)
ent_input_function = tk.Entry(function_frame, width=60)
ent_input_function.pack(side=tk.RIGHT, padx=50)

ent_input_function.insert(0, 'sin(x)')
ent_input_start.insert(0, '0.5')
ent_input_end.insert(0, '10')
ent_input_step.insert(0, '0.3')
ent_input_max_iter.insert(0, '100')
ent_input_eps.insert(0, '1e-5')

table = ttk.Treeview(main_frame, show='headings')  # show убирает крайний левый столбец (корневой элемент)
scroll = ttk.Scrollbar(main_frame)
heads = ['№ root', '[xi, xi + 1]', 'x', 'f(x)', 'iterations', 'error']
table['columns'] = heads

figure = plt.figure()

main_menu = tk.Menu(root, tearoff=0)
menu = tk.Menu(main_menu, tearoff=0)
main_menu.add_cascade(label='Меню', menu=menu)
root.config(menu=main_menu, bg="black")
infomenu = tk.Menu(menu, tearoff=0)
a = (
    'Лысцев Н. Д. ИУ7-23Б',
    'Уточнение корня методом секущих'
)
for i in a:
    infomenu.add_command(label=i)
menu.add_cascade(label='Информация о программе и авторе',
                 menu=infomenu)

error_menu = tk.Menu(menu, tearoff=0)

a = (
    "Справка по кодам ошибок:",
    "0. корень найден",
    "1. деление на ноль",
    "2. превышено число итераций",
    "3. корень не лежит на отрезке",
    "4. несколько корней на отрезке"
)
for i in a:
    error_menu.add_command(label=i)
menu.add_cascade(label='Информация по кодам ошибок',
                 menu=error_menu)

for header in heads:
    table.heading(header, text=header, anchor='center')
    table.column(header, anchor='center', width=120)

x, y = sp.symbols('x y')


def f(value):
    return eval(ent_input_function.get().replace('x', '(' + str(value) + ')'))


def get_all_values():
    try:
        a = float(ent_input_start.get())
        b = float(ent_input_end.get())
        if a >= b:
            messagebox.showinfo("Incorrect data entered!", "Please re-enter")
            return None
        h = float(ent_input_step.get())
        max_iteration = int(ent_input_max_iter.get())
        eps = float(ent_input_eps.get())
        f(a)
    except:
        messagebox.showinfo("Incorrect data entered!", "Please re-enter")
        return None
    return a, b, h, max_iteration, eps


def table_build():
    scroll.config(command=table.yview)
    table.config(yscrollcommand=scroll.set)
    scroll.pack(side=tk.RIGHT, fill=tk.Y)
    table.pack(fill=tk.BOTH)


def find_inflation_points(function: str):
    diff1 = sp.diff(function, x)
    # print("diff1", diff1)
    diff2 = sp.diff(diff1, x)
    # print("diff2", diff2)
    solution = sp.solve(diff2, x)
    return str(diff2), list(solution)


def main():
    if get_all_values() is None:
        return

    figure.clear()

    a, b, h, max_iteration, eps = get_all_values()
    table_build()
    for i in table.get_children():
        table.delete(i)
    root.update()

    x = np.linspace(a, b, 10000)
    y = []
    for xi in x:
        y.append(f(xi))
    y = np.array(y)
    plt.title(f'График функции {ent_input_function.get()}')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid()
    plt.plot(x, y)

    extremum = []
    for i in range(1, len(y) - 1):
        if y[i] >= y[i - 1] and y[i] >= y[i + 1]:
            extremum.append((x[i], y[i]))
        elif y[i] <= y[i - 1] and y[i] <= y[i + 1]:
            extremum.append((x[i], y[i]))
    extremum = np.array(extremum)
    if len(extremum) != 0:
        plt.scatter(extremum[:, 0], extremum[:, 1], marker='p', color='orange', label='extremum')

    x_infl = []
    y_infl = []
    pr, solution = find_inflation_points(ent_input_function.get())
    for i in range(len(x)):
        if abs(eval(pr.replace('x', '(' + str(x[i]) + ')'))) < 1e-2:
            x_infl.append(x[i])
            y_infl.append(y[i])
    x_infl = np.array(x_infl)
    y_infl = np.array(y_infl)

    if len(x_infl) != 0 and solution:
        plt.scatter(x_infl, y_infl, marker='P', color='green', label='inflection points')

    i = 0
    roots = []
    count = 0
    while a + h * (i + 1) <= b + h:
        left = a + h * i
        right = a + h * (i + 1)

        previous_x = right  # предыдущий корень
        current_x = left  # текущий корень
        if f(left) * f(right) > 0:  # нет корня на отрезке
            i += 1
            continue

        iteration = 0  # счетчик итераций
        no_root = False
        error_code = 0  # код ошибки
        while abs(current_x - previous_x) > eps:
            current_y = f(current_x)
            previous_y = f(previous_x)
            if abs(current_y - previous_y) == 0:
                no_root = True
                error_code = 1
                break

            next_x = current_x - ((current_x - previous_x) / (current_y - previous_y)) * f(current_x)

            current_x = previous_x
            previous_x = next_x

            iteration += 1
            if iteration > max_iteration:
                no_root = True
                error_code = 2
                break

        if not left <= current_x <= right:
            error_code = 3
            no_root = True

        if not no_root:
            if len(roots) != 0 and current_x - roots[-1] < eps:
                count += 1
                error_code = 4
                values = (count, f'[{left:.3f}, {right:.1g}]', '', '', iteration, error_code)
                table.insert('', tk.END, values=values)
            else:
                count += 1
                roots.append(current_x)
                values = (count, f'[{left:.3f}, {right:.3f}]',
                          f'{current_x:.7f}',
                          f'{f(current_x):.1g}',
                          iteration,
                          error_code)
                table.insert('', tk.END, values=values)
        else:
            values = (count, f'[{left:.3f}, {right:.1g}]', '', '', iteration, error_code)
            table.insert('', tk.END, values=values)
        i += 1

    roots = np.array(roots)
    values = []
    for i in roots:
        values.append(f(i))
    values = np.array(values)

    if len(roots) != 0:
        plt.scatter(roots, values, marker='p', color='red', label='roots')

    plt.legend()
    plt.show()


btn_launch = tk.Button(main_frame, text='launch', width=10, command=main)
btn_launch.pack()

root.mainloop()
