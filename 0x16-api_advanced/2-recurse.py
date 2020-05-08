#!/usr/bin/python3
"""queries the Reddit API and returns a list"""
import requests


def recurse(subreddit, hot_list=[], after=""):
    req = requests.get("https://www.reddit.com/r/{}/hot.json"
                       .format(subreddit),
                       header={'user-agent': 'head'},
                       params={'after': after},
                       allow_redirects=False)

if req.status_code == 200:
    req_json = req.json().get('data').get('children')
    subs = req_json['data'].get('after')
    for posts in subs:
        hot_list.append(posts.get('data').get('title'))
    else:
        return(None)
    if after is None:
        return hot_list
    else:
        return recurse(subreddit, hot_list, after)
