"""
Задание 6.	Пользователь вводит номер буквы в алфавите.
Определить, какая это буква.

Пример:
Введите номер буквы: 4
Введёному номеру соответствует буква: d

Подсказка: используйте ф-ции chr() и ord()
"""


word = int(input('Введите номер буквы: '))
word = ord('a') + word - 1
print('Это буква', chr(word))