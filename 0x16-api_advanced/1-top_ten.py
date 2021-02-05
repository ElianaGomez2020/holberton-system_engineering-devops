#!/usr/bin/python3
"""queries the Reddit API and prints the titles of the first 10 hot posts"""

import requests


def top_ten(subreddit):
    """queries the Reddit API and prints the titles"""
    i = 0
    respons = requests.get("https://www.reddit.com/r/{}/hot.json"
                           .format(subreddit), headers={'User-agent': 'hola'})
    if not respons:
        print("None")
    else:
        while i < 10:
            print(respons.json().get('data').get('children')[i].get('data')
                  .get('title'))
            i += 1
