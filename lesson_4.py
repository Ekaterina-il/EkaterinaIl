from functools import reduce
from itertools import cycle
from itertools import count


# 1 Задание


def salary(hours, earnings_per_hour, bonus):
    return hours * earnings_per_hour + bonus


print(f"1 Задание. Заработная плата сотрудника: {salary(10, 100, 15)}")

# 2 Задание

# my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
# new_list = [el for el in my_list if el - el[-1]]
# print(f"2 Задание. Исходный список: {my_list}")
# print(f"Новый список: {new_list}")


# 3 Задание


my_list = [el for el in range(20, 240) if el % 20 == 0 or el % 21 == 0]
print(f"3 Задание. {my_list}")

# 4 Задание

# 5 Задание

my_list = [el for el in range(100, 1001) if el % 2 == 0]
print(my_list)


def my_func(prev_el, el):
    # prev_el - предыдущий элемент
    # el - текущий элемент
    return prev_el * el


print(f"5 Задание. {reduce(my_func, my_list)}")

# 6 Задание

from itertools import cycle
from itertools import count

# не понятно, почему не импортируются функции