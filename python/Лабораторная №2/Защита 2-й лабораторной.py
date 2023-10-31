# метод половинного деления

import tkinter as tk
from tkinter import messagebox

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
ent_input_eps.insert(0, '1e-5')


def get_all_values():
    try:
        a = float(ent_input_start.get())
        b = float(ent_input_end.get())
        if a >= b:
            messagebox.showinfo("Incorrect data entered!", "Please re-enter")
            return None
        eps = float(ent_input_eps.get())
        f(a)
    except:
        messagebox.showinfo("Incorrect data entered!", "Please re-enter")
        return None
    return a, b, eps


e = 0.0001


def f(value):
    return eval(ent_input_function.get().replace('x', '(' + str(value) + ')'))


ent = tk.Entry()


def main():
    if get_all_values() is None:
        return
    ent.delete(0, tk.END)
    a, b, eps = get_all_values()
    y1 = f(a)
    y2 = f(b)
    if y1 * y2 >= 0:
        ent.insert(0, "no root")
    else:
        n = 1
        x = (a + b) / 2
        y3 = f(x)
        while abs(y3) > eps:
            x = (a + b) / 2
            y3 = f(x)
            if y1 * y3 < 0:
                b = x
            else:
                a = x
                n += 1
        ent.insert(0, str(x))
    ent.pack()


btn_launch = tk.Button(main_frame, text='launch', width=10, command=main)
btn_launch.pack()

root.mainloop()
