import random
min = 1
max = 6

roll_again = "yes"

while roll_again == "yes":
    print ("Rolling dice ...")
    print ("You rolled:")
    print (random.randint(min, max))

    roll_again = input("Roll the dices again?")