# Просто зверюшка
# Демонастрация работы простейшего класса и объекта


class Critter(object):  # объявление класса
    """Виртуальный питомец"""
    def talk(self):  # объявление метода
        print("Привет, Я зверюшка - экземпляр класса Critter.")

# основная часть


crit = Critter()  # создание объекта класса
crit.talk()  # вызов метода класса
input("\nНажмите Enter, чтобы выйти.")