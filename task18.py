""" Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

*Пример:*

5
    1 2 3 4 5
    6
    -> 5
    """
import random
N = int(input('Введите натуральное число:'))
#lst = [random.randrange(10) for _ in range(N)]
lst = [5, 6, 6, 3, 5, 3, 2, 9, 4, 8]
print(f'{lst = }')
#k = int(input('Введите число k:'))
#k = int(random.randrange(0,10))
k = 7
print(k)
from math import fabs
a = lst[0]
for i in range(len(lst)):
    if fabs(lst[i]-k) < fabs(a-k) or fabs(lst[i]-k) == fabs(a-k): #and lst[i] <=a:
       a = lst[i]
print(a)
   
    

           






