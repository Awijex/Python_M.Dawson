#nasted = ["раз", ("два","три"), ["четыре", "пять", "шесть"]]
#print(nasted)
# scores = [("Маша", 1000),("Вася", 1500),("Петя", 3000)]
# print(scores[0])
# a_scores = scores[2]
# print(a_scores)
# print(a_scores[0])
# print(scores[2][0])
# name, score = ("Иван Иванович", 175)
# print(name)
# print(score)
# Рекорды 2.0
# Демонстрация вложенных последовательностей
scores = []
choice = None
while choice != 0:
    print(
        """
        Рекорды 2.0
        0 - выйти
        1 - показать рекорды
        2 - добавить рекорд
        """
          )
    choice = input("Ваш выбор: ")
    print()
    # выход
    if choice == "0":
        print("До свидания")
    # вывод таблицы рекордов
    elif choice == "1":
        print("Рекорды\n")
        print("Имя\tРезультат")
        for entry in scores:
            score, name = entry
            print(name, "\t", score)

        # add a score
    elif choice == "2":
        name = input("Впишите имя игрока: ")
        score = int(input("Впишите его результат: "))
        entry = (score, name)
        scores.append(entry)
        scores.sort(reverse=True)
        scores = scores[:5] #в списке остается только 5 рекордов

    # непонятный пользовательский ввод
    else:
        print("Извините, в меня нет пункта", choice)

    input("\nНажмите Enter, чтобы начать снова.")

input("\nEnter, для выхода.")


