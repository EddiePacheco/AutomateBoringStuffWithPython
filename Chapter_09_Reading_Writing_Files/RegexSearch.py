# Open all .txt files in a folder and search for any line that matches a user-supplied regular expression.
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