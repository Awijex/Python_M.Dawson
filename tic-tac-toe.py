# Псевдокод:
# Вывести на экран инструкции для игрока
# решить, кому принадлежит ход первым
# создать пустую доску для игры в "Крестики-нолики"
# отобразить доску
# до тех пор пока никто не выиграл или не стостоялась ничья
#       если сейчас ход пользователя
#             получить ход из пользовательского ввода
#             изменить вид доски
#       иначе
#           рассчитать ход компьютера
#           изменить вид доски
#       вывести на экран обновленный вид доски
#       осуществить переход хода
# поздравить победителя или констатировать ничью

# Крестики нолики
# Компьютер играет в крестики-нолики против пользователя
# глобальный константы
X = "X"
O = "O"
EMPTY = " "
TIE = "TIE"
NUM_SQUARES = 9


def display_instruct():
    """Выводит на экран инструкцию для игрока."""
    print(
        """
        Добро пожаловать на ринг самых беспощадных интеллектуальных состязаний всех
        времен.
        Твой мозг и мой процессор сойдутся в схватке за доской игры "Крестики-нолики"
        
        Чтобы сделать ход, введи число от 0 до 8. Числа однозначно соответствуют полям
        доски - так, как показано ниже:
        0 | 1 | 2
        - - - - - 
        3 | 4 | 5
        - - - - - 
        6 | 7 | 8
        Приготовься к бою, жалкий белковый человечишка. Вот-вот начнется рещающее сражение.\n   """
        )


def ask_yes_no(question):
    """Задает вопрос с ответом "Да" или "Нет"."""
    response = None
    while response not in ("y", "n"):
        response = input(question).lower()
    return response


def ask_number(question, low, high):
    """Просит ввести число из диапазона."""
    response = None
    while response not in range(low, high):
        response = int(input(question))
    return response


def pieces():
    """Определяет кто ходит первым."""
    go_first = ask_yes_no("Do you require the first move? (y/n): ")
    if go_first == "y":
        print("\nThen take the first move.  You will need it.")
        human = X
        computer = O
    else:
        print("\nYour bravery will be your undoing... I will go first.")
        computer = X
        human = O
    return computer, human


def new_board():
    """Создает игровую доску."""
    board = []
    for square in range(NUM_SQUARES):
        board.append(EMPTY)
    return board


def display_board(board):
    """Покащзывает игровую доску."""
    print("\n\t", board[0], "|", board[1], "|", board[2])
    print("\t", "---------")
    print("\t", board[3], "|", board[4], "|", board[5])
    print("\t", "---------")
    print("\t", board[6], "|", board[7], "|", board[8], "\n")


def legal_moves(board):
    """Создавет список доступных ходов."""
    moves = []
    for square in range(NUM_SQUARES):
        if board[square] == EMPTY:
            moves.append(square)
    return moves


def winner(board):
    """Определяет победителя."""
    WAYS_TO_WIN = ((0, 1, 2),
                   (3, 4, 5),
                   (6, 7, 8),
                   (0, 3, 6),
                   (1, 4, 7),
                   (2, 5, 8),
                   (0, 4, 8),
                   (2, 4, 6))

    for row in WAYS_TO_WIN:
        if board[row[0]] == board[row[1]] == board[row[2]] != EMPTY:
            winner = board[row[0]]
            return winner

    if EMPTY not in board:
        return TIE

    return None


def human_move(board, human):
    """Получает ход человека."""
    legal = legal_moves(board)
    move = None
    while move not in legal:
        move = ask_number("Твой ход. Выбери одно из полей (0 - 8):", 0, NUM_SQUARES)
        if move not in legal:
            print("\nСмешной человек! Это поле уже занято. Выбери плиз"
                  "другое.\n")
    print("Ладно...")
    return move


def computer_move(board, computer, human):
    """Получает ход компьютера"""
    # создадим рабочую копью доски, чтобы функция меняла некоторые значения в списке
    board = board[:]
    # поля от лучшего к худшему
    BEST_MOVES = (4, 0, 2, 6, 8, 1, 3, 5, 7)
    print("I shall take square number", end=" ")
    # если компьютер победит, выбрать этот ход
    for move in legal_moves (board):
        board[move] = computer
        if winner(board) == computer:
            print(move)
            return move
        # выполнить проверку данного хода
        board[move] = EMPTY
    # если победит человек, блокировать данный ход
    for move in legal_moves (board):
        board[move] = human
        if winner (board) == human:
            print (move)
            return move
        # выполнить проверку хода, отменить изменения
        board[move] = EMPTY
    # выбрать лучший ход из всех доступных, при условии, если никто не победит
    for move in BEST_MOVES:
        if move in legal_moves (board):
            print(move)
            return move


def next_turn(turn):
    """Осуществляет переход хода."""
    if turn == X:
        return O
    else:
        return X


def congrat_winner(the_winner, computer, human):
    """Поздравляет игрока с победой."""
    if the_winner != TIE:
        print("Три", the_winner, "в ряд!\n")
    else:
        print("Ничья!\n")
    if the_winner == computer:
        print("Как я и предсказывал, победа далась мне слишком легко, знай, тебе никогда"
              "не одалеть меня!\n")
    elif the_winner == human:
        print("О нет, этого не может быть! Неужели ты как-то сумел перехитрить меня,"
              "жалкий человечишка?\n"
              "Клянусь, что я больше не допущу подобного!")
    elif the_winner == TIE:
        print("Тебе несказанно повезло, дружок: ты сумел свести игру вничью, \n"
              "Радуйся же сегодняшнему успеху! В следующей игре тебе суждено проиграть.")


def main():
    display_instruct()
    computer, human = pieces()
    turn = X
    board = new_board()
    display_board(board)
    while not winner(board):
        if turn == human:
            move = human_move(board, human)
            board[move] = human
        else:
            move = computer_move(board, computer, human)
            board[move] = computer
        display_board(board)
        turn = next_turn(turn)
    the_winner = winner(board)
    congrat_winner(the_winner, computer, human)


# запуск программы
main()
input("\n\nPress the enter key to quit.")















