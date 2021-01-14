# 1 задание

class Data:

    def __init__(self, dd_mm_yyyy):
        self.dd_mm_yyyy = dd_mm_yyyy

    @classmethod
    def user_data(cls, data):
         return list(map(int, data.dd_mm_yyyy.split("_")))

    @staticmethod
    def validation(data):
        checked_data = data.dd_mm_yyyy.split("_")
        if len(checked_data[2]) not in {2, 4}:
            raise ValueError("Введено неправильное значение года")
        if not 1 <= int(checked_data[1]) <= 12:
            raise ValueError("Введен неправильный месяц")
        if not 1 <= int(checked_data[0]) <= 31:
            raise ValueError("Введено неправильное значение дня")
        print("1 Задание: Успешно")


data = Data("01_11_2140")
data.validation(data)
print(Data.user_data(data))


# 2 Задание

class ErrDiv(Exception):

    def __init__(self, text_error):
        self.txt = text_error


    try:
        print("2 Задание:", 5/5)
    except ZeroDivisionError:
        print("2 Задание: Делить на 0 нельзя!")


# 3 Задание
print("3 Задание:")


class OwnError(Exception):

    def __init__(self, txt):
        self.txt = txt


new_list = []
while True:
    try:
        item = input("Введите число: ")
        if item == "stop":
            break
        if not item.isdigit():
            raise OwnError("Вы ввели не число!")
        new_list.append(item)
    except OwnError as err:
        print(err)

print(new_list)

