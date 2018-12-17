print("We will play Madlibs! Enter words that fit the catagory!")
a = (input("name: ").capitalize())
b = input("adjective: ")
c = input("place: ")
d = input("food: ")
e = input("drink: ")
f = (input("name: ").capitalize())
g = input("adverb: ")
h = input("verb: ")

x = 'an' if b[0] in 'aeiou' else 'a'

madlib = f'''{a} is having {x} {b} party in {c}. They are serving {d}s and {e}. 
{f} was so {g} to be invited, that they {h} for days.'''

print(madlib)
