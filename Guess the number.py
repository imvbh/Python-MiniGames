import random as rnd

number = rnd.randint(1, 100)
guess = int(input("Guess the number between 1 and 100: "))

guesses = 1

while guess != number:
    if abs(number-guess)<=3:
        print("You are close")
    elif 3<(number-guess)<10:
        print("You are little bit lower")
    elif 3<(guess-number)<10:
        print("You are little bit higher")
    elif guess > number:
        print("Too high. Try again.")
    else:
        print("Too low. Try again.")
    guess = int(input("Guess the number between 1 and 100: "))
    guesses += 1


print("Congratulations! You correctly guessed the number in", guesses, "guesses.")