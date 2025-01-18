#! python3
# search_pypi.py - Opens several search results.

# Get the search keywords from the command line arguments.
# Retrieve the search results page.
# Open a browser tab for each result.

# Step 1: Read the cmd line arguments from sys.argv.
# Step 2: Fetch the search result page with the requests module.
# Step 3: Find the links to each search result.
# Step 4: Call the webbrowser.open() function to open the web browser.

import sys, requests, webbrowser, bs4

print('Searching...')    # Display text while downloading the search result page.

# Step 1: Read the cmd line arguments from sys.argv.
# sys.argv[0] is the program filename, sys.argv[1] is the first argument.
# The search keywords are stored in sys.argv[1].
res = requests.get('https://pypi.org/search/?q=' + ' '.join(sys.argv[1:]))
res.raise_for_status() # Check for errors.

# Step 2: Fetch the search result page with the requests module.
# Create a BeautifulSoup object from the HTML text.
soup = bs4.BeautifulSoup(res.text, 'html.parser')
link_elems = soup.select('.package-snippet')
num_open = min(5, len(link_elems))  # Open the first 5 results, or less if there are fewer than 5.
for i in range(num_open):
    url_to_open = 'https://pypi.org' + link_elems[i].get('href')
    print('Opening', url_to_open)
    webbrowser.open(url_to_open)