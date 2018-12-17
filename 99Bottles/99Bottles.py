
for x in range(100, 0, -1):
    if x < 100 and x > 1:
        print( "{x} bottles of beer on the wall, {x} bottles of beer. Take one down, pass it around, {y} bottles of beer on the wall.".format(x=x, y=x-1))
    if x == 1:
        print( "{x}  bottle of beer on the wall {x} bottle of beer. Take one down, pass it around, no more bottles of beer on the wall.\n" 
            "No more bottles of beer on the wall, no more bottles of beer." 
            "Go to the store and buy some more, 99 bottles of beer on the wall.".format(x=x))
        