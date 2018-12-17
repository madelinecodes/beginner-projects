total = float(input("enter total amount:  "))
quarters = total // .25
total = total % .25
dimes = total // .1
total = total % .1
nickles = total // .5
total = total % .5
pennies = total // .01

print("you need {} quarters".format(int(quarters)))
print("you need {} dimes".format(int(dimes)))
print("you need {} nickles".format(int(nickles)))
print("you need {} pennies".format(int(pennies)))