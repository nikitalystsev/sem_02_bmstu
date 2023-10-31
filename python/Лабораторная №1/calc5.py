sample = "0123456789ABCDEF"
system = 5


def check_first_negative_number(number1: str,
                                number2: str,
                                operation_sign: str):
    if float(number1) < 0:
        if operation_sign == '-':
            number1, number2, = number2, number1[1:]
            return number1, number2, '+'
        else:
            number1, number2, = number2, number1[1:]
            return number1, number2, '-'
    return number1, number2, operation_sign


def number_refinement(number1: str, number2: str):
    if number1 not in '.':
        number1 += '.'
    if number2 not in '.':
        number2 += '.'

    whole1 = number1.split('.')[0]
    fractional1 = number1.split('.')[1]
    whole2 = number2.split('.')[0]
    fractional2 = number2.split('.')[1]

    max_len_whole = max(len(whole1), len(whole2))
    max_len_fractional = max(len(fractional1), len(fractional2))

    whole1 = whole1.zfill(max_len_whole)
    whole2 = whole2.zfill(max_len_whole)

    fractional1 = fractional1.ljust(max_len_fractional, '0')
    fractional2 = fractional2.ljust(max_len_fractional, '0')

    number1 = ''.join([whole1, fractional1])
    number2 = ''.join([whole2, fractional2])

    return number1, number2, max_len_whole


def get_new_number(number1: str, number2: str, operation_sign=''):
    if number1 < number2:
        number1, number2 = number2, number1
        operation_sign = '-'
    temp = number2
    number2 = ''
    for i in temp:
        number2 += sample[system - 1 - sample.find(i)]
    p = 1
    return number1, number2, operation_sign, p


def calculate_operation(number1: str,
                        number2: str,
                        operation_sign='+'):
    temp = number1
    temp_sign = operation_sign
    if number1[0] == '+':
        number1 = number1[1:]
    print('------------------------------------------')
    # общие действия для всех операций
    print('Переданные числа:', number1, number2)
    number1, number2, operation_sign = check_first_negative_number(
        number1,
        number2,
        operation_sign
    )

    number1, number2, max_len_whole = number_refinement(
        number1,
        number2
    )
    print('Измененные  числа:', number1, number2)
    print('Знак операции:', operation_sign)
    print('Длина для возврата точки:', max_len_whole)
    p = 0  # переменная, отвечающая за переполнение в разряде
    len_number = len(number1)
    print('Длина числа:', len_number)
    result = ''
    print('Начальный результат:', result)
    print('------------------------------------------')

    # получаем новое число, если операция вычитание
    if operation_sign == '-':
        number1, number2, operation_sign, p = get_new_number(number1,
                                                             number2)
    # основной цикл вычислений
    for i in range(-1, -len_number - 1, -1):
        subtotal = sample.find(number1[i]) + sample.find(number2[i]) + p
        print('Промежуточная сумма:', subtotal)
        p = subtotal // system  # переменная,
        # отвечающая за переполнение, либо 0, либо 1
        print('p =', p,
              'Переполнение есть' if p == 1 else 'Переполнения нет')
        numeral = subtotal % system
        print('Цифра, что запишется в результат:', numeral)
        result += sample[numeral]
        print('Промежуточный результат:', result)
        print()
    print('------------------------------------------')
    print('Результат после основного цикла:', result)

    # если по итогу у нас остался дополнительный разряд,
    # то мы его и прибавляем
    # остаться он может только в операции сложения
    if p == 1 and operation_sign == '+':
        result += sample[p]
        max_len_whole += 1
        len_number += 1
    print('Результат после потенциальных изменений разряда:', result)
    result = result[::-1]
    result = result[:max_len_whole] + '.' + result[max_len_whole:]
    result = result.strip('0')
    print('Результат после некоторых проверок:', result)
    if float(temp) < 0 and temp_sign == '-':
        operation_sign = '-'

    if operation_sign == '+':
        operation_sign = ''
    if result.startswith('.'):
        result = '0' + result
    if result[-1] == '.':
        result = result.rstrip('.')
    result = operation_sign + result
    print('Возвращаемый результат:', result)
    return result


print(calculate_operation('0', '23.11', '-'))
