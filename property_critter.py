# Зверюшка со свойствами
# Демонстрирует свойства


class Critter(object):
    """Виртуальный питомец"""

    def __init__(self, name):
        print("Появилась на свет новая зверюшка!")
        self.__name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        if new_name == "":
            print("Имя зверюшки не может быть пустой строкой.")
        else:
            self.__name = new_name
            print("Имя успещно изменено.")

    def talk(self):
        print("\nПривет, меня зовут", self.name)


# основная часть

crit = Critter("Бобик")
crit.talk()
print("\nМою зверюшку зовут", end=" ")
print(crit.name)
print("\nПопробую изменить имя зверюшки на Мурзик...")
crit.name = "Мурзик"
print("\nМою зверюшку зовут", end=" ")
print(crit.name)
print("\nПопробую изменить имя зверюшки на пустую строку...")
crit.name = ""
print("\nМою зверюшку зовут", end=" ")
print(crit.name)
input("\n\nНажмите Enter, чтобы выйти.")
