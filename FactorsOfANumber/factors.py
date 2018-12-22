x = int(input("Find all factors. Enter your number here:  "))
def is_prime(i):
    is_prime = False
    for j in range(2, i):
        if (i % j) == 0:
            is_prime = False
        else:
            is_prime = True
    return is_prime

def factor(x):
    facts=[]
    if x > 0:
        for i in range(1, x + 1):
            if (x % i) == 0:
                if is_prime(i) is True or i == 2:
                    i = str(i)
                    facts.append(i + '*')
                else:
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
print('*indicates a prime number')

