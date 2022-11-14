def display(board):
    print(board[1], ' | ', board[2], ' | ', board[3])
    print('--------------')
    print(board[4], ' | ', board[5], ' | ', board[6])
    print('--------------')
    print(board[7], ' | ', board[8], ' | ', board[9])


def clear_display():
    for clr in range(1, 10):
        board[clr] = ' '


def check_winner(selection):
    a1 = range(1, 4)
    a2 = range(4, 7)
    a3 = range(7, 10)
    b1 = range(1, 8, 3)
    b2 = range(2, 9, 3)
    b3 = range(3, 10, 3)
    c1 = range(1, 10, 4)
    c2 = range(3, 8, 2)
    check_list = [a1, a2, a3, b1, b2, b3, c1, c2]

    if selection in ['X', 'x']:
        check_value1 = 'X'
        check_value2 = 'O'
    elif selection in ['O', 'o']:
        check_value1 = 'O'
        check_value2 = 'X'

    result = 0

    for a, b, c in check_list:
        if board[a] == check_value1 and board[b] == check_value1 and board[c] == check_value1:
            print('Winner : PLAYER 1')
            result = player_selection(result)

        elif board[a] == check_value2 and board[b] == check_value2 and board[c] == check_value2:
            print('Winner : PLAYER 2')
            result = player_selection(result)


def player_selection(result):
    print('\nPlayer 1:\nPlayer 1 will start playing first:')
    selection = input('Choose X or O to start playing')

    if selection in ['X', 'x']:
        assign_p1 = 'X'
        assign_p2 = 'O'
    elif selection in ['O', 'o']:
        assign_p1 = 'O'
        assign_p2 = 'X'

    clear_display()

    list1 = []
    list2 = []

    result = 0

    # PLAYER 1:
    for player1 in range(0, 5):
        while result != 1:
            choice1 = int(input(f'\nSelect a number in (1-9) to fill : {assign_p1} :'))
            list = list1 + list2

            if choice1 in range(1, 10):
                if choice1 not in list:
                    board[choice1] = assign_p1
                    display(board)
                    check_winner(selection)

                    player1 += 1
                    if player1 == 5:
                        if result == 0:
                            print('The Match is Draw\nGame Over')
                            result = player_selection(result)
                            exit()
                    break
                else:
                    print('You have entered an already existing value, Please enter again')
            else:
                print('Enter between 1 - 9')
        list1.append(choice1)

        # PLAYER 2

        while result != 1:
            choice2 = int(input(f'\nSelect a number in (1-9) to fill : {assign_p2} :'))
            list = list1 + list2

            if choice2 in range(1, 10):
                if choice2 not in list:
                    board[choice2] = assign_p2
                    display(board)
                    check_winner(selection)
                    break
                else:
                    print('You have entered an already existing value, Please enter again')
            else:
                print('Enter between 1 - 9')


board = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
display(board)
result = 0
player_selection(result)
