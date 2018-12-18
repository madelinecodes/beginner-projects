import random
cpu_guess = random.randint(1, 100)
guesses = 0
playing = True

while playing:
    person = int(input("Guess a number between 1 and 100:  "))
    if person not in range(1,100):
        ("Please follow the rules")
        guesses += 1
    elif person > cpu_guess:
        print ("Your guess is too HIGH!")
        guesses += 1
    elif person < cpu_guess:
        print ("Your guess is too LOW!")
        guesses += 1
    elif person == cpu_guess:
        print ("You got it! That took you {guesses} guesses!".format(guesses=guesses))
        exit()

        
