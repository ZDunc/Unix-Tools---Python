#!/usr/bin/python3

#PROGRAM DESCRIPTION: Recursively change all file extensions in a directory of
#command line argument old_extension to argument new_extension

import sys
import os
import re

# Check for valid command line arguments
if len(sys.argv) != 4:
    print('Usage: python change_extension.py directory_name old_extension new_extension\n')
    sys.exit()

currentPath = os.getcwd() # Get current path from system
#print(currentPath)
childPath = os.getcwd() + '/' + sys.argv[1] # Append given child directory
#print(childPath)

#Check if directory exists
if (not os.path.isdir(childPath)):
  print ('Directory cannot be located. Exiting program.\n')

#Store values from command line arguments
old_extension = sys.argv[2]
old_length = len(old_extension)
new_extension = sys.argv[3]

#A function that recursively changes the extension name given input
def change_extension(dir): # Modeled after my Perl code
    for file in os.listdir(dir): # iterate through directory
        newDir = dir + '/' + str(file) # append path to filename
        #print (file)
        if os.path.isdir(newDir): #check if a dir
            #print (file)
            change_extension(newDir) # recursive function call
            continue
        if file.endswith(old_extension): # if matching old extension name
            newfile = re.sub(r'.{}$'.format(old_extension), r'.{}'.format(new_extension), file)
            #print (newfile)
            oldName = dir + '/' + file
            newName = dir + '/' + newfile
            os.rename(oldName, newName) # replace

change_extension(childPath) # Call the function
