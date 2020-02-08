#!/usr/bin/python3
"""
this script query the API redddit and retrieves a list of the titles of the
all articles top to a subreddit given
"""


import requests


def recurse(subreddit, hot_list=[], after=""):
    """ retrieves all articles top """
    url = 'https://www.reddit.com/r/{}/hot.json?after={}'.format(subreddit,
                                                                 after)
    header = {'User-Agent': 'Chrome'}
    r = requests.get(url, headers=header, allow_redirects=False)
    if r.status_code == 200:
        for dat in range(r.json().get('data').get('dist')):
            hot_list.append('y')
            a = r.json().get('data').get('after')
        if (a):
            return recurse(subreddit, hot_list, a)
        else:
            return hot_list
    else:
        return None
