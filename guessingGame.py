import random
rand = random.randint(1, 9)
print("Here you are guess a number (between 1 and 9):")
chances=0
while chances < 5:
    go=int(input("Tell me your guess-- "))
    
    if go==rand:
     print("Congrats! You have won in the first attempt")

    if go!=rand:
     print("Better luck next time")
   

    