total_points = 0
skill_points = []


def generator_skills(skill):
    global total_points
    global skill_points
    skill_points[skill][1] += 1
    total_points -= 1



def greeting():
    global total_points
    global skill_points
    print("""
          Добро пожаловать в генератор персонажей!

          0 - выйти 
          1 - Показать оставшиеся очки улучшения
          2 - Добавить Силы 
          3 - Добавить Здоровья
          4 - Добавить Мудрости
          5 - Добавить Ловкости
          6 - Вернуть назад очки улучшения
          7 - Показать таблицу скиллов
        """)


def initialize():
    global total_points
    global skill_points
    total_points = 30
    skill_points = [
         ["Strength", 0],
         ["Hit_Points", 0],
         ["Wisdom", 0],
         ["Agility", 0]
    ]

def show_skills():
    global skill_points

    for skill in skill_points:
        print (f"\n\n\t{skill[0]} = {skill[1]}")



def main():
    global total_points
    global skill_points
    greeting()
    initialize()
    choice = -1
    while choice != 0:
        choice = -1
        if total_points <= 0:
            print("Вы израсходовали все очки прокачки")
            continue
        choice = int(input("Ваш выбор: "))
        if choice == 1:
            print(total_points)
        elif 1 < choice < len(skill_points) + 2:
            generator_skills(skill=choice - 2)
        elif choice == 7:
            print(show_skills())
        else:
            print("Некорректный ввод")


    print("Poka")




if __name__ == "__main__":
    main()
