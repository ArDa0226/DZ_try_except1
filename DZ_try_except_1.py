
def string_to_ints(s):
    try:
        return int(s)
    except ValueError:
        return f'Ошибка: невозможно преобразовать {s} в целое число.'

def read_file(filename):
    try:
        with open(filename, mode='r', encoding='utf8') as file:
            return file.read()
    except FileNotFoundError:
        return f'Ошибка: файл {filename} не найден.'
    except IOError:
        return f'Ошибка ввода/вывода при работе с файлом {filename}.'


def divide_number(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return 'Ошибка: деление на ноль'
    except TypeError:
        return 'Ошибка: аргументы должны быть числами.'

def acces_list_element(lst, index):
    try:
        return lst[index]
    except IndexError:
        return f'Ошибка: индекс {index} вне диапазона списка.'
    except TypeError:
        return 'Ошибка: индекс должен быть числом.'

print(divide_number(10, 't'))
print(divide_number(10, 0))

print(string_to_ints(5))
print(string_to_ints('t'))

print(read_file('txt.txt'))

print(acces_list_element(34, 3))
print(acces_list_element(4455, 'g'))
