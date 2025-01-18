#! python3
# map_it.py - Launches a map in the browser using an address from the

# Get a street address from the command line arguments or clipboard.
# Open the web browser to the Google Maps page for the address.

# Step 1: Read the command line arguments from sys.argv.
# Step 2: Read the clipboard content.
# Step 3: Call the webbrowser.open() function to open the web browser.

import webbrowser, sys
#!pip install pyperclip
import pyperclip

# Step 1: Read the command line arguments from sys.argv.
# If there are no cmd line arguments,
# then assume the address is in the clipboard.

if len(sys.argv) > 1:
    address = ' '.join(sys.argv[1:])
else:
    address = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/' + address)

# Execute the program on the command line:
# python3 map_it.py [address]

# Example:
# python3 map_it.py 1600 Amphitheatre Parkway, Mountain View, CA