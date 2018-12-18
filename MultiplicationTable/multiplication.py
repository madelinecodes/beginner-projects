max = range(1, 10)
spaces = len(str(max[-1] * max[-1])) + 1

for i in max:
    line = ('')
    for j in max:
        num = str(i * j)
        padding = (spaces - len(num)) * ' '
        line += num + padding
    print(line)