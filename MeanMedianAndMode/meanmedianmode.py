import math
from collections import Counter

given = list(map(int,sorted(input("Enter your list of numbers, seperated by a comma:  ").split(","))))
length = len(given)

print(given)
print(length)

def mean(given, length):
    try:
        s = sum(given)
        mean = s / length
        return round(mean,2)
    except ValueError:
        print ("invalid input")

def median(given, length):
    try:
        if length % 2 == 0:
            m = given[length//2]
            m1 = given[length//2 -1]
            median = (m+m1)/2
            return median
        else:
            median = given [length//2]
            return median
    except ValueError:
        print ("invalid input")
def mode(given):   
    try:
        count = Counter(given)
        max_count = max(count.values())
        mode = [word for word,max_word in count.items() if max_word == max_count]
        if mode == given:
            return "none"
        else:
            return mode
    except ValueError:
        print ("invalid input")

mean = mean(given, length)
median = median(given, length)
mode = mode(given)
print("The mean is {mean}, median is {median} and mode is {mode}".format(mean=mean,median=median,mode=mode))