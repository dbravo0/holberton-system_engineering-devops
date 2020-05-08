#!/usr/bin/python3
import requests


def number_of_subscribers(subreddit):
    headers = {'User-agent': 'Mozilla/5.0'}
    req = requests.get("https://www.reddit.com/r/{}/about.json"
                         .format(subreddit), headers=headers)
    if req.status_code == 200:
        return req.json()['data']['subscribers']
    return 0
