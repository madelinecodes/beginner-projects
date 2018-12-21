#Used regex. Total error count was 87 including i's at the start of sentances,
#stand-alone i's, and -i-'s

import re
file = open('story.txt',mode='r')
contents = file.read()

#getting i followed by dash, followed by space, proceeded by a ! and space, proceeded by a ? and space.
regex = re.compile(r'i(?=-)|i(?=\s)|(?<=\!\s)i|(?<=\?\s)i')
# sub them for 'I' and count how many subs we did
subbing = regex.subn('I', contents)
#stringify and seperate count
newStory = ''.join(str(subbing[0]))
count = ''.join(str(subbing[1]))
#make the string \n an actual new line
newStory =(newStory.replace("\\n","\n" ))
#print story just to check
print(newStory)
print("Total count was {count}".format(count=count))

#write new txt file
updatedFile = open('newstory.txt', 'w')
updatedFile.write(newStory)
updatedFile.close()