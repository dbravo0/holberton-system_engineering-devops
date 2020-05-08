#!/usr/bin/python3
"""queries the Reddit API and prints the titles of the first 10 hot posts"""
import requests


def top_ten(subreddit):
    """prints the first 10 hot posts listed for a given subreddit"""
    req = requests.get("https://api.reddit.com"
                       "/r/{}/hot".format(subreddit),
                       params={'limit': '10'},
                       allow_redirects=False,
                       headers={'User-Agent': 'head'})

    if req.status_code == 200:
        subs = req_.json()["data"]["children"]
        for posts in subs:
            print(posts["data"]["tittle"])
    else:
        print(None)
