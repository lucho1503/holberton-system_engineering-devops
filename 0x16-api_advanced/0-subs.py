#!/usr/bin/python3
# return a number of subscribers of a subreddit gven


import requests


def number_of_subscribers(subreddit):
    """ return the number of subreddits """

    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    header = {'User-Agent': 'Chrome'}
    r = requests.get(url, headers=header)
    if r.status_code == 200:
        return r.json().get('data').get('subscribers')
    else:
        return (0)
