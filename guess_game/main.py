# Guessing game
import random


def high_low(x):
    welcome_message = "Welcome to my guessing game,\nin this game you will have to guess the number im thinking! \n\
If you are to high or to low the computer will let you know\n\n"
    thinking = "I'm thinking of a number between 1 and 100 can you guess what it is? "
    print(welcome_message)
    personal_money = 100
    question = input("Want to make a bet on how many tries\nwithout going over? ").lower()

    if (question[0] == "y") or "Y":
        number_guess = int(input("How many guesses? "))
        wager = int(input("How much do you want to bet? €"))
        while wager > personal_money:
            if wager > personal_money:
                wager = int(input("You don't have enough funds, please enter a lower number: "))

        else:
            personal_money - wager

    else:
        wager = 0
    print(thinking)
    thinking = random.randint(1, x)
    guess = 0
    i = 0
    while guess != thinking:
        guess = int(input("Guess a number: "))
        if guess > thinking:
            print("Lower ")
            i += 1
        elif guess < thinking:
            print("Higher")
            i += 1
    i += 1
    if number_guess >= i:
        winnings = wager * 2
        # str(personal_money + wager)
        total = personal_money + wager
        print(f"Well Done you found the number!!!\nIt only took you {i} tries\n")
        print(f"You won you bet €{wager} and won €{winnings} added to your total which is €{total}")

    else:
        print(f"Well Done you found the number!!!\nIt only took you {i} tries\n")
        print(f"Unfortunately your bet was of and you have lost €{wager}")


high_low(100)
