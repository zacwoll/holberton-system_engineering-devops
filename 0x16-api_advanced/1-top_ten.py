#!/usr/bin/python3
"""
Query the Reddit API and print the title of the first 10 hot posts
"""
import requests


def top_ten(subreddit):
    r = requests.get('https://www.reddit.com/r/{}/hot.json?limit=10'
                     .format(subreddit), headers={'User-Agent': 'custom'},
                     allow_redirects=False)
    if r.status_code == 200:
        for post in r.json().get('data').get('children'):
            print(post.get('data').get('title'))
    else:
        print("None")
