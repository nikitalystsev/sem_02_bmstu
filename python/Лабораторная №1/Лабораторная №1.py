# Лысцев Никита ИУ7-23Б
# Калькулятор пятеричной системы счисления

import tkinter as tk
from tkinter import messagebox
import checks as ch
import calc5


def add_digit(digit):
    """ Функция добавляет цифру в поле ввода"""
    value = ent1.get()
    if value[0] == '0' and len(value) == 1:
        value = value[1:]
    ent1['state'] = tk.NORMAL
    ent1.delete(0, tk.END)
    ent1.insert(tk.END, value + digit)
    ent1['state'] = tk.DISABLED


def add_operator(operator):
    """ Функция добавляет знак операции или точку в поле ввода"""
    # print('add_operator call')
    value = ent1.get()
    if value[0] == '0' and len(value) == 1:
        value = value[1:]
    elif value[-1] in '-+':
        value = value[:-1]
    elif '+' in value or '-' in value:
        calculate()
        value = ent1.get()
    ent1['state'] = tk.NORMAL
    ent1.delete(0, tk.END)
    ent1.insert(tk.END, value + operator)
    ent1['state'] = tk.DISABLED


def add_dot(operator):
    """ Функция добавляет точку в поле ввода"""
    value = ent1.get()
    #    if value[0] == '0' and len(value) == 1:
    #        value = value[1:]
    #    elif value[-1] in '-+':
    #        value = value[:-1]
    #    elif '+' in value or '-' in value:
    #        calculate()
    #        value = ent1.get()
    ent1['state'] = tk.NORMAL
    ent1.delete(0, tk.END)
    ent1.insert(tk.END, value + operator)
    ent1['state'] = tk.DISABLED


def calculate():
    """Функция вставляет в поле ввода посчитанный результат"""
    value = ent1.get()
    if value[-1] in '+-':
        value = value + value[:-1]
    value = calc_math_expression(value)
    if not ch.check_float(value):
        # print('Некорректное value =', value)
        messagebox.showinfo('Некорректная операция!',
                            'Введенная операция не может быть вычислена')
        ent1['state'] = tk.NORMAL
        ent1.delete(0, tk.END)
        ent1.insert(tk.END, '0')
        ent1['state'] = tk.DISABLED
    else:
        ent1['state'] = tk.NORMAL
        ent1.delete(0, tk.END)
        ent1.insert(0, value)
        ent1['state'] = tk.DISABLED


def calc_math_expression(s):
    """Функция считает полученное из поля ввода значение"""
    # print('calc_math_expression call')
    # print('Переданная в функцию строка:', s)
    operators = '+-'
    expression = s
    number1 = ''
    number2 = ''
    operation_sign = ''
    for i in range(len(expression) - 1, -1, -1):
        if expression[i] in operators:
            operation_sign = expression[i]
            j = i + 1
            k = i - 1
            while j < len(expression) and (expression[j].isdigit()
                                           or expression[j] == '.'):
                number2 += expression[j]
                j += 1
            while k >= 0 and (expression[k].isdigit()
                              or expression[k] == '.'
                              or expression[k] in '-+'):
                number1 += expression[k]
                k -= 1
            break
    number2.strip()
    number1 = number1[::-1]
    number1.strip()
    # print('Первое число:', number1)
    # print('Второе число:', number2)
    # print('Знак операции при вычислении:', operation_sign)
    if ch.check_float(number1) and ch.check_float(number2):
        result = calc5.calculate_operation(number1, number2, operation_sign)
        # print('Возвращаемое значение:', result)
        return result
    # print('Возвращаемое значение:', expression)
    return expression


def delete_symbol():
    """Функция удаляет последний введенный в поле ввода символ"""
    s = ent1.get()
    s = s[:-1]
    if not s:
        s = '0'
    ent1['state'] = tk.NORMAL
    ent1.delete(0, tk.END)
    ent1.insert(tk.END, s)
    ent1['state'] = tk.DISABLED


def delete_all_elem():
    """Функция очищает поле ввода"""
    ent1['state'] = tk.NORMAL
    ent1.delete(0, tk.END)
    ent1.insert(tk.END, '0')
    ent1['state'] = tk.DISABLED


def get_button_digit(digit: str):
    """Функция создает кнопку для переданной в качестве пареметра цифре"""
    return tk.Button(text=digit, bg='#34495e', fg='#ecf0f1',
                     font=('@Microsoft JhengHei UI', 20),
                     command=lambda: add_digit(digit),
                     relief=tk.FLAT)


def get_button_operator(operator: str):
    """
    Функция создает кнопку для переданного
    в качестве параметра знака операции или точки
    """
    if operator == '+/-':
        return tk.Button(text=operator, bg='#34495e',
                         font=('@Microsoft JhengHei UI', 20), fg='#ecf0f1',
                         command=lambda: add_operator(operator),
                         relief=tk.FLAT)
    return tk.Button(text=operator, bg='#34495e',
                     font=('@Microsoft JhengHei UI', 20), fg='#ecf0f1',
                     command=lambda: add_operator(operator),
                     relief=tk.FLAT)


def calc_button(operator: str):
    """Функция создает кнопку для вычисления полученного из поля ввода значения"""
    return tk.Button(text=operator, bg='#2d3e50',
                     fg='#ecf0f1', font=('@Microsoft JhengHei UI', 20),
                     command=calculate,
                     relief=tk.FLAT)


def get_separator_button(separator: str):
    """Функция создает кнопку для разделителя -- точки"""
    return tk.Button(text=separator, bg='#34495e',
                     fg='#ecf0f1', font=('@Microsoft JhengHei UI', 20),
                     command=lambda: add_dot(separator),
                     relief=tk.FLAT)


def delete_one_elem_button(operator: str):
    """Функция создает кнопку для удаления последнего элемента в поле ввода"""
    return tk.Button(text=operator, bg='#34495e',
                     font=('@Microsoft JhengHei UI', 20), fg='#ecf0f1',
                     command=delete_symbol,
                     relief=tk.FLAT)


def delete_all(operator: str):
    """Функция создает кнопку для очищения поля ввода"""
    return tk.Button(text=operator, bg='#34495e',
                     fg='#ecf0f1', font=('@Microsoft JhengHei UI', 20),
                     command=delete_all_elem,
                     relief=tk.FLAT)


def check_symbols(event):
    """В зависимости от нажатой клавиши выполяется то, или иное действие"""
    # print(repr(event.char))
    if event.char in '01234':
        # print('check call')
        add_digit(event.char)
    elif event.char == '.' or event.char in '+-':
        add_operator(event.char)
    elif event.char == '\r':
        calculate()
    elif event.char.isalpha():
        messagebox.showinfo('Некорректный ввод!',
                            'В поле ввода вводятся только цифры от 0 до 4, '
                            'точка и знаки операций!')
    elif event.char == '\x08':
        delete_symbol()


root = tk.Tk()
root.geometry('240x210+100+200')
root.minsize(240, 210)
root.maxsize(400, 350)
root.title('Калькулятор')
root.bind('<Key>', check_symbols)
mainmenu_ = tk.Menu(root, tearoff=0)
menu = tk.Menu(mainmenu_, tearoff=0)
mainmenu_.add_cascade(label='Меню', menu=menu)
root.config(menu=mainmenu_, bg='black')

actionsmenu = tk.Menu(menu, tearoff=0)
a = (
    'Сложение: знак "+"',
    'Вычитание: знак "-"'
)
b = '+', '-'
for i in range(len(a)):
    actionsmenu.add_command(label=a[i],
                            command=lambda x=b[i]: add_operator(x))
menu.add_cascade(label='Заданные действия',
                 menu=actionsmenu)

menu.add_command(label='Очистка поля ввода и вывода',
                 command=delete_all_elem)

infomenu = tk.Menu(menu, tearoff=0)
a = (
    'Лысцев Н. Д. ИУ7-23Б',
    'Калькулятор систем счисления (5с/с)'
)
for i in a:
    infomenu.add_command(label=i)

menu.add_cascade(label='Информация о программе и авторе',
                 menu=infomenu)

ent1 = tk.Entry(root, bg='#ecf0f1', fg='#34495e',
                font=('@Microsoft JhengHei UI', 20),
                justify=tk.RIGHT,
                width=26,
                borderwidth=0)
ent1.insert(tk.END, '0')
ent1['state'] = tk.DISABLED
ent1.grid(row=0, column=0, columnspan=4, stick='wens')
a = (
    get_button_digit('4'),
    get_button_digit('1'),
    get_button_digit('0'),
    get_button_digit('3'),
    get_button_digit('2'),
    delete_one_elem_button('C'),
    get_button_operator('+'),
    get_separator_button('.'),
    delete_all('AC'),
    get_button_operator('-'),
    calc_button('=')
)
c = 0
for j in range(4):
    for i in range(1, 4):
        if i == 3 and j == 1:
            pass
        elif i == 3 and j == 0:
            a[c].grid(row=i, column=j, stick='wens', columnspan=2)
            c += 1
        else:
            a[c].grid(row=i, column=j, stick='wens')
            c += 1

for j in range(4):
    root.grid_columnconfigure(j, weight=1, minsize=40)

for i in range(1, 4):
    root.grid_rowconfigure(i, weight=1, minsize=40)

root.mainloop()
