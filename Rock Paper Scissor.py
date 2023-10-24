# Date of creation: 30th Dec 2022
# source: self (topic from web)
#

import random

computer = ['rock', 'paper', 'scissors']


def players_choice():
    while True:
        player = input("~Choose between rock/paper/scissors: ")
        if player == 'r':
            player = 'rock'
            print('You chose rock')
            break
        elif player == 'p':
            player = 'paper'
            print('You chose paper')
            break
        elif player == 's':
            player = 'scissors'
            print('You chose scissors')
            break
        elif player == 'q':
            break
        else:
            print('Please choose between r/p/s')
    return player


def computers_choice():
    computer_choice = random.choice(computer)
    print(f"Computer chose {computer_choice}")
    return computer_choice


def decision1(plc, cmc):
    if plc == cmc:
        return '***Its a TIE***'
    elif plc == 'rock':
        if cmc == 'scissors':
            return "***You WON***"
        else:
            return "***You LOST***"
    elif plc == 'paper':
        if cmc == 'rock':
            return "***You WON***"
        else:
            return "***You LOST***"
    elif plc == 'scissors':
        if cmc == 'paper':
            return "***You WON***"
        else:
            return "***You LOST***"


def main():
    inp = input(
        f"Welcome to Rock, Paper, Scissors\nPress enter to play (press 'q' to quit at any point) :")
    player_score = 0
    computer_score = 0
    while True:
        if inp == 'q':
            print("Bye!")
            break
        else:
            ply = players_choice()
            if ply == 'q':
                print("You chose to quit, Bye!")
                break
            else:
                comp = computers_choice()
                result = decision1(ply, comp)
                if result == "***You WON***":
                    player_score += 1
                elif result == "***You LOST***":
                    computer_score += 1
                else:
                    player_score += 0
                    computer_score += 0
                print(
                    f"{result} \n>>Your score is: {player_score} \n>>Computers Score is: {computer_score}\n ")


main()
