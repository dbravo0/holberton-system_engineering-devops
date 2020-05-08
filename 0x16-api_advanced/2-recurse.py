#!/usr/bin/python3
"""queries the Reddit API and returns a list"""
import requests


def recurse(subreddit, hot_list=[], after=""):
    req = requests.get("https://www.reddit.com/r/{}/hot.json"
                       .format(subreddit),
                       header={'user-agent': 'head'},
                       params={'after': after},
                       allow_redirects=False)

    if req.status_code != 200:
        return None
    else:
        req_json = req.json().get('data').get('children')
        after = req_json['data'].get('after')
        for posts in req_json:
            hot_list.append(posts['data'].get('title'))
        if after is None:
            return hot_list
        else:
            return recurse(subreddit, hot_list, after)
