import random

print('Initializing Dice Rolling Simulator...')

#Randomly chooses a number between 1 and 6 and then adds it to an empty list
def diceRoller(num_of_dice):
    results = []
    for DiceNum in range(num_of_dice):
        num = random.randint(1,6)
        results.append(num)
    return results

def main():
    num_of_dice = int(input("Enter the number of dice rolled: "))       #Asks the user to input the number of dice they are rolling
    if num_of_dice <= 0:
        print("Please enter a valid number")
    else:
        for x, result in enumerate(diceRoller(num_of_dice), start = 1): #x represents the dice number. It increments with the dice rolls
            print(f"Dice Number {x}: {result}")
main()




    






