x = (int(input("How high would you like the table to go? Enter here:  "))) + 1
max = range(1, x)
spaces = len(str(max[-1] * max[-1])) + 1

for i in max:
    line = ('')
    for j in max:
        num = str(i * j)
        padding = (spaces - len(num)) * ' '
        line += num + padding + "| "
        hor = (len(line)-1) * '-'

    print(line)
    print (hor)