# Capstone Project 1 - Simple Game: Rock, Paper, Scissors
# Jeremy Wolfe
# Jan 10, 2018

import random

ROCK = 1
PAPER = 2
SCISSORS = 3

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
    user_choice = ''

    while (user_choice.lower() != 'q' and not user_choice.isdigit()):
        print('Welcome to Rock-Paper-Scissors Game')
        print('     Select 1) for Rock')
        print('            2) for Paper')
        print('            3) for Scissors')
        print('             Q to quit')
        user_choice = input('Please make a selection: ')

        if (user_choice.lower() == 'q'):
            break

        if (user_choice.isdigit()):
            if (int(user_choice) < 1 or int(user_choice) > 3):
                print('Error - must select number between 1 and 3')
            else:
                break

    return user_choice

def get_computer():
    # 1=rock, 2=paper, 3=scissors
    pick = random.randint(1,3)
    return pick

def determine_winner(user, pc):
    # 1=rock, 2=paper, 3=scissors
    if user == pc:
        return "tie"

    if (user == ROCK and pc == PAPER):
        return 'computer wins - paper wraps rock'
    elif (user == ROCK and pc == SCISSORS):
        return 'player wins - rock breaks scissors'

    if (user == PAPER and pc == ROCK):
        return 'player wins - paper wraps rock'
    elif (user == PAPER and pc == SCISSORS):
        return 'computer wins - scissors cuts paper'

    if (user == SCISSORS and pc == ROCK):
        return 'computer wins - rock breaks scissors'
    elif (user == SCISSORS and pc == PAPER):
        return 'player wins - scissors cuts paper'

main()


