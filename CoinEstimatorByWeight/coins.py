type = (input("Type Q to calculate Quarters, D for dimes, N for nickles, or P for pennies: ")).capitalize()

if type == "Q":
    weight = input("Weight of quarters in grams:  ")
    quarters = round(float(weight) / 5.67)
    amount = (quarters * 25) / 100
    wraps = round(quarters / 40)
    print("You have approx. {quarters} quarters totaling to about {amount:.2f} dollars. You need {wraps} wraps.".format( quarters = quarters, amount = amount, wraps = wraps))

if type =="D":
    weight = input("Weight of dimes in grams:  ")
    dimes = round(float(weight) / 2.268)
    amount = (dimes * 10) / 100
    wraps = round(dimes / 50)
    print("You have approx. {dimes} quarters totaling to about {amount:.2f} dollars. You need {wraps} wraps.".format( dimes = dimes, amount = amount, wraps = wraps))

if type == "N":
    weight = input("Weight of nickles in grams:  ")
    nickles = round(float(weight) / 5)
    amount = (nickles * 5) / 100
    wraps = round(nickles / 40)
    print("You have approx. {nickles} quarters totaling to about {amount:.2f} dollars. You need {wraps} wraps.".format( nickles = nickles, amount = amount, wraps = wraps))

if type =="P":
    weight = input("Weight of pennies in grams:  ")
    pennies = round(float(weight) / 2.50)
    amount = pennies / 100
    wraps = round(pennies / 50)
    print("You have approx. {pennies} quarters totaling to about {amount:.2f} dollars. You need {wraps} wraps.".format( pennies = pennies, amount = amount, wraps = wraps))


