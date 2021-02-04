#!/usr/bin/python3
"""function that queries the Reddit API and
    returns the number of subscribers"""

import requests


def number_of_subscribers(subreddit):
    """ Reddit API"""
    respons = requests.get("https://www.reddit.com/r/{}/about.json"
                           .format(subreddit), headers={'User-agent': 'hello'})

    if not respons:
        return 0
    return(respons.json().get('data').get('subscribers'))
