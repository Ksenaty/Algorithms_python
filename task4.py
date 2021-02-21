# Написать программу, которая генерирует в указанных пользователем границах: ● случайное целое число,
# ● случайное вещественное число, ● случайный символ.
# Для каждого из трех случаев пользователь задает свои границы диапазона.
# Например, если надо получить случайный символ от 'a' до 'f', то вводятся эти символы.
# Программа должна вывести на экран любой символ алфавита от 'a' до 'f' включительно.

from random import randint, uniform

start = float(input('Введите число для начала границы чисел <<<'))
stop = float(input('Введите число для конца границы чисел <<<'))
alphabet = 'abcdefghijklmnopqrstuvwxyz'
start_alhabet = str(input('Введите букву для начала границы букв <<<'))
stop_alhabet = str(input('Введите букву для конца границы букв <<<'))
start_index = alphabet.find(start_alhabet)
stop_index = alphabet.find(stop_alhabet)
# Формально проверка введенных данных
if start_index > stop_index:
    if stop > start:
        print('Вы ввели неправильные данные')
else:
    random_int = randint(start, stop)
    random_float = uniform(start, stop)
    random_str = alphabet[randint(start_index, stop_index)]
    print(f'число = {random_int}')
    print(f'вещественное число = {random_float}')
    print(f'символ = {random_str}')
