while True:
    sides = input("Please enter your three side lengths, seperated by a comma, or Q to quit:  ")
    if sides.lower() == "q":
        exit()
    else:
        sides = sorted(sides.split(","),reverse=True)
        if int(sides[1])**2 + int(sides[2])**2 == int(sides[0])**2:
            print("You have a pythagorean triple on your hands.") 
        else:
            print("Nope, that one is not a pythagorean triple. ")