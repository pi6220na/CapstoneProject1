# Capstone Project 1 - Simple Game: Rock, Paper, Scissors
# Jeremy Wolfe
# Jan 10, 2018

import random

ROCK = 1
PAPER = 2
SCISSORS = 3

# main loop controls the game flow
def main():
    try:
        user_choice = get_input()

        while (user_choice.lower() != 'q'):

            computer_pick = get_computer()
            user_num = int(user_choice)
            winner = determine_winner(user_num, computer_pick)
            output_computer_choice(computer_pick)
            print(winner)
            print('')
            user_choice = get_input()
    except Exception as err:
        print('An error ocurred. Error message: ', err)

# prints user choice menu and validates the input
def get_input():
    user_choice = ''

    while ( True ):

        print('Welcome to Rock-Paper-Scissors Game')
        print('     Select 1) for Rock')
        print('            2) for Paper')
        print('            3) for Scissors')
        print('            Q or q to quit')
        user_choice = input('Please make a selection: ')

        # ( user_choice.lower() != 'q' and not user_choice.isdigit() ):


        if (user_choice.lower() == 'q'):
            break

        if (user_choice.isdigit()):
            if (int(user_choice) < 1 or int(user_choice) > 3):
                print('')
                print('Error - must select number between 1 and 3')
            else:
                break

        print('')
        print('Error - invalid input, try again')
        print('')

    return user_choice

# pick a random integer between 1 and 3
def get_computer():
    # 1=rock, 2=paper, 3=scissors
    pick = random.randint(1,3)
    return pick

# the "brains" of the game - determine who won the game or if it's a tie
# see https://en.wikipedia.org/wiki/Rock%E2%80%93paper%E2%80%93scissors for game rules
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

# output the computer's choice in human readable format
def output_computer_choice(computer_pick):
    if (computer_pick == 1):
        print('Computer chose: Rock')
    if (computer_pick == 2):
        print('Computer chose: Paper')
    if (computer_pick == 3):
        print('Computer chose: Scissors')

    print('')

main()


