"""
This program simulates a slot machine game.
The user deposits money and bets on a certain number of lines.
The slot machine then spins, and if the symbols on any line match, the user wins according to the value of the symbols.
The game continues until the user decides to quit.
"""

import random

# Constants for the game
MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

# Symbol counts and values
symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}

def check_winnings(columns, lines, bet, values):
    """
    Check for winnings based on the slot machine's columns, the number of lines bet on,
    the bet amount, and the symbol values.
    Returns the total winnings and the winning lines.
    """
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)

    return winnings, winning_lines

def get_slot_machine_spin(rows, cols, symbols):
    """
    Generate a spin for the slot machine.
    Returns the columns of the slot machine with randomly selected symbols.
    """
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        # Make a copy of all_symbols
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)

    return columns

def print_slot_machine(columns):
    """
    Print the slot machine's columns in a formatted way.
    """
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")
        print()

def deposit():
    """
    Prompt the user to deposit an amount to start playing.
    Returns the deposited amount.
    """
    while True:
        amount = input("What would you like to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a number.")
    return amount

def get_number_of_lines():
    """
    Prompt the user to enter the number of lines to bet on.
    Returns the number of lines.
    """
    while True:
        lines = input(f"Enter number of lines to bet on (1 - {MAX_LINES}): ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines.")
        else:
            print("Please enter a number.")
    return lines

def get_bet():
    """
    Prompt the user to enter the bet amount per line.
    Returns the bet amount.
    """
    while True:
        amount = input(f"What would you like to bet on each line? $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between {MIN_BET} and {MAX_BET}.")
        else:
            print("Please enter a number.")
    return amount

def spin(balance):
    """
    Conduct a spin of the slot machine.
    Returns the net gain or loss after the spin.
    """
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(f"You do not have enough to bet that amount. Your current balance is: ${balance}")
        else:
            break
    print(f"You're betting ${bet} on {lines} lines. Total bet is: ${total_bet}")

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"You won ${winnings}.")
    print("You won on lines:", *winning_lines)

    return winnings - total_bet

def main():
    """
    Main function to run the slot machine game.
    """
    balance = deposit()
    while True:
        print(f"Current balance is ${balance}")
        answer = input("Press Enter to play (q to quit).")
        if answer == "q":
            break
        balance += spin(balance)

    print(f"You're left with ${balance}")

# Run the main function to start the game
main()
