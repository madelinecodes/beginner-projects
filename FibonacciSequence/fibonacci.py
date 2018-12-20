count = 0
n0 = 0
n1 = 1
fib = ["0", "1", ]
nth = (input("Which placement would you like access to?  "))

try:
    nth = int(nth)
    if nth >= 0:
        if nth == 0:
            v = 0
        elif nth == 1:
            v = 1
        else:
            while count < nth - 1:
                n = n0 + n1
                n0 = n1
                n1 = n
                f = str(n)
                count += 1
                fib.append(f)

            v = str(f)
    else:
        print("Sorry, thats not valid. The placement must be positive.")
        exit()
except ValueError:
    print("Please only enter numbers!")
    exit()
# the below is just so the print statement looks nice
last = int((str(nth))[len(str(nth)) - 1])
if last == 1:
    nth = str(nth)+"st"
elif last == 2:
    if nth == 12:
        nth = str(nth)+"th"
    else:
        nth = str(nth)+"nd"
elif last == 3:
    nth = str(nth)+"rd"
else:
    nth = str(nth)+"th"
print("The {nth} number has a value of {v}!".format(nth=nth, v=v))
