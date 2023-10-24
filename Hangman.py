import random

def hangman():
    words = ['apple', 'banana', 'cherry', 'dates', 'elderberry', 'fig', 'grapefruit', 'honeydew', 'kiwi', 'lemon']
    word = random.choice(words)
    turns = 6
    guessed = ''
    hangman_pic = ['   O  \n', ' /|\ \n', ' / \ \n', ' ___\n']

    print('Welcome to Hangman!')
    print(' '.join(hangman_pic))
    print('\n')

    while turns > 0:
        failed = 0
        for char in word:
            if char in guessed:
                print(char, end=' ')
            else:
                print('_', end=' ')
                failed += 1
        if failed == 0:
            print('\nCongratulations! You win!')
            break

        guess = input('\nGuess a character: ')
        guessed += guess

        if guess not in word or len(guess)>1:
            turns -= 1
            print(f'Wrong! You have {turns} turns left.')
            print(' '.join(hangman_pic[0:6-turns]))

            if turns == 0:
                print(f'\nSorry, you lost! The word was {word}.')

hangman()
