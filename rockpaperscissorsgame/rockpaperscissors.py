import random
playing = True
score = {'human': 0, 'comp': 0}
    
def get_score(score):
    return 'Human: {human} - Computer: {comp}'.format(human=score['human'], comp=score['comp'])

while playing:
    roll = input("Type Rock, Paper, Scissors or Q to stop playing:  ").capitalize()
    rnd = random.randint(0, 2)
    moves = ['Rock', 'Paper', 'Scissors']
    move = moves[rnd]
    if roll == "Q":
        exit()
    elif roll not in moves:
        print("typo?")
    else:
        if roll == move:
            print("You chose {roll} and the computer chose {move}.".format(roll = roll, move = move))
            print("That's a draw")
        elif roll == 'Rock' and move == 'Paper':
            print('Paper beats rock. You lose!')
            score['comp'] += 1
        elif roll == 'Paper' and move == 'Scissors':
            print('Scissors cuts paper. You lose!')
            score['comp'] += 1
        elif roll == 'Scissors' and move == 'Rock':
            print('Rock smashes scissors. You lose!')
            score['comp'] += 1
        else:
            print("You chose {roll} and the computer chose {move}.".format(roll = roll, move = move))
            print("You win!")
            score['human'] += 1

    print(get_score(score))