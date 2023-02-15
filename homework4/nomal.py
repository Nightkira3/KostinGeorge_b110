__author__ = 'Костин Георгий'

# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1
# TODO:

elem_n = int(input('Введите начало: '))
elem_m = int(input('Введите конец: '))

def fibonacci(elem_n, elem_m):
    res = []
    numb = 0
    following = 1
    for i in range(elem_m+1):
        if i >= elem_n:
            res.append(following)
        numb, following = following, following + numb
    return res

print(fibonacci(elem_n, elem_m))

# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()
# TODO:

def sort_to_max(origin_list):
    n = 1
    while n < len(origin_list):
        for i in range(len(origin_list) - n):
            if origin_list[i] > origin_list[i + 1]:
                origin_list[i], origin_list[i + 1] = origin_list[i + 1], origin_list[i]
        n += 1
    return origin_list

print(sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0]))

# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.
# TODO:

def some_kind_of_filter (filter_func, items):
    result = []
    for item in items:
        if filter_func(item):
            result.append(item)
    return result

# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.
# TODO:

print('Введите координаты точек: \n'
      'А1(х1, у1), А2(х2, у2), А3(x3 ,у3), А4(x4 , у4))')

x = [int(input('x{} = '.format(x))) for x in range(1, 5)]
y = [int(input('y{} = '.format(y))) for y in range(1, 5)]

diagonal = [(x[2] + x[0]) / 2, (y[2] + y[0]) / 2]
diagonal2 = [(x[3] + x[1]) / 2, (y[3] + y[1]) / 2]

if diagonal == diagonal2:
    print('Точки являются вершинами параллелограмма')
else:
    print('Точки не являются вершинами параллелограмма')