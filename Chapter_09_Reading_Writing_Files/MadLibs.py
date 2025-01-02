# Reads in text files and lets the user add their own text anywhere the word ADJECTIVE, NOUN, ADVERB, or VERB appears in the text file.
# Prompt the user to replace these words in the text file.
# The results should be printed to the screen and saved to a new text file.

import re
import os
import sys

print("Current working directory:", os.getcwd())

# Read the file
try:
    with open(r'C:\Users\Eddie\OneDrive\Code\AutomateBoringStuffWithPython\Chapter_09_Reading_Writing_Files\MadLibs.txt', 'r') as MadLibsFile:
        MadLibsContent = MadLibsFile.read()
except FileNotFoundError:
    print('The file MadLibs.txt does not exist in the current working directory.')
    sys.exit()

# Find the words to replace
MadLibsRegex = re.compile(r'(ADJECTIVE|NOUN|ADVERB|VERB)')
MadLibsMatches = MadLibsRegex.findall(MadLibsContent)

# Replace the words
for word in MadLibsMatches:
    if word == 'ADJECTIVE':
        print('Enter an adjective:')
    elif word == 'NOUN':
        print('Enter a noun:')
    elif word == 'ADVERB':
        print('Enter an adverb:')
    elif word == 'VERB':
        print('Enter a verb:')
    replacement = input()
    MadLibsContent = MadLibsRegex.sub(replacement, MadLibsContent, 1)

# Print the results
print(MadLibsContent)

# Save the results
with open(r'C:\Users\Eddie\OneDrive\Code\AutomateBoringStuffWithPython\Chapter_09_Reading_Writing_Files\MadLibsResults.txt', 'w') as MadLibsFile:
    MadLibsFile.write(MadLibsContent)

print('The results have been saved to MadLibsResults.txt')