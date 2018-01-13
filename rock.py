
# Capstone Project 1 - Simple Game: Rock-Paper-Scissors
# Jeremy Wolfe
# Jan 10, 2018

import random
import pprint

ROCK = 1
PAPER = 2
SCISSORS = 3
TESTRUN = 10000


# main loop controls the game flow
def main():
    #try:

        player_choice = get_input()

        while (player_choice.lower() != 'q'):

            if int(player_choice) == 4:
                run_auto_game_test()
                break

            computer_pick = get_computer_pick()
            winner = determine_winner(int(player_choice), computer_pick)
            display_computer_choice(computer_pick)
            print(winner)
            print('')
            player_choice = get_input()

        print('')
        print('Thanks for playing')
        print('')

    #except Exception as err:

    #    print('An error occurred. Error message: ', err)


# prints player choice menu and validates the input
def get_input():

    player_choice = ''

    while ( True ):

        print('Welcome to Rock-Paper-Scissors Game')
        print('     Select 1) for Rock')
        print('            2) for Paper')
        print('            3) for Scissors')
        print('            4) to run automatic game loop')
        print('            Q or q to quit')
        player_choice = input('Please make a selection: ')

        if (player_choice.lower() == 'q'):
            break

        if (player_choice.isdigit()):
            if (int(player_choice) < 1 or int(player_choice) > 4):
                print('')
                print('Error - must select number between 1 and 4')
                print('')
            else:
                break
        else:
            print('')
            print('Error - enter 1, 2, 3, or 4, or q to quit')
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

def run_auto_game_test():
    loopCount = 0
    # use a dictionary to hold win/loss counts and stats
    player1 = { 'tie':0 , 'win':0, 'loss':0, 'rock':0, 'paper':0, 'scissors':0 }
    player2 = { 'tie':0 , 'win':0, 'loss':0, 'rock':0, 'paper':0, 'scissors':0 }

    while loopCount < TESTRUN:

        player1_choice = get_computer_pick()
        player2_choice = get_computer_pick()
        winner = determine_winner(player1_choice, player2_choice)


        #if 'rock' in winner:
        #    print('winner has a rock in the string')
        #if winner[26:34] == 'scissors':
        #    print('winner has a scissors in the string')
        #print(winner[16:24])
        #if 'paper' in winner:
        #    print('winner has a paper in the string')


        if winner[0:4] == 'tie':
            player1['tie'] += 1
            player2['tie'] += 1


        if winner[0:6] == 'player':
            #print('winner = player')
            player1['win'] += 1
            player2['loss'] += 1
            if 'rock' in winner:
                player1['rock'] = player1['rock'] + 1
            if 'paper' in winner:
                player1['paper'] = player1['paper'] + 1
            #if winner[26:34] == 'scissors':
            if 'scissors' in winner:
                player1['scissors'] = player1['scissors'] + 1
                #print('                         added one to scissors')

        if winner[0:8] == 'computer':
            #print('winner = computer')
            player2['win'] = player2['win'] + 1
            player1['loss'] += 1
            if 'rock' in winner:
                player2['rock'] = player2['rock'] + 1
            if 'paper' in winner:
                player2['paper'] = player2['paper'] + 1
            if 'scissors' in winner:
                player2['scissors'] = player2['scissors'] + 1


        loopCount += 1

    pp = pprint.PrettyPrinter(indent=4)
    print('player1 = ')
    pp.pprint(player1)
    #print(player1)
    print('player2 = ')
    pp.pprint(player2)
    #print(player2)


main()
