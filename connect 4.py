# modules
from termcolor import *


# function for making grid
def grid(store):
    for row in range(9):
        for column in range(19):
            if column % 2 == 0:
                current_column = column // 2
                if column != 18:
                    cprint(store[row][current_column], None, 'on_cyan', attrs=['bold'],  end='')
                else:
                    print()
            else:
                cprint('|', 'green', 'on_cyan', attrs=['bold'], end='')


# function for deciding the winner
def winner(value):
    p1_check_list = []
    p2_check_list = []
    for i in value:
        for j in i:
            if j == p1_color:
                lane = i.index(j)
                p1_check_list.append(lane)
            elif j == p2_color:
                lane = i.index(j)
                p2_check_list.append(lane)

    # print(check_list)
    if (p1_check_list == sorted(p1_check_list)) and (len(p1_check_list) == 4):
        print(f'{p1_name} is the winner of this game, congo!')
    elif (p2_check_list == sorted(p2_check_list)) and (len(p2_check_list) == 4):
        print(f'{p2_name} is the winner of this game, congo!')
    else:
        print('no one is the winner')


markLib = [
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]

# game info inputs
player = 1
flag = 1
finish_value = int(input('with how many pieces you want to play the game:- '))
if finish_value < 4:
    print('required more than this')
    finish_value = int(input('with how many pieces you want to play the game:- '))
else:
    print('WELCOME TO CONNECT 4\n')
p1_name = str(input('player 1 name:- '))
p2_name = str(input('player 2 name:- '))


# player's color
p1_color = colored(' ', None, 'on_grey')
p2_color = colored(' ', None, 'on_yellow')


# game info
print('\n\t\t\t\t\tSTART')
print('Game info:-\n\t\t1.Place your marks by entering the row and column number.\n\t\t2.Here rows are '
      'horizontally and columns are vertically placed.\n\t\t3.The first player to get 4 across or '
      'diagonal should win!\n\t\t4.This game starts from bottom.\n')


# main
grid(markLib)
while flag <= finish_value * 2:
    print()
    print(f'player: {player}')
    rowNum = int(input('enter row no.:- '))
    columnNum = int(input('enter column no.:- '))
    if player == 1:
        markLib[-rowNum][columnNum - 1] = p1_color
        grid(markLib)
        player += 1

    else:
        markLib[-rowNum][columnNum - 1] = p2_color
        grid(markLib)
        player -= 1

    flag += 1

winner(markLib)