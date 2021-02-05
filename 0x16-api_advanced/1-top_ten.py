#!/usr/bin/python3
"""queries the Reddit API and prints the titles 
of the first 10 hot posts"""

import requests


def top_ten(subreddit):
    """ Reddit API"""
    x = 0
    respons = requests.get("https://www.reddit.com/r/{}/hot.json"
                           .format(subreddit), headers={'User-agent': 'hello'})

    if not respons:
        print("None")
    else:
        while x < 10:
            print(respons.json().get('data').get('children')[x].get('data')
                  .get('title'))
        x += 1
