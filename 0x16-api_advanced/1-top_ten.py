#!/usr/bin/python3
"""
Advanced Api using reddit API
"""


import requests


def top_ten(subreddit):
    """
    Fetches top 10 posts of a subreddit
    """

    if not subreddit:
        print(None)
        return None

    url = "https://api.reddit.com/r/{}/hot/".format(subreddit)
    headers = {"User-Agent": "Google Chrome Version 122.0.6261.95"}

    response = requests.get(url, headers=headers, allow_redirects=False)
    data = response.json()

    if response.status_code != 200:
        print(None)
        return None

    data = data["data"].get("children")

    if not data:
        return
        print(None)

    for i, _data in enumerate(data):
        if i > 9:
            break
        print(_data["data"]["title"])
