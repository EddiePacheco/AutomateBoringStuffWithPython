#! python3
# download_xkcd.py - Downloads every single XKCD comic.

# Loads the XKCD home page.
# Saves the comic image on that page.
# Follows the Previous Comic link.
# Repeats until it reaches the first comic.

# Step 1: Download the pages with the requests module.
# Step 2: Find the URL of the comic image for a page using Beautiful Soup.
# Step 3: Download and save the comic image to the hard drive with iter_content().
# Step 4: Find the URL of the Previous Comic link, and repeat.

import os, requests, bs4

url = 'http://xkcd.com' # starting url
os.makedirs('xkcd', exist_ok=True) # store comics in ./xkcd

while not url.endswith('#'): # first comic's Previous button links to #
    # Download the page.
    print(f'Downloading the page {url}...\n')
    result = requests.get(url)
    result.raise_for_status()

    soup = bs4.BeautifulSoup(result.text, 'html.parser')

    # Find the URL of the comic page.
    comic_elem = soup.select('#comic img')
    if comic_elem == []:
        print('Could not find comic image.')
    else:
        comic_url = 'http:' + comic_elem[0].get('src')
    
    # TODO: Download the comic image.
    print(f'Downloading the image {comic_url}...\n')
    result = requests.get(comic_url)
    result.raise_for_status()

    # TODO: Save the comic image to ./xkcd.
    image_file = open(os.path.join('xkcd', os.path.basename(comic_url)), 'wb')
    for chunk in result.iter_content(100000):
        image_file.write(chunk)
    image_file.close()

    # TODO: Get the Prev button's url.
    prev_link = soup.select('a[rel="prev"]')[0] # get the first <a> element with the rel attribute set to prev
    url = 'http://xkcd.com' + prev_link.get('href')
    
print('Done.')