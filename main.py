# 1. Создайте программу для игры в ""Крестики-нолики"" при помощи виртуального окружения и PIP

# Основные этапы программы:
# 1. Распечатать доску.
# 2. Принять ввод от игрока.
# 3. Поместить маркеры игроков (X или О) на доску.
# 4. Проверить, выиграна ли игра, ничья или игра продолжается.
# 5. Повторять 3 и 4 шаги до тех пор пока игра не будет выиграна или будет ничья.
# 6. Спросить, хотят ли игроки продолжить игру.

# Шаг 1: Создать функцию, которая будет распечатывать игровую доску. Доска будет представлять
# из себя лист.

import random
from tqdm import tqdm


def display_board(board):
    print('\n'*100)
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')

# Шаг 2. Создать функцию, которая которая производит ввод данных с консоли первым игроком (X или O)
#  и присваивает ему введенный маркер, второму игроку присваивается противоположный маркер.


def player_input():
    '''
    Output = (Маркер первого игрока, Маркер второго игрока)
    '''

    marker = ''

    while marker != 'X' and marker != 'O':
        marker = input('Игрок 1, введите X или O: ').upper()

    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')

# Шаг 3. Cоздать функцию, которая принимает в качестве аргументов игровую доску в виде листа,
# маркер ("X" или "O") и желаемую позицию (от 1 до 9) и помещает его на игровую
# доску.


def place_marker(board, marker, position):
    board[position] = marker

# Шаг 4. Cоздать функцию, которая принимает в качестве аргументов игровую доску в виде листа,
#  маркер ("X" или "O") и проверяет текущую ситуацию на выигрыш/ничью.


def win_check(board, mark):
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or  # across the top
            # across the middle
            (board[4] == mark and board[5] == mark and board[6] == mark) or
            # across the bottom
            (board[1] == mark and board[2] == mark and board[3] == mark) or
            # down the middle
            (board[7] == mark and board[4] == mark and board[1] == mark) or
            # down the middle
            (board[8] == mark and board[5] == mark and board[2] == mark) or
            # down the right side
            (board[9] == mark and board[6] == mark and board[3] == mark) or
            # diagonal
            (board[7] == mark and board[5] == mark and board[3] == mark) or
            (board[9] == mark and board[5] == mark and board[1] == mark))  # diagonal

# Шаг 5. Cоздать функцию, которая случайно определит какой игрок будет играть первым.


def choose_first():

    flip = random.randint(0, 1)

    if flip == 1:
        return 'Игрок 1'
    else:
        return 'Игрок 2'

# Шаг 6. Cоздать функцию, которая проверяет сводобно ли место на доске.


def space_check(board, position):
    return board[position] == ' '

# Шаг 7. Cоздать функцию, которая проверяет заполнена ли доска.


def full_board_check(board):
    for i in tqdm(range(1, 10)):
        if space_check(board, i):
            return False
    return True

# Шаг 8. Cоздать функцию, которая просит игрока ввести следующую позицию (от 1 до 9) и затем
# использовать функцию с шага № 6, чтобы проверить свободно ли место на доске.
# Если оно свободно, что возвращаем эту позицию для дальнейшего использования.


def player_choice(board):
    position = 0

    while position not in list(range(1, 10)) or not space_check(board, position):
        position = int(input("Выберите позицию: (1-9) "))

    return position

# Шаг 9. Cоздать функцию, которая cпросит игрока, хочет ли он сыграть еше раз.


def replay():
    return input('Хотите сыграть еще раз?: ').lower().startswith('д')

# Шаг 10. Игра.


while True:
    the_board = [' ']*10
    player_1_marker, player_2_marker = player_input()

    turn = choose_first()
    print(turn + ' будет ходить первым.')

    play_game = input("Готов играть? да или нет? ")

    if play_game == 'да':
        game_on = True
    else:
        game_on = False

    while game_on:

        if turn == 'Player 1':
            # Показываем доску
            display_board(the_board)

            # Игрок 1 выбирает позицию
            position = player_choice(the_board)

            # Ставим маркет на позиции, которую игрок выбрал
            place_marker(the_board, player_1_marker, position)

            # Проверяем, есть ли выигрыш
            if win_check(the_board, player_1_marker):
                display_board(the_board)
                print("Игрок 1 выиграл!")
                game_on = False
            # или ничья
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print("Ничья!")
                    game_on = False
                # Нет победы и ничьи? Тогда черёд следующего игрока
                else:
                    turn = 'Player 2'

        else:
            # Показываем доску
            display_board(the_board)

            # Игрок 2 выбирает позицию
            position = player_choice(the_board)

            # Ставим маркет на позиции, которую игрок выбрал
            place_marker(the_board, player_2_marker, position)

            # Проверяем, есть ли выигрыш
            if win_check(the_board, player_2_marker):
                display_board(the_board)
                print("Игрок 2 выиграл!")
                game_on = False
            # или ничья
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print("Ничья!")
                    game_on = False
                # Нет победы и ничьи? Тогда черёд следующего игрока
                else:
                    turn = 'Player 1'

    if not replay():
        break
