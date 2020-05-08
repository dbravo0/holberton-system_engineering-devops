#!/usr/bin/python3
"""queries the Reddit API and returns the number of subscribers"""
import requests


def number_of_subscribers(subreddit):
    """returns the number of subscribers from Reddit"""
    req = requests.get("https://www.reddit.com/r/{}/about.json"
                       .format(subreddit), headers={'user-agent': 'head'})
    if req.status_code == 200:
        return req.json()['data']['subscribers']
    return 0
