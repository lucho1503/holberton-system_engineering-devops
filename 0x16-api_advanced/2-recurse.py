#!/usr/bin/python3
""" return a list that contains the titles for a subreddit given """


import requests


def recurse(subreddit, hot_list=[], after=""):
    """ returns a list recursivelly """
    url = 'https://www.reddit.com/r/{}/hot.json?after={}'.format(subreddit,
                                                                 after)
    h = {'User-Agent': 'Chrome'}
    r = requests.get(url, headers=h, allow_redirects=False)
    if r.status_code == 200:
        for data in range(r.json().get('data').get('dist')):
            hot_list.append('y')
            af = r.json().get('data').get('after')
        if (af):
            return recurse(subreddit, hot_list, af)
        else:
            return hot_list
    else:
        return None
