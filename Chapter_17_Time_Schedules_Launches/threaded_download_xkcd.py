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

import os, requests, bs4, threading

os.makedirs('xkcd', exist_ok=True) # store comics in ./xkcd

def download_xkcd(start_comic_num, end_comic_num):
    for url_number in range(start_comic_num, end_comic_num):
        # Download the page.
        print('Downloading page http://xkcd.com/%s...' % url_number)
        response = requests.get('http://xkcd.com/%s' % url_number)
        response.raise_for_status()

        soup = bs4.BeautifulSoup(response.text, 'html.parser')

        # Find the URL of the comic image.
        comic_elem = soup.select('#comic img')
        if comic_elem == []:
            print('Could not find comic image.')
        else:
            comic_url = 'http:' + comic_elem[0].get('src')
            # Download the image.
            print('Downloading image %s...' % comic_url)
            response = requests.get(comic_url)
            response.raise_for_status()

            # Save the image to ./xkcd.
            image_file = open(os.path.join('xkcd', os.path.basename(comic_url)), 'wb')
            for chunk in response.iter_content(100000):
                image_file.write(chunk)
            image_file.close()

# Create and start the Thread objects.
downloaded_threads = [] # a list of all the Thread objects
for i in range(0, 140, 10):
    start = i
    end = i + 9
    if start == 0:
        start = 1 # There is no comic 0, so set it to 1.
    download_thread = threading.Thread(target=download_xkcd, args=(start, end))
    downloaded_threads.append(download_thread)
    download_thread.start()

# Wait for all threads to end.
for download_thread in downloaded_threads:
    download_thread.join()
print('Done.')