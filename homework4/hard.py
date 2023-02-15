__author__ = 'Костин Георгий'

# Задание-1:
# Написать программу, выполняющую операции (сложение и вычитание) с простыми дробями.
# Дроби вводятся и выводятся в формате:
# n x/y ,где n - целая часть, x - числитель, у - знаменатель.
# Дроби могут быть отрицательные и не иметь целой части, или иметь только целую часть.
# Примеры:
# Ввод: 5/6 + 4/7 (всё выражение вводится целиком в виде строки)
# Вывод: 1 17/42  (результат обязательно упростить и выделить целую часть)
# Ввод: -2/3 - -2
# Вывод: 1 1/3
# TODO:


# Задание-2:
# Дана ведомость расчета заработной платы (файл "data/workers").
# Рассчитайте зарплату всех работников, зная что они получат полный оклад,
# если отработают норму часов. Если же они отработали меньше нормы,
# то их ЗП уменьшается пропорционально, а за заждый час переработки
# они получают удвоенную ЗП, пропорциональную норме.
# Кол-во часов, которые были отработаны, указаны в файле "data/hours_of"
# TODO:

import os

DIR = "data"
workers = []
hours_of = []

with open(os.path.join(DIR, "workers"), "r", encoding="UTF-8") as ws:
    ws.readline()

    for line in ws:
        worker = list(map(lambda x: int(x) if x.isnumeric() else x, line.split()))
        if worker:
            workers.append(worker)

with open(os.path.join(DIR, "hours_of"), "r", encoding="UTF-8") as hs:
     hs.readline()

     for line in hs:
         hours = list(map(lambda x: int(x) if x.isnumeric() else x, line.split()))

         if hours:
            hours_of.append(hours)

for hours in hours_of:

    for worker in workers:
        if hours[0] in worker and hours[1] in worker:
            worker.append(hours[2])

for worker in workers:
    hoursNorm = worker[4]
    salary = worker[2]
    hoursWorked = worker[5]
    hourRate = salary / hoursNorm

    payment = hourRate * hoursWorked if hoursNorm > hoursWorked else salary + (hoursWorked - hoursNorm) * hourRate * 2
    worker.append(round(payment, 2))


tableHead = ['Имя', 'Фамилия', 'Зарплата', 'Должность', 'Норма_часов', 'Отработано_часов', 'Начислено']
workers.insert(0, tableHead)

workersTable = list(map(list, (zip(*workers))))
workers = []
for column in workersTable:
    column = list(map(str, column))
    maxLen = max(list(map(len, column)))

    workers.append(list(map(lambda x: x.ljust(maxLen, " "), column)))

workers = list(zip(*workers))
print(workers)

with open(os.path.join(DIR, "Зарплата"), "a", encoding="UTF-8") as s:
    for worker in workers:
        s.write("   ".join(worker) + os.linesep)

# Задание-3:
# Дан файл ("data/fruits") со списком фруктов.
# Записать в новые файлы все фрукты, начинающиеся с определенной буквы.
# Т.е. в одном файле будут все фрукты на букву “А”, во втором на “Б” и т.д.
# Файлы назвать соответственно.
# Пример имен файлов: fruits_А, fruits_Б, fruits_В ….
# Важно! Обратите внимание, что нет фруктов, начинающихся с некоторых букв.
# Напишите универсальный код, который будет работать с любым списком фруктов
# и распределять по файлам в зависимости от первых букв, имеющихся в списке фруктов.
# Подсказка:
# Чтобы получить список больших букв русского алфавита:
# print(list(map(chr, range(ord('А'), ord('Я')+1))))

# TODO:

import os

fruits = []
file = os.path.join("data", "fruits.txt")
with open(file, "r", encoding="UTF-8") as f:
    for line in f:
        if line.strip():
            fruits.append(line.strip())

letters = list(map(chr, range(ord('А'), ord('Я')+1)))
fil_dic = {}

while len(fruits) > 0:
    fruit = fruits.pop().title()
    if fil_dic.get(fruit[0]) == None:
        fil_dic[fruit[0]] = []
    fil_dic[fruit[0]].append(fruit)

for key, value in fil_dic.items():
    with open("fruit_{}".format(key), "w", encoding="UTF-8") as f:
        f.write(os.linesep.join(sorted(fil_dic[key])))

