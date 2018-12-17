import random
playing = True

    
while playing:
    roll =(input("Type Rock, Paper, Scissors or Q to stop playing:  ")).capitalize()
    comp = random.randint(1,3)
    if comp == 1:
        comp = 'Rock'
    elif comp == 2:
        comp = 'Paper'
    elif comp == 3:
        comp = 'Scissors'
    if roll == "Q":
        exit()
    elif roll not in ('Rock','Paper','Scissors'):
        print("typo?")
    else:
        if roll == comp:
            print("You chose {roll} and the computer chose {comp}.".format(roll = roll, comp = comp))
            print("That's a draw")
        elif roll == 'Rock' and comp == 'Paper':
            print('Paper beats Rock. You lose!')
        elif roll == 'Paper' and comp == 'Scissors':
            print('Scissors cuts paper. You lose!')
        elif roll == 'Scissors' and comp == 'Rock':
            print('Rock smashes scissors. You lose!')
        else:
            print("You chose {roll} and the computer chose {comp}.".format(roll = roll, comp = comp))
            print("You win!")