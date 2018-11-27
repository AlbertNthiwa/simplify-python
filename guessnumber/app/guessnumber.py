import random

number = random.randint(1,9)
guess = 0
count = 0

while guess != number and guess != "exit":
    guess = input("Guess a number between 1 and 9: \n")
    
    if guess == "exit":
        break
    
    guess = int(guess)
    count += 1
    
    if guess < number:
        print("Too low!")
    elif guess > number:
        print("Too high!")
    else:
        print("Bingo! You got it")
        print("It took you " +str(count)+ " tries!")