#!/usr/bin/python3
""" prints the titles of the first 10 hot post of a subreddit given """

import requests


def top_ten(subreddit):
    """ prints the title of the first 10 hot post """
    url = 'https://www.reddit.com/r/{}/hot.json?limit=10'.format(subreddit)
    h = {'User-Agent': 'Chrome'}
    r = requests.get(url, headers=h, allow_redirects=False)
    if r.status_code == 200:
        for data in r.json().get('data').get('children'):
            print(data.get('data').get('title'))
    else:
        print(None)
