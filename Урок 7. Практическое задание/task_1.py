"""
1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран
исходный и отсортированный массивы. Сортировка должна быть реализована в
виде функции. Обязательно доработайте алгоритм (сделайте его умнее).
Идея доработки: если за проход по списку не совершается ни одной сортировки, то завершение
Обязательно сделайте замеры времени обеих реализаций

Подсказка: обратите внимание, сортируем не по возрастанию, как в примере,
а по убыванию
"""
import timeit
import random

def bubble_sort(orig_list):
    swap = True
    while swap:
        swap = False
        for i in range(len(orig_list)-1):
            if orig_list[i] < orig_list[i+1]:
                orig_list[i], orig_list[i+1] = orig_list[i+1], orig_list[i]
                swap = True

    return orig_list


orig_list = [random.randint(-1000, 1000) for _ in range(2000)]
print("Исходный массив (рандом): ", orig_list)
print("Отсортированный массив (рандом):", bubble_sort(orig_list))

print(timeit.timeit("bubble_sort(orig_list)",
    setup="from __main__ import bubble_sort, orig_list", number=1000))


orig_list = [i for i in range(-1000, 1000)]
orig_list.reverse()
print("Исходный массив (изначально сортирован): ", orig_list)
print("Отсортированный массив (изначально сортирован):", bubble_sort(orig_list))

print(timeit.timeit("bubble_sort(orig_list)",
    setup="from __main__ import bubble_sort, orig_list", number=1000))

"""
Не до конца уверен, что алгоритм верный,
так как разных объемах данных иногда для отсортированного списка время получается больше.

"""
