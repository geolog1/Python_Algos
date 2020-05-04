"""
Задание_9.Найти максимальный элемент среди минимальных элементов столбцов матрицы.

Пример:

Задайте количество строк в матрице: 3
Задайте количество столбцов в матрице: 4
 36 20 42 38
 46 27  7 33
 13 12 47 15
[13, 12, 7, 15] минимальные значения по столбцам
Максимальное среди них = 15
"""

from random import randint

def func(row_numb, col_numb):

    matrix = []
    # Создаем матрицу
    for i in range(row_numb):
        string = []
        for j in range(col_numb):
            string.append(randint(0, 50))
            print(f'{string[j]:3}', end='')
        matrix.append(string)
        print()

    # Создается список, в который будем заносить минимальные элементы по столбцам
    min_lst = []
    # Определяем минимальные элементы по столбцам
    for i in range(col_numb):
        min_l = []
        for j in range(row_numb):
            min_l.append(matrix[j][i])
        min_lst.append(min(min_l))

    print(f'{min_lst} минимальные значения по столбцам')
    print(f'Максимальные значения по столбцам {max(min_lst)}')

try:
    ROW_NUMB = int(input("Задайте количество строк в матрице: "))
    COL_NUMB = int(input("Задайте количество столбцов в матрице: "))
    func(ROW_NUMB, COL_NUMB)
except ValueError:
    print("Ошибка. Надо ввести число!")
