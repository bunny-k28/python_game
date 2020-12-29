# function to draw grid
def grid(list):
    for row in range(5):
        if row % 2 == 0:
            currentRow = row // 2
            for column in range(5):
                if column % 2 == 0:
                    currentColumn = column // 2
                    if column != 4:
                        print(list[currentRow][currentColumn], end='')
                    else:
                        print(list[currentRow][currentColumn], end='')
                        print()
                else:
                    print('|', end='')
        else:
            print('-----')

def winner():
    pass

# data unit
player = 1
flag = 1
markField = [[' ', ' ', ' '],
             [' ', ' ', ' '],
             [' ', ' ', ' ']]
grid(markField)
# game processor
while flag < 9:
    print(f'turn: player {player}\n')
    row = int(input('in which row you want to place the mark:- '))
    column = int(input('in which column you want to place the mark:- '))
    if player == 1:
        markField[row-1][column-1] = 'X'
        grid(markField)
        player += 1

    else:
        markField[row - 1][column - 1] = 'O'
        grid(markField)
        player -= 1

    flag += 1