# Capstone Project 1 - Simple Game: Rock, Paper, Scissors
# Jeremy Wolfe
# Jan 10, 2018

import random

def main():
    user_choice = get_input()

    while (user_choice.lower() != 'q'):

        computer_pick = get_computer()
        user_num = int(user_choice)
        winner = determine_winner(user_num, computer_pick)
        print('Computer chose: ' + str(computer_pick))
        print(winner)
        print('')
        user_choice = get_input()

def get_input():
    print('Welcome to Rock-Paper-Scissors Game')
    print('     Select 1) for Rock')
    print('            2) for Paper')
    print('            3) for Scissors')
    print('             Q to quit')
    user_choice = input('Please make a selection: ')

    return user_choice

def get_computer():
    # 1=rock, 2=paper, 3=scissors
    pick = random.randint(1,3)
    return pick

def determine_winner(user, pc):

    if user == pc:
        return "tie"

    if (user == 1 and pc == 2):
        return 'computer wins - paper wraps rock'
    elif (user == 1 and pc == 3):
        return 'player wins - rock breaks scissors'

    if (user == 2 and pc == 1):
        return 'player wins - paper wraps rock'
    elif (user == 2 and pc == 3):
        return 'computer wins - scissors cuts paper'

    if (user == 3 and pc == 1):
        return 'computer wins - rock breaks scissors'
    elif (user == 3 and pc == 2):
        return 'player wins - scissors cuts paper'

main()


