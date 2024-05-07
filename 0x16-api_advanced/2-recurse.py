#!/usr/bin/python3

"""
Advanced API using Reddit API
"""


import requests


def recurse(subreddit, hot_list=[], after=None, count=0):
    """
    Recursively fetches titles of hot posts on a subreddit
    from Reddit API.
    """

    url = "https://api.reddit.com/r/{}/hot".format(subreddit)
    params = {"after": after, 'count': count}
    headers = {"User-Agent": "Google Chrome Version 122.0.6261.95"}
    response = requests.get(url, params=params, headers=headers,
                            allow_redirects=False)

    if response.status_code == 200:
        after = response.json().get('after')

        # fetches posts data
        data = response.json()["data"]["children"]

        # gets all titles in each slice
        if after:
            return recurse(subreddit, hot_list, after, count=len(hot_list))
        titles = [child['data']['title'] for child in data]
        hot_list += titles
        return hot_list

    return None
