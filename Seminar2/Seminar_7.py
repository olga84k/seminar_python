""" У вас есть код, который вы не можете менять (так часто бывает, когда код в глубине программы используется множество раз и вы не хотите ничего сломать):
transformation = <???>
values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29] # или любой другой список
transormed_values = list(map(transformation, values))
Единственный способ вашего взаимодействия с этим кодом - посредством задания функции transformation.
Однако вы поняли, что для вашей текущей задачи вам не нужно никак преобразовывать список значений, а нужно получить его как есть.
Напишите такое лямбда-выражение transformation, чтобы transformed_values получился копией values.

values = [1, 23, 42, 'asdfg']
transformed
transformed_values = list(map(trasformation, values))
if values == transformed_values:
    print('ok')
else:
    print('fail')
    
    Планеты вращаются вокруг звезд по эллиптическим орбитам. Назовем самой далекой планетой ту, орбита которой имеет самую большую площадь. Напишите функцию find_farthest_orbit(list_of_orbits), которая среди списка орбит планет найдет ту, по которой вращается самая далекая планета. Круговые орбиты не учитывайте: вы знаете, что у вашей звезды таких планет нет, зато искусственные спутники были были запущены на круговые орбиты. Результатом функции должен быть кортеж, содержащий длины полуосей эллипса орбиты самой далекой планеты. Каждая орбита представляет из себя кортеж из пары чисел - полуосей ее эллипса. Площадь эллипса вычисляется по формуле S = pi*a*b, где a и b - длины полуосей эллипса. При решении задачи используйте списочные выражения. Подсказка: проще всего будет найти эллипс в два шага: сначала вычислить самую большую площадь эллипса, а затем найти и сам эллипс, имеющий такую площадь. Гарантируется, что самая далекая планета ровно одна
Пример ввода и вывода данных представлены на следующем слайде
orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
print(*find_farthest_orbit(orbits))
def find_farthest_orbit(list_of_orbits):
    tmp = 0
    tmplst = [0,0]
    s = 0
    for i in list_of_orbits:
        a, b = i
        if a != b:
            tmp = a * b
        if tmp > s:
            s = tmp
            tmplst[0], tmplst[1]= a, b
    return tmplst
orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
print(*find_farthest_orbit(orbits))

второе решение
return max(list_of_orbits, key = lambda i: (i[0] != i[1]) * i[0] * i[1])

третье решение
orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]

def find_farthest_orbit(lst):
max = 0
max_i = 0
new_lst = enumerate(lst)
for i, (k, v) in new_lst:
if k != v:
if k * v > max:
max = k * v
max_i = i
return lst[max_i]

print(*find_farthest_orbit(orbits))

Напишите функцию same_by(characteristic, objects), которая проверяет, все ли объекты имеют одинаковое значение некоторой характеристики, и возвращают True, если это так. Если значение характеристики для разных объектов отличается - то False. Для пустого набора объектов, функция должна возвращать True. Аргумент characteristic - это функция, которая принимает объект и вычисляет его характеристику.
Ввод: Вывод:
values = [0, 2, 10, 6] same
if same_by(lambda x: x % 2, values):
print(‘same’)
else:
print(‘different’)
"""
#Первое решение

def same_by(func, values):
    for i in range(1, len(values)):
        if func(values[i]) != func(values[i - 1]):
            return False
    return True
values = [1, 3, 6, 7]
if same_by(lambda x: x % 2, values):
    print('same')
else:
    print('different')