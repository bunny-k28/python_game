from random import *
from ascii_code import playerLife

life = 0  # player's life
life_flag = 6
player2_word = ''
player1_word = input('enter any word for player 2: ')


# loop fir making word blank
for i in player1_word:
    player2_word += '_ '

# creates a dynamic variables
blank_list = player2_word.split()

# random pos for hint assigning
for j in range(len(player1_word) // 2):
    hint_pos = randint(1, len(player1_word))
    blank_list.pop(hint_pos - 1)
    blank_list.insert(hint_pos - 1, player1_word[hint_pos - 1])

print('\n'*100)  # to clear the window
print(f'total life: {life_flag}')

# main loop/main program
while True:
    player2_word = ''
    print(playerLife[life], '\n\n')
    for k in blank_list:
        print(k, end='')
    print('\n')
    player2_alpha_input = input('alphabet (or type "exit" to exit the porg): ')

    if player2_alpha_input == 'exit':
        print('GAME EXITED')
        break

    player2_pos_input = int(input('enter the pos of alpha: '))
    print()

    if player1_word[player2_pos_input - 1] == player2_alpha_input:
        blank_list.pop(player2_pos_input - 1)
        blank_list.insert(player2_pos_input - 1, player2_alpha_input)
        for l in blank_list:
            player2_word += l

        if (len(player2_word) == len(player1_word)) and (player2_word == player1_word):
            print(player2_word)
            print('you guessed the correct word')
            print('congo, you won')
            break


    else:
        life += 1
        life_flag -= 1
        print(f'wrong guess, now you have {life_flag} life')
        try:
            pass
        except IndexError as IE:
            print('your life, better luck for next time')
            print('GAME OVER')
            break