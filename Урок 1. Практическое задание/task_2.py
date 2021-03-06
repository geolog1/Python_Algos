"""
Задание 2. Выполнить логические побитовые операции "И", "ИЛИ"
и др. над числами 5 и 6. Выполнить
над числом 5 побитовый сдвиг вправо и влево на два знака.

Подсказка: это стандартные операции, которые осуществляются с помощью
стандартных операторов. Попробуйте найти каких именно.
"""

a = 5 (101)
b = 6 (110)

(a & b) = 4 (100)
"""Бинарный "И" оператор, копирует бит в результат только если бит присутствует в обоих операндах"""

(a | b) = 7 (111)
"""Бинарный "ИЛИ" оператор копирует бит, если тот присутствует в хотя бы в одном операнде"""

(a ^ b) = 3 (011)
"""Бинарный "Исключительное ИЛИ" оператор копирует бит только если бит присутствует в одном из операндов, но не в обоих сразу."""

(~a) = 2 (010)
(~b) = 1 (001)
"""Бинарный комплиментарный оператор. Является унарным (то есть ему нужен только один операнд) меняет биты на обратные"""


a << 2 = 20 (10100)
a >> 2 = 1 (001)

"""Побитовый сдвиг влево. Значение левого операнда "сдвигается" влево на количество бит указанных в правом операнде"""