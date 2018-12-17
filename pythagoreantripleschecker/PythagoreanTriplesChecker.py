while True:
    sides = input("Please enter your three side lengths, seperated by a comma, or Q to quit:  ")
    if sides.lower() == "q":
        exit()
    else:
        sides = sorted(sides.split(","),reverse=True)

        def sqr(side):
            return int(side)**2
            
        if sqr(sides[1]) + sqr(sides[2]) == sqr(sides[0]) :
            print("You have a pythagorean triple on your hands.") 
        else:
            print("Nope, that one is not a pythagorean triple. ")