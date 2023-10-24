import random as rnd

a = [" "," "," "," "," "," "," "," "," "]
comp_available = [1,2,3,4,5,6,7,8,9]
def print_board():
    print(" "+a[0]+" | "+a[1]+" | "+a[2])
    print("---+---+---")
    print(" "+a[3]+" | "+a[4]+" | "+a[5])
    print("---+---+---")
    print(" "+a[6]+" | "+a[7]+" | "+a[8])
board = a




while " " in board:
    player = int(input("Enter your move from 1-9: "))
    board[player-1] = "X"
    comp_available.remove(player)
    if comp_available != []:
        comp= rnd.choice(comp_available)
        comp_available.remove(comp)
        board[comp-1] = "O"
    else:
        print("Its a Tie")
    print_board()

