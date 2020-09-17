#!/usr/bin/python3
"""
Queries the Reddit API and return the number of subscribers for a given
subreddit.
"""
import requests


def number_of_subscribers(subreddit):
    r = requests.get('https://www.reddit.com/r/{}/about.json'
                     .format(subreddit), headers={'User-Agent': 'custom'},
                     allow_redirects=False)
    if r.status_code == 200:
        return r.json().get('data').get('subscribers')
    else:
        return 0
