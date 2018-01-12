
# Capstone Project 1 - Simple Game: Rock-Paper-Scissors
# Jeremy Wolfe
# Jan 10, 2018

import random

ROCK = 1
PAPER = 2
SCISSORS = 3


# main loop controls the game flow
def main():
    try:

        player_choice = get_input()

        while (player_choice.lower() != 'q'):

            computer_pick = get_computer_pick()
            winner = determine_winner(int(player_choice), computer_pick)
            display_computer_choice(computer_pick)
            print(winner)
            print('')
            player_choice = get_input()

    except Exception as err:

        print('An error occurred. Error message: ', err)


# prints player choice menu and validates the input
def get_input():

    player_choice = ''

    while ( True ):

        print('Welcome to Rock-Paper-Scissors Game')
        print('     Select 1) for Rock')
        print('            2) for Paper')
        print('            3) for Scissors')
        print('            Q or q to quit')
        player_choice = input('Please make a selection: ')

        if (player_choice.lower() == 'q'):
            break

        if (player_choice.isdigit()):
            if (int(player_choice) < 1 or int(player_choice) > 3):
                print('')
                print('Error - must select number between 1 and 3')
            else:
                break

        print('')
        print('Error - invalid input, try again')
        print('')

    return player_choice


# pick a random integer between 1 and 3
def get_computer_pick():

    # 1=rock, 2=paper, 3=scissors
    pick = random.randint(1,3)
    return pick


# the "brains" of the game - determine who won the game or if it's a tie
# see https://en.wikipedia.org/wiki/Rock%E2%80%93paper%E2%80%93scissors for game rules
def determine_winner(player, pc):

    # 1=rock, 2=paper, 3=scissors
    if player == pc:
        return "tie"

    if (player == ROCK and pc == PAPER):
        return 'computer wins - paper wraps rock'
    elif (player == ROCK and pc == SCISSORS):
        return 'player wins - rock breaks scissors'

    if (player == PAPER and pc == ROCK):
        return 'player wins - paper wraps rock'
    elif (player == PAPER and pc == SCISSORS):
        return 'computer wins - scissors cuts paper'

    if (player == SCISSORS and pc == ROCK):
        return 'computer wins - rock breaks scissors'
    elif (player == SCISSORS and pc == PAPER):
        return 'player wins - scissors cuts paper'


# output the computer's choice in human readable format
def display_computer_choice(computer_pick):

    if (computer_pick == ROCK):
        print('Computer chose: Rock')
    if (computer_pick == PAPER):
        print('Computer chose: Paper')
    if (computer_pick == SCISSORS):
        print('Computer chose: Scissors')

    print('')


main()
