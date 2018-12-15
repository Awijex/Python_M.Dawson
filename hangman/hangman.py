# Виселица
# by Лешка
# Классическая игра "Виселица". Компьютер случайным образом выбирает слово.
# которое игрок должен отгадать буква за буквой. Если игрок не сумеет
# отгадать за отведенное количество попыток, на экране появится фигурка повешенного.
# импорт модуля
import random
import time
import PyInstaller
# константы
HANGMAN = ("""
    ------
    |     |
    |
    |
    |
    |
    |
    ---------
    """, """
    ------
    |     |
    |     0  
    |
    |
    |
    |
    ---------
    """, """
    ------
    |     |
    |     0    
    |    -+-
    |
    |
    |
    ---------
    """, """
    ------
    |     |
    |     0    
    |   /-+-
    |
    |
    |
    ---------
    """, """
    ------
    |     |
    |     0    
    |   /-+-/
    |
    |
    |
    ---------
    """, """
    ------
    |     |
    |     0    
    |   /-+-/
    |     |
    |
    |
    ---------
    """, """
    ------
    |     |
    |     0  
    |   /-+-/
    |    || 
    |    |
    |    
    ---------
    """, """
    ------
    |     |
    |     0    
    |   /-+-/
    |    |||
    |    | |
    |    
    ---------
    """)
MAX_WRONG = len(HANGMAN) - 1
WORDS = ("ПИТОН", "АРХАНГЕЛЬСК", "ДЖОДЖО", "ПРИВЕТ", "ВИСЕЛИЦА", "ПРЕДЕЛ", "ЛЕША", "ПРОГРАММИСТ", "АНИМЕ")
# инициализация переменных
word = random.choice (WORDS)  # слово для отгадывания
so_far = "-" * len (word)  # по одному дефису на каждую букву, которую надо отгадать
wrong = 0  # количество ошибок, которые сделал игрок
used = []  # буквы, которые игрок уже предлагал
time.sleep(1)
print ("""
╔╗╔╗╔═╔╗╔╗
║║║║╠╗║║║║
╩╩╚╝╚╝╠╝╚╝

╔╗╔╗╗║╔╔╗╔╗╔╗╦╗╔╗╦╠╗ ╦╗
║║║║╠╬╣╠╣║║║║╠╣╠╣║║║ ╠╣
║║╚╝╝║╚║║╝║╚╝╩╝║║║╚╝ ╩╝

║║╔╔╗║║ ╦╗║║╔╔═╔╗║║║║╔╗
║║║║║╚╣ ╠╣║║║╠═║║║║║║╠╣
╚╝║╠╝═╝ ╩╝╚╝╚╚═╝║╚╝╚╩║║   

║║╔╗╔╗║║║║ ╦╗╔╗╔╦╗
╚╣║║╠╣║║║║ ╠╣╠╣║║║ 
═╝╩╩║║╚╣╚╝ ╩╝║║║║║    
""")
time.sleep(1)
while wrong < MAX_WRONG and so_far != word:
    print(HANGMAN[wrong])
    print("\n Ты использовал следующие буквы", used)
    print("\n Загаданное слово выглядит так:", so_far)

    guess = input("\n\nВведите букву: ")
    guess = guess.upper()

    while guess in used:
        print("Ты уже использовал букву", guess)
        guess =input("Введите букву: ")
        guess = guess.upper()

    used.append(guess)

    if guess in word:
        print("Да, буква", guess,  "содержится в слове")

        new = ""

        for i in range(len(word)):
            if guess == word[i]:
                new += guess
            else:
                new += so_far[i]
        so_far = new
    else:
        print("Извини, но буквы", guess, "нету в этом слове")
        wrong += 1

if wrong == MAX_WRONG:
    print(HANGMAN[wrong])
    print ("\nТы был повешен")
else:
    print ("\nТы справился!")

print ("\nЗагаданное слово выглядело вот так", word)

input ("\n\nНажмите enter, чтобы выйти.")
