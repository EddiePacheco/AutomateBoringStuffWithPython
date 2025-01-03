# Open all .txt files in a folder and search for any line that matches a user-supplied regular expression.
# The results should be printed to the screen.

import re
import os

# Prompt the user for a regular expression
print('Enter a regular expression:\n')
UserRegex = re.compile(input())

# Open all .txt files in the current working directory
for filename in os.listdir(os.getcwd()):
    if filename.endswith('.txt'):
        with open(filename, 'r') as File:
            FileContent = File.readlines()
            for line in FileContent:
                if UserRegex.search(line):
                    print(line)