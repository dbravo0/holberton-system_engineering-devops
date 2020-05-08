#!/usr/bin/python3
"""queries the Reddit API and returns a list"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {'user-agent': 'head'},
    req = requests.get(url,
                       params={'after': after},
                       headers=headers,
                       allow_redirects=False)

    if req.status_code != 200:
        return None
    else:
        req_json = req.json()
        after = req_json['data'].get('after')
        for posts in req_json['data']['children']:
            hot_list.append(posts['data'].get('title'))
        if after is None:
            return hot_list
        else:
            return recurse(subreddit, hot_list, after)
