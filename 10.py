# Hero inventory
# Создадим список с несколькими эелементами и выведем его с помощью цикла for
inventory = ['меч', 'кольчуга', 'щит', 'целебное снадобье']
print("\nИтак в вашем арсенале:")
for item in inventory:
    print(item)
# найдем длину списка
print("Сейчас в вашем распоряжении", len(inventory), 'предмета(ов)')
# применение оператора in к спискам
if "целебное снадобье" in inventory:
    print("Вы еще будете жить и повоюете.")
# вывод одного элемента с определенным индексом
index = int(input("\nВведите индекс одного из предметов арсенала: "))
print("Под индексом", index, 'в арсенале находится', inventory[index])
# отобразим срез
start = int(input("\nВведите начальный индекс среза: "))
finish = int(input("Введите конечный индекс среза: "))
print("Срез inventory[", start, ":", finish, "] - это", end=" ")
print(inventory[start:finish])
# соединим два списка
chest = ['золото', 'драгоценные камни']
print("\nВы нашли сундучок. Вот его содержимое:")
print(chest)
print("Вы добавили содержимое ларца к своему арсеналу.")
inventory += chest
print("Теперь в вашем распоряжении:")
print(inventory)
# присваиваем значение элементу по индексу
print("Вы обменяли меч на арбалет.")
inventory[0] = "арбалет"
print("Теперь ваш арсенал содержит следующие предметы:")
print(inventory)
# приписываем значение элементам по срезу индексов
print("За золото и драгоценные камни вы купили магический кристалл,"
      "способный предсказывать будущее.")
inventory[4:6] = ["магический кристалл"]
print("Теперь в твоем распоряжении:")
print(inventory)
# удаляем элемент из списка
print("В тяжелом бою был раздроблен ваш щит.")
del inventory[2]
print("Вот что осталось в вашем арсенале:")
print(inventory)
# удаляем срез списка
print("Воры лишили вас арбалета и кольчуги.")
del inventory[:2]
print("В вашем арсенале только:")
print(inventory)
input('\n\nНажмите Enter, чтобы выйти.')