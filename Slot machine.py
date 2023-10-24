# Date of Creation: 29th Dec 2022
# source: YT
# self input: line 141

import random

MAX_LINES = 3
MAX_BET = 50
MIN_BET = 1

ROWS = 3
COLS = 3

symb_count = {
    'A': 22,
    "B": 4,
    "C": 6,
    "D": 8,
    "E": 3,
    "F": 10,
    "G": 16
}

symb_value = {
    'A': 4,
    "B": 8,
    "C": 6,
    "D": 15,
    "E": 30,
    "F": 5,
    "G": 10
}


def check_win(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for col in columns:
            symb_check = col[line]
            if symbol != symb_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)

    return winnings, winning_lines


def get_slot_spin(rows, cols, symbs):
    all_symbs = []
    for symb, symb_count in symbs.items():
        for _ in range(symb_count):
            all_symbs.append(symb)

    columns = []
    for _ in range(cols):
        column = []
        current_symb = all_symbs[:]
        for _ in range(rows):
            value = random.choice(all_symbs)
            current_symb.remove(value)
            column.append(value)

        columns.append(column)

    return columns


def print_slot(cols):
    for row in range(len(cols[0])):
        for i, col in enumerate(cols):
            if i != len(cols) - 1:
                print(col[row], "| ", end='')
            else:
                print(col[row])


def deposit():
    while True:
        amount = input("what would you like to deposit?\n $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("***Amount must be greater than 0***")
        else:
            print("***Deposit should be a Number***")

    return amount


def get_num_of_lines():
    while True:
        lines = input(
            "Enter the number of lines to bet on (1-" + str(MAX_LINES) + ")? \n")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("***Amount must be in valid region***")
        else:
            print("***Lines should be a Number***")

    return lines


def get_bet():
    while True:
        amount = input("What would you like to bet on each line?\n $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"***Amount must be between ${MIN_BET} & ${MAX_BET}***")
        else:
            print("***Amount should be a number***")

    return amount


def spin(balance):
    lines = get_num_of_lines()
    bet = get_bet()

    while True:
        total_bet = bet * lines
        if total_bet > balance:
            print(
                f"***Your Total bet(${total_bet}) exceeds your balance amount(${balance})***")
            print("Either change your bet amount or update your deposit")
            choice = input("Choose between bet(1) and deposit(2)? (1/2): ")
            if choice == "2":
                balance = deposit()
            elif choice == "1":
                bet = get_bet()
            else:
                print("***choose between 'bet' and 'deposit' or 1 and 2***")
        else:
            break
    print(
        f"You are betting ${bet} on {lines} lines. Total bet is: ${bet*lines} \n Remaining Balance is: ${balance - total_bet}")

    slots = get_slot_spin(ROWS, COLS, symb_count)
    print_slot(slots)
    winnings, winning_lines = check_win(slots, lines, bet, symb_value)

    print(f"You won ${winnings} on  line {winning_lines}")

    n_wins = 0
    if winnings > 0:
        n_wins = +1
    else:
        None
    return winnings - total_bet, n_wins


def main():
    balance = deposit()
    while True:
        print(f"Your current balance is ${balance}")
        answer = input("Press enter to play (or q to quit). ")
        if answer == "q":
            break
        else:
            balance = balance + spin(balance)
    print(f"You left with ${balance} and you won number of times")


main()
