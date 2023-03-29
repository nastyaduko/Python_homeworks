# Задача 30:  Заполните массив элементами арифметической прогрессии. Её первый элемент, разность и количество 
# элементов нужно ввести с клавиатуры. Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.
# Ввод: 7 2 5
# Вывод: 7 9 11 13 15

# first_el, diff, n = map(int, input('введиите чиисла через пробел: ').split())
# my_arr = list()
# [my_arr.append(first_el + (el-1)*diff) for el in range(1, n+1)]
# print(my_arr)


# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону (т.е. не
# меньше заданного минимума и не больше заданного максимума)
# Ввод: [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
# Ввод: [7, 11] - заданный диапазон от(включительно) до(включительно)
# Вывод: [1, 9, 13, 14, 19]

# from random import randint

# size = 10
# diapazon = [randint(-10, 10) for i in range(2)] 
# my_list = [randint(-10, 10) for i in range(size)]
# my_diapazon = sorted(diapazon)
# res_list = list()

# for el in range(size):
#     if my_diapazon[0] <= my_list[el] <= my_diapazon[1]:
#         res_list.append(el)

# print(my_list)
# print(my_diapazon)
# print(res_list)

