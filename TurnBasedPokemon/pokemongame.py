import random
import time
print('*' * 36)
print('''\nThis is a turn based Pokemon style game against the computer.
 You both have 100 health to start. You cannot go above full health. 
 Option 1 deals between 18 and 25 damage, option 2 between 10 and 35. 
 Option 3 heals you by 18 to 25 health points. \n''')
print('*' * 36)
player_health = 100
comp_health = 100
turn = 0
while comp_health and player_health > 0:
    if turn == 0:
        move = int(input('Enter move 1, 2, or 3: '))
        if move not in [1, 2, 3]:
            print('I didnt recognize that number.')
        elif move is 1:
            number = random.randint(18, 25) # set here instead of inline below so that number can be called in print statement 
            comp_health -= number 
            comp_health = max(comp_health, 0)   # makes sure that health never displays below 0
            # affected, dmg_heal, and move_name are only for the sake of the printed message
            affected = 'Computer'
            dmg_heal = 'damaged'
            move_name = 'STRIKE'
        elif move is 2:
            number = random.randint(10, 35)
            comp_health -= number
            comp_health = max(comp_health, 0)
            affected = 'Computer'
            dmg_heal = 'damaged'
            move_name = 'FURY'
        elif move is 3:
            number = random.randint(18, 25)
            player_health += number
            player_health = min(player_health, 100) # makes sure that health doesnt go above 100
            affected = 'Player'
            dmg_heal = 'healed'
            move_name = 'RECOVERY'
        turn = 1 - turn # toggle turn between 0 and 1
    else:
        move = random.randint(1, 3)
        time.sleep(1) # 'loading time'
        if comp_health < 35:     # increase probability of choosing 3 if comp_health is under 35 points
            choices = [1, 2] + [3] * 2
            move = random.choice(choices)
        if move is 1:
            number = random.randint(18, 25)
            player_health -= number
            player_health = max(player_health, 0)
            affected = 'Player'
            dmg_heal = 'damaged'
            move_name = 'STRIKE'
        elif move is 2:
            number = random.randint(10, 35)
            player_health -= number
            player_health = max(player_health, 0)
            affected = 'Player'
            dmg_heal = 'damaged'
            move_name = 'FURY'
        elif move is 3:
            number = random.randint(18, 25)
            comp_health += number
            comp_health = min(comp_health, 100)
            affected = 'Computer'
            dmg_heal = 'healed'
            move_name = 'RECOVERY'
        turn = 1 - turn
    print('*' * 36)
    print('\n!!!{}!!!\n'.format(move_name))
    print('''{affected} has been {dmg_heal} by {number} points. \n 
        Player:{player_health}/Computer:{comp_health}
        '''.format(affected=affected, dmg_heal=dmg_heal, number=number, player_health=player_health, comp_health=comp_health))
    print('*' * 36)
# if either player has reached zero, end the game
if comp_health == 0 or player_health == 0:
    print('GAME OVER! Player:{player_health}/Computer:{comp_health}'.format(
        player_health=player_health, comp_health=comp_health))
