print("practice02.py")

import random

secretNumber = random.randint(1, 4)
userInputString = input("Enter a random number between 1 to 3: ")
userInputInt =  int(userInputString)

print("Winning lottery number:", secretNumber)
print("Your lottery number:", userInputInt)
if userInputInt == secretNumber:
    print("Congrats you won a lottery !!")
else:
    print("Better luck next time !!")
