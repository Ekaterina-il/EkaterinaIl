# 1 Задание

def division():
    el_1 = float(input("Введите первое число: "))
    el_2 = float(input("Введите второе число: "))
    if el_2 == 0:
        el_2 = (float(input("Введите второе число не равное нулю: ")))
    answer = el_1 / el_2
    return answer

print(f"Ответ:, {division()}")




# 2 Задание

def my_func(first_name, second_name, year, city, email, phone):
    return {f"Имя - {first_name}; Фамилия - {second_name}; "
          f"Год рождения - {year}; Город проживания - {city}; E-mail - {email}; Телефон - {phone}"}

print(my_func(first_name=(input("Введите имя: ")), second_name=input("Введите фамилию: "),
              year=input("Введите год рождения :"), city=input("Введите город проживания: "),
              email=input("Введите email: "), phone=input("Введите телефон: ")))




# 3 Задание
# def my_func(el_1, el_2, el_3):
#     a = max(el_1, el_2, el_3)
#
#     return a
#
# print(my_func(el_1=10, el_2=20, el_3=30))
# Ерунда какая-то




# 4 Задание

def my_func(x, y):
    x = float(input("Введите действительное положительное число: "))
    y = float(input("Введите целое отрицательное число: "))

    my_result = x**y
    return my_result


my_result = my_func(5, -1)


print(my_result)
# Не понятно почему, у функции с позиционными аргументами (условие дом.задания), когда я их присваиваю в 45 строке, расчет производится
# все-равно по введенным пользователем значениям. Проще сделать функцию без аргументов - def my_func()




# 5 Задание????
# my_list = input("Введите числа через пробел: ")
# my_sum = sum(my_list)
# print(my_sum)



# 6 Задание

def int_func():
    your_word = input("Введите слово маленькими латинскими буквами: ")
    new_str = input("Введите строку маленькими латинскими буквами, состоящую из слов, разделенных пробелами: ")
    return your_word.capitalize(), new_str.capitalize()


print(int_func())
# Здесь не получилось каждое слово в строке вывести с большой буквы.

