UNFINISHED

num = input("Number:  ")
curr_base = int(input("Current base:  "))
new_base = int(input("Desired base:  "))
going = True



int(num, new_base) 


def again():
    again = (input("Would you like to go again? Y/N: "))
    if again.lower() == "y":
        going = True
    elif again.lower() == "n":
        going = False
    else:
       again()