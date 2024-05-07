"""
Advanced API data fetching.
"""


import requests


def number_of_subscribers(subreddit):
    """ Fetches Subreddit API. """

    if not subreddit:
        return 0

    headers = {"User-Agent": "Google Chrome Version 122.0.6261.95"}
    url = "https://api.reddit.com/r/{}/about.json".format(subreddit)

    response = requests.get(url, headers=headers)

    data = response.json()

    subs = data["data"].get("subscribers")

    if not subs:
        return 0
    return subs
