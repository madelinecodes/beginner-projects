x = int(input("Find all factors. Enter your number here:  "))

def factor(x):
    facts=[]
    if x > 0:
        for i in range(1, x + 1):
            if (x % i) == 0:
                facts.append(i)
        return facts
    elif x < 0:
        for i in range (x-1, 0):
            if x % i == 0:
                facts.append(i)
        return facts
    elif x == 0:
        print("All numbers are factors of Zero my friend.")
print (', '.join(map(str, factor(x))))