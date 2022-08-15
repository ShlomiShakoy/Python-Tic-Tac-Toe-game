import os
board=['1','2','3','4','5','6','7','8','9']
count=[]
player1wins=[]
player2wins=[]
def display():
    os.system('cls')
    print('Player 1 is: X')
    print('Player 2 is: O\n')
    print(f' {board[0]}   |   {board[1]}   |   {board[2]}')
    print('-----|-------|-----')
    print(f' {board[3]}   |   {board[4]}   |   {board[5]}')
    print('-----|-------|-----')
    print(f' {board[6]}   |   {board[7]}   |   {board[8]}\n')
    print(f'Player 1 wins: {len(player1wins)}')
    print(f'Player 2 wins: {len(player2wins)}\n')
def choice(player):
    result=""
    correct=True
    while correct:
        if player=='1':
            result=input(f'Player {player} please enter your square: ')
            if result.isdigit():
                result_int=int(result)
                if result_int in range(1,10):
                    if board[result_int - 1] != 'X' and board[result_int - 1] != 'O':
                        correct = False
                        board[result_int-1]='X'
                        player='2'
                        count.append('1')
                    else:
                        print('Wrong choice, this place is not empty!')
                        correct = True
                        player='1'
                else:
                    print(f"Player {player}, the number is not in the range(1-9)!")
                    correct = True
                    player='1'
            else:
                print("It's not a number!")
        elif player == '2':
            result = input(f'Player {player} please enter your square: ')
            if result.isdigit():
                result_int = int(result)
                if result_int in range(1,10):
                    if board[result_int-1]!='X' and board[result_int-1]!='O':
                        correct = False
                        board[result_int - 1] = 'O'
                        player = '1'
                        count.append('2')
                    else:
                        print('Wrong choice, this place is not empty!')
                        correct = True
                        player='2'
                else:
                    print(f"Player {player}, the number is not in the range(1-9)!")
                    correct = True
                    player='2'
            else:
                print("It's not a number!")
    if (board[0]=='X' and board[1]=='X' and board[2]=='X') or (board[0]=='X' and board[3]=='X' and board[6]=='X') or (board[0]=='X' and board[4]=='X' and board[8]=='X') or(board[1]=='X' and board[4]=='X' and board[7]=='X') or (board[2]=='X' and board[5]=='X' and board[8]=='X')or (board[2]=='X' and board[4]=='X' and board[6]=='X')or (board[3]=='X' and board[4]=='X' and board[5]=='X') or(board[5]=='X' and board[4]=='X' and board[3]=='X')or (board[6]=='X' and board[7]=='X' and board[8]=='X'):
        display()
        print('Player 1 is the winner!')
        player1wins.append('1')
        return False
    elif (board[0]=='O' and board[1]=='O' and board[2]=='O') or (board[0]=='O' and board[3]=='O' and board[6]=='O') or (board[0]=='O' and board[4]=='O' and board[8]=='O') or(board[1]=='O' and board[4]=='O' and board[7]=='O') or (board[2]=='O' and board[5]=='O' and board[8]=='O')or (board[2]=='O' and board[4]=='O' and board[6]=='O')or (board[3]=='O' and board[4]=='O' and board[5]=='O') or(board[5]=='O' and board[4]=='O' and board[3]=='O')or (board[6]=='O' and board[7]=='O' and board[8]=='0'):
        display()
        print('Player 2 is the winner!')
        player2wins.append('2')
        return False
    if len(count)==9:
        print('Even result!')
        return False
    return True
def check_winner():
    player='1'
    while choice(player):
        if player=='1':
            player='2'
        elif player=='2':
            player='1'
        display()
    reset_game=""
    while not reset_game.isdigit():
        reset_game=input('Press either 1 to reset the game or other key for exit: ')
        if reset_game.isdigit():
            reset_game_int=int(reset_game)
            if reset_game_int==1:
                board[0] = '1'; board[1] = '2'; board[2] = '3'; board[3] = '4'; board[4] = '5'; board[5] = '6'; board[6] = '7'; board[7] = '8'; board[8] = '9';
                count.clear()
                display()
                check_winner()
            else:
                print('Thanks for playing!')
        else:
            print('Thanks for playing!')

display()
check_winner()