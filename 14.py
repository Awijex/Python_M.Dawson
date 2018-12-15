# Receive_and_return
# Демонстрация параметров возвращения


def display(message):
    print(message)


def give_me_five():
        five = 5
        return five


def ask_yes_no(question):
    """Задает вопрос с ответом 'да' или 'нет'."""
    response = None
    while response not in ("y", "n"):
        response = input(question).lower()
    return response
    # основная часть


display("Вам сообщение.\n")
number = give_me_five()
print("Вот что возвратила функция give_me_five():", number)
answer = ask_yes_no("\nПожалуйста введите 'y' or 'n': ")
print("Thanks, that enter", answer)
input("\n\nPress enter, that quit.")





