#!/usr/bin/python3
"""queries the Reddit API and prints the titles of the first 10 hot posts"""
import requests


def top_ten(subreddit):
    headers = {'user-agent': 'head'}
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    req = requests.get(url,
                       params={'limit': 10},
                       headers=headers,
                       allow_redirects=False)

    if req.status_code != 200:
        print(None)
    else:
        req_json = req.json()
        for posts in req_json['data']['children']:
            print(posts['data'].get('title'))
