# -*- coding: utf-8 -*-
"""
Excersise 1 - Find the Number
Description: Create a program invoked in the command line. 
             It generatesa random number between 1 and 30(including 1 and 30).
             Ask the user to guess the number, then tell them whether 
             they guessed too low, too high, or exactly right.

Name: Fabián Munoz Aguirre
Student ID: A00354910
"""

import random
import datetime as dt

"Declare variables"
randomNumber = 0
guessedNumber = 0
countTries = 0
continueFlag = True
interruptFlag = False
resultMessage = ""
dateOfEvent = dt.date.today()
timeOfEvent = dt.datetime.now()

"Initialize random number"
randomNumber = random.randrange(1,30,1)

"Begin loop for user input"
while continueFlag:
    "Iterate number of tries..."
    countTries += 1
    
    "Request input to user"
    inputString = input("Please ipnput an integer number ranging from 1 to 30 (type \'exit' to stop):\n")
    
    "Did the user type exit?"
    if(inputString.lower() == 'exit'):
        countTries-=1
        print("\n Exited by user.\n The randomNumber was: {}".format(randomNumber))
        interruptFlag = True
        break
    
    "Check what input number was and asses range"
    if(inputString.isnumeric()):
        guessedNumber = int(inputString)
        
        if (guessedNumber == randomNumber):
            print("You got it exactly right!")
            break
        elif (guessedNumber > 30):
            print("You are above the range, please try again")
        elif (guessedNumber > randomNumber and guessedNumber < 31):
            print("You got it too high")
        else:
            print("You got it too low")
    else:
        print("That is not a valid entry, please try again or type exit to stop")

"Final count of tries message"
print("\n Number of tries: {} \n".format(countTries))

"Begin saving routine of results message"
resultMessage = "Date and Time of event: " + dateOfEvent.strftime("%m/%d/%Y") + " " + timeOfEvent.strftime("%H:%M:%S") + "\n"

if interruptFlag:
    resultMessage += "User interruped the excecution before finishing" + "\n"
    resultMessage += "Number of tries before interruption: " + str(countTries) + "\n"
else:
    resultMessage += "User guessed correctly the random number \n"
    resultMessage += "Number of tries to find the number: " + str(countTries) + "\n"


resultMessage += "Number to be guessed was: " + str(randomNumber) + "\n"
resultMessage += "-------------------------------------------------------------------\n"

print(resultMessage)

with open("GuessingSteps.txt", "a") as text_file:
    text_file.write(resultMessage)
