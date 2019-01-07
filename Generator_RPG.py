# Напишите программу <<Генератор персонажей>> для ролевой игры. Пользователю должно быть
# предоставлено 30 пунктов, которые можно распределить между четырьмя характеристиками:
# Сила, Здоровье, Мудрость и Ловкость. Надо сделать так, чтобы пользователь мог не только
# брать эти пункты из общего <<пула>> , но и возвращать их туда из характеристик, которым
# он решит присвоить другие значения.


total_points = 30

skill_points = {"Strength": 0,
                "Hit_points": 0,
                "Wisdom": 0,
                "Agility": 0}

choice = None
while choice != 0:
    print("""
      Добро пожаловать в генератор персонажей!
      
      0 - выйти 
      1 - Показать оставшиеся очки улучшения
      2 - Добавить Силы 
      3 - Добавить Здоровья
      4 - Добавить Мудрости
      5 - Добавить Ловкости
      6 - Вернуть назад очки улучшения
      
    """)
    choice = int(input("Ваш выбор: "))
    print()
    if choice == 0:

        print("Пока")
        quit()
    elif choice == 1:
        print(total_points)
    elif choice == 2:
        skill_points["Strength"] += 1
        total_points -= 1
    elif choice == 3:
        skill_points["Hit_points"] += 1
        total_points -= 1
    elif choice == 4:
        skill_points["Wisdom"] += 1
        total_points -= 1
    elif choice == 5:
        skill_points["Agility"] += 1
        total_points -= 1



