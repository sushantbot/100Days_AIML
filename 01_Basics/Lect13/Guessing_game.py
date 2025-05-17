import random

jackpot_number=random.randint(1,100) # randomly slects intger between 1 and 100

guess = int(input("Guess Number:"))
count=1

# We will run loop untill the guess and jackpot number gets equal
while guess != jackpot_number:
    if guess > jackpot_number:
        print("Guess lesser Number")
    else:
        print("Guess Higher Number")
    
    # for every attampt increase count
    count+=1;guess = int(input("Wapis Guess kar:"))
    # take input again
    
    
print("-------------Sahi Jawab--------------")
if (count >1) and (count <5):
    print("Excellent, You took ",count,"attempts")
elif(count >5) and (count <10):
    print("Average, You took ",count,"attempts")
else:
    print("Poor, You took ",count,"attempts") 
    