#!/usr/bin/python3
"""
Advanced API data fetching.
"""


import requests


def number_of_subscribers(subreddit):
    """ Fetches Subreddit API. """

    headers = {"User-Agent": "Google Chrome Version 122.0.6261.95"}
    url = "https://api.reddit.com/r/{}/about.json".format(subreddit)

    response = requests.get(url, headers=headers, allow_redirects=False)

    data = response.json()

    if response.status_code != 200:
        return 0

    subs = data["data"].get("subscribers")

    if not subs:
        return 0
    return subs
