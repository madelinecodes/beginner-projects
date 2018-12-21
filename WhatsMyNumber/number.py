import math
num = 10
def is_prime(num):
    for i in range(2, num - 1):
        if (num % i) == 0:
            is_prime = False
            break
        else:
            is_prime = True
    return is_prime
def sum_nums(num):
     s = 0
     string = str(num)
     for i in range(0,len(string)):
         s += int(string[i])
         i += 1
     return s
def sum_two(num):
     f = str(num)[0] 
     f1 = str(num)[1]
     total = int(f) + int(f1)
     return total
def second_last(num):
    i = len(str(num))-2
    sec = str(num)[i]
    sec_last = int(sec)
    return sec_last
def last(num):
    l = len(str(num))-1
    laststr = str(num)[l]
    last = int(laststr)
    return last


for num in range(10,1001):
    if is_prime(num) is True:
        if '1' not in str(num) and '7' not in str(num):
            if sum_nums(num) <= 10:
                if sum_two(num) % 2 != 0:
                    if second_last(num) % 2 == 0 and second_last(num) > 1:
                        if len(str(num)) == last(num):
                            print(num)
                    else:
                        continue
                else:
                    continue
            else:
                continue
        else:
            continue              
    else: 
        continue
num += 1

