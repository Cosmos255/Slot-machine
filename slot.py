import random


def spin_row():
    symbols = ["🍒", "🍒", "🍒", "🍒", "🍒", "🍉", "🍉", "🍉", "🍉", "🍋", "🍋", "🍋", "🔔", "🔔", "⭐"]

    return [random.choice(symbols) for _ in range(3)]


def print_row(row):
    print("*************")
    print(" | ".join(row))
    print("*************")


def get_reward(row, bet):

    if row[0] == row[1] == row[2]:
        if row[0] == '🍒':
            return bet * 3

        elif row[0] == '🍉':
            return bet * 4

        elif row[0] == '🍋':
            return bet * 5

        elif row[0] == '🔔':
            return bet * 10

        elif row[0] == '⭐':
            return bet * 20

    return 0


def main():
    balance = 100

    print("************************")
    print(f"Welcome to Python Slots")
    print("Symbols: 🍒 🍉 🍋 🔔 ⭐")

    while balance > 0:
        print(f"Current balance RON{balance}")

        bet = input(f"Place your bet amount ")

        if not bet.isdigit():
            print(f"Please enter a valid number ")
            continue

        bet = int(bet)

        if bet > balance:
            print("Insufficient funds")
            continue

        if bet <= 0:
            print(f"bet must be greater than 0")

        balance -= bet

        row = spin_row()
        print("Spinning...", end="\n")
        print_row(row)

        payout = get_reward(row, bet)

        if payout > 0:
            print(f"You won RON{payout} :3")
        else:
            print(f"Sorry you lost :(")

        balance += payout

        play_again = input(f"Do you want to spin again(y/n): ").lower()

        if play_again != 'y':
            break

    print("******************************************")
    print(f"Game over! Your final balance is {balance}")
    print("******************************************")


if __name__ == '__main__':
    main()
