
def string_to_ints(s):
    try:
        return int(s)
    except ValueError:
        return f'������: ���������� ������������� {s} � ����� �����.'

def read_file(filename):
    try:
        with open(filename, mode='r', encoding='utf8') as file:
            return file.read()
    except FileNotFoundError:
        return f'������: ���� {filename} �� ������.'
    except IOError:
        return f'������ �����/������ ��� ������ � ������ {filename}.'


def divide_number(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return '������: ������� �� ����'
    except TypeError:
        return '������: ��������� ������ ���� �������.'

def acces_list_element(lst, index):
    try:
        return lst[index]
    except IndexError:
        return f'������: ������ {index} ��� ��������� ������.'
    except TypeError:
        return '������: ������ ������ ���� ������.'

print(divide_number(10, 't'))
print(divide_number(10, 0))

print(string_to_ints(5))
print(string_to_ints('t'))

print(read_file('txt.txt'))

print(acces_list_element(34, 3))
print(acces_list_element(4455, 'g'))
