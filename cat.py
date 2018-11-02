from random import randint

class Cat:

    def __init__(self, name):
        self.name = name
        self.mood = 100
        self.fulness = 50
        self.home = None


    def __str__(self):
        return f'Я - {self.name}, настроение - {self.mood}, сытость - {self.fulness}'

    def eat(self):
        if self.home is None:
            print(f'Я {self.name} нет дома...')
        else:
            self.home.cat_bowl -=10
            self.fulness += 30
            print(f'{self.name} вкусно поел...')

    def settle_in_the_house(self, house):
        self.home = house
        print (f'{self.name} вселился в дом')

    def sleep(self):
        self.fulness -= 20
        print(f'{self.name} спал весь день')

    def act(self):
        if self.fulness <= 0:
            print(f'{self.name} умер... ')
            return
        dice = randint(1, 6)
        if dice == 1:
            self.eat()
        else:
            self.sleep()



class House:

    def __init__(self):
        self.cat_bowl = 50


catyara = Cat(name="Кошак")
print(catyara)
catyara.eat()
my_home = House()
catyara.settle_in_the_house(house = my_home)
catyara.eat()
print(catyara)
catyara.sleep()
print(catyara)

for day in range(1, 30):
    print(f'****************** день{day}')
    catyara.act()
    if catyara.fulness <= 0:
       print(f'{catyara.name} мертв!')
       break

    print(catyara)