# -*- coding: utf-8 -*-
def string_to_ints(s):
    try:
        return int(s)
    except ValueError:
        return f'Îøèáêà: íåâîçìîæíî ïðåîáðàçîâàòü {s} â öåëîå ÷èñëî.'

def read_file(filename):
    try:
        with open(filename, mode='r', encoding='utf8') as file:
            return file.read()
    except FileNotFoundError:
        return f'Îøèáêà: ôàéë {filename} íå íàéäåí.'
    except IOError:
        return f'Îøèáêà ââîäà/âûâîäà ïðè ðàáîòå ñ ôàéëîì {filename}.'


def divide_number(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return 'Îøèáêà: äåëåíèå íà íîëü'
    except TypeError:
        return 'Îøèáêà: àðãóìåíòû äîëæíû áûòü ÷èñëàìè.'

def acces_list_element(lst, index):
    try:
        return lst[index]
    except IndexError:
        return f'Îøèáêà: èíäåêñ {index} âíå äèàïàçîíà ñïèñêà.'
    except TypeError:
        return 'Îøèáêà: èíäåêñ äîëæåí áûòü ÷èñëîì.'

print(divide_number(10, 't'))
print(divide_number(10, 0))

print(string_to_ints(5))
print(string_to_ints('t'))

print(read_file('txt.txt'))

print(acces_list_element(34, 3))
print(acces_list_element(4455, 'g'))
