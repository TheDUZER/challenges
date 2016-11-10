#Coin Flipper by Ian Guitard
import random
y = input("Press any key to flip the coin.")
x = 0
z = 0
def coinFlip():
    a = random.randint(1, 2)
    if a == 1:
        print("Heads")
        return "Heads"
    else:
        print("Tails")
        
#if statement in loop counts up total number of heads or tails since program intitialization
while True:
    if coinFlip() == "Heads":
        x += 1
    else:
        z += 1
    print("\nHeads total: " + str(int(x)) + "      Tails Total: " + str(int(z)))
    y = input("Press enter to flip the coin.")
        
    
