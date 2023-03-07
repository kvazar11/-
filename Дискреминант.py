#Шапка
print("Программа, которая решает квадратное уравнение по D")
#Задаём коэффициенты
a , b , c = float(input()) , float(input ()) , float(input())
#Формула дискриминанта 
d = b ** 2 - 4*a*c
#Математический модуль
from math import sqrt
#Условие 
if d < 0:
    print("Нет корней")
elif d > 0:
    x1 = (-b + sqrt(d) ) / 2*a
    x2 = (-b - sqrt(d) ) / 2*a
    print("x1 =",round (x1, 2))
    print("x2 =",round (x2, 2))
elif d == 0:
    x = - b / 2*a
    print("x =",round (x, 2))
    
