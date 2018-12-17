import time
import random

going = True

while going:
    question = input("Ask the 8 ball a question or enter Q to quit:  ")
    answers = random.randint(1,8)

    print("thinking...")
    time.sleep(2) 

    if question.lower() == "q":
        exit()
  
    elif answers == 1:
        print ("It is certain")
    
    elif answers == 2:
        print ("Outlook good")
    
    elif answers == 3:
        print ("You may rely on it")
    
    elif answers == 4:
        print ("Ask again later")
    
    elif answers == 5:
        print ("Concentrate and ask again")
    
    elif answers == 6:
        print ("Reply hazy, try again")
    
    elif answers == 7:
        print ("My reply is no")
    
    elif answers == 8:
        print ("My sources say no")