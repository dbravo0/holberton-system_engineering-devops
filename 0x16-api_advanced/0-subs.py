#!/usr/bin/python3
"""queries the Reddit API and returns the number of subscribers"""
import requests


def number_of_subscribers(subreddit):
    """returns the number of subscribers from Reddit"""
    headers = {'User-agent': 'Mozilla/5.0'}
    req = = requests.get("https://www.reddit.com/r/{}/about.json"
                         .format(subreddit), headers=headers)
    if req.status_code == 200:
        return response.json()['data']['subscribers']
    return 0
