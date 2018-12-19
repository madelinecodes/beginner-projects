import random

words = ['hello','monday','tuesday','friday','ice','algebra','suitcase', 'knives', 'ninjas', 'shampoo', 'happy','sad', 'practice','makes','perfect']
word = random.choice(words).lower()
word_len = len(word)
#temp = "_" * word_len
total_turns = 6
taken_turns = 0
wrong_guess = 0
guesses = []
print_word = ['_'] * len(word)

print("The word chosen contains {word_len} letters. You have 6 wrong guesses.".format(
    word_len=word_len))
print("""
            Welcome to Hangman!
                _________
                |      |
                |
                |
                |
                |
                |
                |
            ---------
            """)


def print_scaffold(wrong_guess,):  # prints the scaffold
    if (wrong_guess == 0):
        print("""
            Still looking good!
            _________
            |      |
            | 
            |
            |
            |
            |
            |
        ---------
        """)
    elif (wrong_guess == 1):
        print("""
            Wrong! Dont worry, it's only one.
            _________
            |      |
            |      O
            |
            |
            |
            |
            |
        ---------
        """)
    elif (wrong_guess == 2):
        print("""
            Eek, now there's a body!
            _________
            |      |
            |      O
            |      |
            |      |
            |
            |
            |
        ---------
        """)
    elif (wrong_guess == 3):
        print("""
            One arm!
            _________
            |      |
            |      O
            |     \|
            |      |
            |
            |
            |
        ---------
        """)
    elif (wrong_guess == 4):
        print("""
            We've got a whole upper body!
            _________
            |      |
            |      O
            |     \|/
            |      |
            |
            |
            |
        ---------
        """)
    elif (wrong_guess == 5):
        print("""
            Dangerously close!
            _________
            |      |
            |      O
            |     \|/
            |      |
            |     /
            |
            |
        ---------
        """)
    elif (wrong_guess == 6):
        print("""
            Bummer!
            _________
            |      |
            |      O
            |     \|/
            |      |
            |     / \\
            |
            |
        ---------
        """)


while taken_turns <= total_turns:
    if taken_turns == total_turns:
        print("All out of guesses! You lose!")
        exit()
    guess = input("Guess a letter or word:  ")
    if guess in guesses:
        print('You\'ve already guessed {guess}!'.format(guess=guess))
        continue
    guesses.append(guess)
    if guess == word:
        print("You've guessed it!")
        exit()
    else:
        correct = False
        for i in range(0, len(word)):
            if word[i] == guess and word[i] != '_':
                print_word[i] = guess
                correct = True
                print_scaffold(wrong_guess)
        if '_' not in print_word:
            print('Well done! You won!')
            print('It was: ' + word)
        if not correct:
            wrong_guess += 1
            print_scaffold(wrong_guess)
        print(' '.join(print_word))
        print("\n Guessed:  " + (','.join(guesses)))
    taken_turns += 1
