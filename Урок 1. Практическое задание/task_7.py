"""
7. По длинам трех отрезков, введенных пользователем,
определить возможность существования треугольника,
составленного из этих отрезков. Если такой треугольник существует,
то определить, является ли он разносторонним, равнобедренным или равносторонним.
"""

a = int(input())
b = int(input())
c = int(input())

if (a + b > c) and (c + b > a) and (a + c > b):
    if (a == b == c):
        print("equilateral")
    elif (a == c) or (c == b) or (b == a):
        print("isosceles")
    elif (a*a + b*b == c*c) or (a*a + c*c == b*b) or (c*c + b*b == a*a):
        print("right")
    elif (a != b) and (b != c) and (a != c):
        print("scalene")
else:
         print("impossible")