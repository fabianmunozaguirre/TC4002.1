# -*- coding: utf-8 -*-
"""
Exercise 3 - Word count
Description: Create a program that parses a file given as parameter and counts 
             the number of occurrences for a list of words identified in the file.
             The identification is sensitive case. 
             The program will accept the words to test as arguments.
             English or Spanish.

Name: Fabián Munoz Aguirre
Student ID: A00354910
"""

bagOfWords = []
wordFrequency = []

def sortFrequenciesDictionary(freqDictionary):
    tempContainer = [(freqDictionary[key], key) for key in freqDictionary]
    tempContainer.sort()
    tempContainer.reverse()
    return tempContainer

def FindLabFile(userFileName):
    try:
        with open(userFileName, "r") as text_file:
            for ln in text_file:
                for wrd in ln.split():
                    bagOfWords.append(wrd)
            wordFrequency = [bagOfWords.count(wrd) for wrd in bagOfWords]
            pairedDict = dict(list(zip(bagOfWords,wordFrequency)))
            sortedDict = sortFrequenciesDictionary(pairedDict)
            print(sortedDict)
    except IOError:
        print("Opss!, an I/O error ocurred while trying to open your file")
        return False

print('Welcome to word count!')
print("Next, please enter a file name where I will try to find and count your words")
FindLabFile(input("Enter the file name:" ))