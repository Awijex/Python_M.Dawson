# Переводчик с гикского на русский Geek - человек повернутый, да, вы меня правильно поняли, повернутый, на какой-либо
#  одной тематике и который реально разбирается в ней, так что в какой-то мере задрот, но все же принятна называть
# такого человека гиком. Демонстрация использования словарей, создадим словарь geek >далее внесем в него ключи и
# значения. (вносим только те слова, которые нам необходимо будет перевести в дальнейшем на русский)
geek = {"404": "Не знать, не владеть информацией. От сообщения об ошибке 404('Страница не найдена'.)",
        "Googling": "'Гугление', поиск в Сети сведений о ком-либо, о чем-либо.",
        "Keyboard Plaque": "Мусор, который скапливается в клавиатуре компьютера.",
        "Link Rot": "Процесс устаревания гиперссылок на веб-страницах.",
        "Percussive Maintenance": "О ситуации, когда кто-либо бьет по корпусе исправного электронного прибора"
                                  "в надежде восстановить его работу.",
        "Uninstalled": "Об увольнении кого-либо. Особенно популярно на рубеже 1990-2000-х годов.",
        "Dancing Baloney": "Зарубежные копьютерщики так называют анимированную графику и другие визуальные"
                           "эффекты, неважные сами по себе, но часто применяемые веб-дизайнерами,чтобы"
                           "произвести впечатление на заказчика."}

choice = None
while choice != "0":

    print(""" 
    Переводчик с гикского на русский
    0 - Выйти
    1 - Найти толкование термина
    2 - Добавить термин
    3 - Изменить толкование
    4 - Удалить термин
    """)
    choice = input("Ваш выбор: ")
    print()
# выход из программы
    if choice == "0":
          print("До свидания. ")
# поиск толкования
    elif choice == "1":
        term = input("Какой термин вы хотите перевести с гикского на русский? ")
        if term in geek:
            definition = geek[term]
            print("\n", term, "означает", definition)
        else:
            print("\nУвы, этот термин мне незнаком:", term)
# добавление термина с толкованием
    elif choice == "2":

       term = input("Какой термин гикского языка вы хотите добавить? ")
       if term not in geek:
            definition = input("\nВпишите ваше толкование: ")
            geek[term] = definition
            print("\nТермин", term, "добавлен в словарь.")
       else:
        print("\nТакой термин уже есть! Попробуйте изменить его толкование.")

    # новое толкование известного нам термина
    elif choice == "3":
        term = input("Какой термин вы хотите переопределить? ")
        if term in geek:
             definition = input("Впишите ваше толкование")
             geek[term] = definition
             print("\nТермин", term, "переопределен.")
        else:
            print("\nТакого термина пока нет! Попробуйте добавить его в словарь.")

    # удаление существующего термина вместе с толкованием
    elif choice == "4":
        term = input("Какой термин вы хотите удалить? ")
        if term in geek:
            del geek[term]
            print("\nТермин", term, "удален.")
        else:
            print("\nНичем помочь не могу. Термина", term, "нет в словаре.")

    # непонятный пользовательский ввод
else:
    print("Извините, в меню нет пункта", choice)
input("\n\nНажмите Enter, чтобы выйти.")
