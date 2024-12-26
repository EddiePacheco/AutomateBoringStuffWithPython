import re

# Compile a regular expression pattern into a regular expression object
pattern = re.compile(r'\d+')

# Use the pattern to search for digits in a string
match = pattern.search('The price is 100 dollars')

if match:
    print(f"Match found: {match.group()}")
else:
    print("No match found")

BatRegex = re.compile(r'Bat(wo)+man')
mo1 = BatRegex.search('The Adventures of Batwoman')
mo1.group()

mo2 = BatRegex.search('The Adventures of Batwowowowoman')
mo2.group()