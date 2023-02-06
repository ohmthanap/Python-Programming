"""
    Import random module and math module
    Input upper and lower number for the range of guessing
    Using .randint function to select the number from the range between upper and lower number
    Set guessing_count to limit the number to guess
    Set the limitation of guessing by using math.log function
    Using while loop to continue the execution until get the correct number
    Using if-else statement to check the number of guessing
    Input the guessing number and add +1 for guessing count
    Using if-else statement to judge the number
    Display that the guessing number is correct or not
"""

import random
import math

upper = int(input("Enter the upper number: "))
lower = int(input("Enter the lower number: "))
correct_number = random.randint(lower, upper)   # must import random module
guessing_count = 0
guessLimit = int(math.log(upper - lower + 1, 2))    # must import math module

while True:
    if guessing_count <= guessLimit:
        guess_number = int(input("Enter guessing number: "))
        guessing_count += 1
        if guess_number < correct_number:
            print("Try to guess higher number")
            continue
        elif guess_number > correct_number:
            print("Try to guess lower number")
            continue
        else:
            print("You guessed the correct number")
            break
    else:
        print("Over guessing count limit")
        break

print("The number of guessing count is", guessing_count)
print("The correct number is", correct_number)

