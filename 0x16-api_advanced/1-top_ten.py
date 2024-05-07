#!/usr/bin/python3
"""
Advanced Api using reddit API.
THis tasks fetches hot topics on a subreddit
"""


import requests


def top_ten(subreddit):
    """
    Fetches top 10 posts of a subreddit
    """

    url = "https://api.reddit.com/r/{}/hot/".format(subreddit)
    headers = {"User-Agent": "Google Chrome Version 122.0.6261.95"}

    response = requests.get(url, headers=headers, allow_redirects=False)
    data = response.json()

    if response.status_code != 200:
        print(None)
        return None

    data = data["data"].get("children")

    for i in range(10):
        if i < len(data):
            print(data[i]['data']['title'])
