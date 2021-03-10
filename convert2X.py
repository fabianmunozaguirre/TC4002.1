# -*- coding: utf-8 -*-
"""
Excersise 2 - Converter
Description: Create a command line program that take as input parameter a number
             and then it displays in the console the corresponding number (positive integers Plus Zero) 
             in Binary and Hexadecimal. It also manages errors using exceptions for not using numbers.

Name: Fabián Munoz Aguirre
Student ID: A00354910
"""
import sys

convertNumber = 0
binaryEquivalent = ''
hexEquivalent = ''
hexDigits = '0123456789ABCDEF'

def NumberToBinary(numberToConvert):
    message = ''
    if numberToConvert >= 1:
        message += NumberToBinary(numberToConvert // 2)
    return message + str(numberToConvert % 2)

def NumberToHex(numberToConvert):
    if (numberToConvert // 16) == 0:
        return hexDigits[numberToConvert % 16]
    return NumberToHex(numberToConvert // 16) + hexDigits[numberToConvert % 16]
    

"User input and first validations"
inputString = input("Please input a positive integer number:\n")
if(inputString.isnumeric()):
    convertNumber = int(inputString)
    if(convertNumber < 0):
        print("Only positive numbers are allowed, program will exit")
        sys.exit()
else:
    print("Only positive numbers are allowed, program will exit")
    sys.exit()


binaryEquivalent = NumberToBinary(convertNumber)
binaryEquivalent = binaryEquivalent[-len(binaryEquivalent)+1:]

hexEquivalent = NumberToHex(convertNumber)

print("Binary equivalent: " + binaryEquivalent + ", Hexadecimal equivalent: " + hexEquivalent)