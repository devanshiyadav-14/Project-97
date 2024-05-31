import random
print("Number Guessing Game")
print("Guess a number between 1 and 9")
chances=0
number=random.randint(1,9)

        
while chances<5:
    guess=int(input("enter your guess:"))
    if guess!=number:
        print("your guess was too low : Guess a number higher than",guess)
    if guess==number:
        print("Congratulations! You won")
        break
    chances+=1
print(chances)
if not chances<5:
        print("You loose","the number is",number)
    
