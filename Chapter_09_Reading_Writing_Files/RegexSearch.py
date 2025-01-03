# Open all .txt files in a folder and search for any line that matches a user-supplied regular expression.
"""
This script searches for lines matching a user-supplied regular expression in all .txt files within the current working directory.
Modules:
    re: Provides support for regular expressions.
    os: Provides a way of using operating system dependent functionality.
    pathlib: Provides an object-oriented interface to the filesystem.
Functions:
    None
Usage:
    Run the script and enter a regular expression when prompted. The script will search through all .txt files in the current working directory and print lines that match the regular expression.
Example:
    Enter a regular expression:
    \d{3}-\d{3}-\d{4}
    This will search for lines containing phone numbers in the format 123-456-7890.
"""
# The results should be printed to the screen.

import re
import os
from pathlib import Path

# Prompt the user for a regular expression
print('Enter a regular expression:\n')
UserRegex = re.compile(input())

# Open all .txt files in the current working directory
CurrDir = Path.cwd()
for filename in CurrDir.glob('*.txt'):
    with open(filename, 'r') as File:
        FileContent = File.readlines()
        for line in FileContent:
            if UserRegex.search(line):
                print(line)
# for filename in os.listdir(os.getcwd()):
#     if filename.endswith('.txt'):
#         with open(filename, 'r') as File:
#             FileContent = File.readlines()
#             for line in FileContent:
#                 if UserRegex.search(line):
#                     print(line)