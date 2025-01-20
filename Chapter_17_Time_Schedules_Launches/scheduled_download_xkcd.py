#! python3
# threaded_download_xkcd.py - Downloads new XKCD comics if available.

import os, requests, bs4, threading

os.makedirs('xkcd', exist_ok=True) # store comics in ./xkcd

def get_latest_comic_num():
    response = requests.get('http://xkcd.com')
    response.raise_for_status()
    soup = bs4.BeautifulSoup(response.text, 'html.parser')
    prev_link = soup.select('a[rel="prev"]')[0]
    latest_comic_num = int(prev_link.get('href').strip('/')) + 1
    return latest_comic_num

def download_xkcd(comic_num):
    # Download the page.
    print('Downloading page http://xkcd.com/%s...' % comic_num)
    response = requests.get('http://xkcd.com/%s' % comic_num)
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

def main():
    latest_comic_num = get_latest_comic_num()
    last_downloaded_comic_num = 0

    # Check if the last downloaded comic number is stored
    if os.path.exists('xkcd/last_comic.txt'):
        with open('xkcd/last_comic.txt', 'r') as file:
            last_downloaded_comic_num = int(file.read().strip())

    if latest_comic_num > last_downloaded_comic_num:
        download_xkcd(latest_comic_num)
        with open('xkcd/last_comic.txt', 'w') as file:
            file.write(str(latest_comic_num))
    else:
        print('No new comic to download.')

if __name__ == '__main__':
    main()