#!/usr/bin/python3
""" this script retrieves a top ten first post of a reddit given """

import requests


def top_ten(subreddit):
    """ first top ten subreddits post """
    url = 'https://www.reddit.com/r/{}/hot.json?limit=10'.format(subreddit)
    header = {'User-Agent': 'Chrome'}
    r = requests.get(url, headers=header, allow_redirects=False)
    if r.status_code == 200:
        for data in r.json().get('data').get('children'):
            print(data.get('data').get('title'))
    else:
        print(None)
