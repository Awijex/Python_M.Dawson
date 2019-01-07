# Обработка
# Демонстрация обработки исключительных ситуаций
# try/except

# обработка исключения определенного типа
# try:
#     num = float(input("\nВведите число: "))
# except ValueError:
#     print("Это не число!")

# обработка исключений разных типов
# print()
# for value in (None, "Привет!"):
#     try:
#         print("Пытаюсь преобразовать в число: ", value, "-->", end=" ")
#         print(float(value))
#     except (TypeError, ValueError):
#         print("Похоже, что это не число!")

# print()
# for value in (None, "Привет!"):
#     try:
#         print("Пытаюсь преобразовать в число:", value, "-->", end=" ")
#         print(float(value))
#     except TypeError:
#         print("Я умею преобразовывать только строки и числа!")
#     except ValueError:
#         print("Я умею преобразовывать только строки, составленные из цифр!")
#
#

# получение аргумента
try:
    num = float(input("\nВведите число: "))
except ValueError as e:
    print("Это не число! Интерпретатор как бы говорит нам:")
    print(e)

# try/except/else
try:
    num = float(input("\nВведите число: "))
except ValueError:
    print("Это не число!")
else:
    print("Вы ввели число", num)
input("\n\nНажмите Enter, чтобы выйти.")