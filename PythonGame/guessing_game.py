import random

def guessing_game():
    num_guess = 0
    while True:
        num = random.randint(1, 101)
        guess = int(input("Guess the number"))
        num_guess = guess + 1
        guess = print("Guesses" + num_guess)
        if guess > num:
            print("The number is too high")
        if guess < num:
            print("The number is too low")
        if guess == num :
            print("You guess it right")
            break

