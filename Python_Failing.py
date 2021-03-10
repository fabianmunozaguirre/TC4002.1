"""
Excersise 4 - Converter
Description: You need to create two functions to substitute str() and int().
             A function called int_to_str() that converts integers into strings
             and a function called str_to_int() that converts strings into integers

Name: Fabián Munoz Aguirre
Student ID: A00354910
"""

def int_to_str(parameter):
    if isinstance(parameter, str) :
        return parameter
    
    resultingString = ''
    while True:
        parameter, residue = divmod(parameter, 10)
        resultingString = chr(ord('0') + residue) + resultingString
        if parameter == 0:
            break
    return resultingString

def str_to_int(parameter):
    if isinstance(parameter, int) :
        return parameter
    
    DIGIT_DICTIONARY= {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5,  '6':6, '7':7, '8':8,  '9':9}
    resultingNumber = 0
    
    for charDigit in parameter:
        resultingNumber = 10 * resultingNumber + DIGIT_DICTIONARY[charDigit]
    return resultingNumber


print('String 1 to int is: ', str_to_int('1'))
print('String 5 to int is: ', str_to_int('5'))
print('String 10 to int is: ', str_to_int('10'))
print('String 15 to int is: ', str_to_int('15'))
print('String 20 to int is: ', str_to_int('20'))
print('String 100 to int is: ', str_to_int('100'))
print('String 999 to int is: ', str_to_int('999'))
print('String 761 to int is: ', str_to_int('761'))
print('String 0001 to int is: ', str_to_int('0001'))
print('String 010 to int is: ', str_to_int('010'))
print('\n')
print('Integer \'10\' to int is: ', int_to_str(1))
print('Integer \'20\' to int is: ', int_to_str(20))
print('Integer \'30\' to int is: ', int_to_str(30))
print('Integer \'9\' to int is: ', int_to_str(9))
print('Integer \'8\' to int is: ', int_to_str(8))
print('Integer \'7\' to int is: ', int_to_str(7))
print('Integer \'1.1\' to int is: ', int_to_str(11))
print('Integer \'2\' to int is: ', int_to_str(2))
