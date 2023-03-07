__author__ = 'Костин Георгий'

# Задача-1:
# Следующая программа написана верно, однако содержит места потенциальных ошибок.
# используя конструкцию try добавьте в код обработку соответствующих исключений.
# Пример.
# Исходная программа:
# TODO:

if __name__ == '__main__':
    def avg(a, b):
        """Вернуть среднее геометрическое чисел 'a' и 'b'.

        Параметры:
            - a, b (int или float).

        Результат:
            - float.
        """
        if a * b >= 0:
            return (a * b) ** 0.5
        else:
            raise ValueError("Невозможно определить среднее геометрическое "
                             "введенных чисел.")


    try:
        a = float(input("a = "))
        b = float(input("b = "))
        c = avg(a, b)
        print(f"Среднее геометрическое = {c}")
    except ValueError as err:
        print("Ошибка:", err, ". Проверьте введенные числа.")
    except Exception as err:
        print("Ошибка:", err)

    if __name__ == '__main__':
        avg()


# ПРИМЕЧАНИЕ: Для решения задач 2-4 необходимо познакомиться с модулями os, sys!
# СМ.: https://pythonworld.ru/moduli/modul-os.html, https://pythonworld.ru/moduli/modul-sys.html

# Задача-2:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.
# TODO:

import os


def make_dir(name):
    try:
        os.makedirs(name)
        print('Успешно создано!')
    except FileExistsError:
        print('{} - уже существует\n'
              'Создание невозможно!'.format(name))


def remove_dir(name):
    try:
        os.removedirs(name)
        print('Успешно удалено!')
    except FileNotFoundError:
        print('{} - папки не существует\n'
              'Удаление невозможно!'.format(name))


def start():
    answer = ''
    quantity_dirs = range(1, 10)

    while answer != '3':

        answer = input('Выберите пункт меню:\n'
                       '1. Создать папки dir_1 - dir_9\n'
                       '2. Удалить папки dir_1 - dir_9\n'
                       '3. Продолжить\n')
        if answer == '3':
            continue
        elif answer == '1':
            for i in quantity_dirs:
                i = str(i)
                make_dir('dir_' + i)
        elif answer == '2':
            for i in quantity_dirs:
                i = str(i)
                remove_dir('dir_' + i)


if __name__ == '__main__':
    start()

# Задача-3:
# Напишите скрипт, отображающий папки текущей директории.
# TODO:


def list_dir():
    for item in os.listdir(os.getcwd()):
        print(item)


if __name__ == '__main__':
    list_dir()

# Задача-4:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.
# TODO:

import shutil


def file_copy():
    name_file = os.path.realpath(__file__)
    new_file = name_file + '.copy'
    if os.path.isfile(new_file) != True:
        shutil.copy(name_file, new_file)
        return new_file + ' - создан'
    else:
        return 'Файл уже скопирован'

if __name__ == '__main__':
    print(file_copy())