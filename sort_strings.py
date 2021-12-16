#!/usr/bin/python        # Will not work with python3

#PROGRAM DESCRIPTION: Sort a list of lowercase strings (by given set of rules)

import sys
# import argparse #for command line arguments

# Check for valid command line arguments
if len(sys.argv) != 2:
    print('Usage: python sort_strings.py filename.txt\n')
    sys.exit()

# Assign argument filename.txt to string - file
file = sys.argv[1]

# Open file, read each line into a list, strip newline characters
with open(file) as f:
    myList = [line.rstrip() for line in f]

# Function to convert a string into a string with no vowels
def allVowelString(str):
    return str.translate(None, 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ')

#for x in range(len(myList)):
    #print (myList[x])

# print(*myList) #Python3 print, space delimeter

# Sort function, sort by all vowel string first, if tie, sort by original string
def mySort(a, b): # Modeled after my sort_strings.pl code
    if allVowelString(a) > allVowelString(b):
        return 1
    elif allVowelString(a) < allVowelString(b):
        return -1
    else:
        if a > b:
            return 1
        elif a < b:
            return -1
        else:
            return 0

myList.sort(mySort) # Call sort function

for x in range(len(myList)): #Print sorted list
    print (myList[x])
