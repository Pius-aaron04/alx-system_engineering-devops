#!/usr/bin/python3

"""
Advanced API using Reddit API
"""


import requests


def count_words(subreddit, word_list, after=None, words_count={}, count=0):
    """
    Recursively fetches titles of hot posts on a subreddit
    from Reddit API.
    """

    if not word_list:
        return
    
    url = "https://api.reddit.com/r/{}/hot".format(subreddit)
    params = {"after": after, 'count': count}
    headers = {"User-Agent": "Google Chrome Version 122.0.6261.95"}
    response = requests.get(url, params=params, headers=headers,
                            allow_redirects=False)
    #unique words
    # frequency of each word in word list
    frequency = {word.lower(): word_list.count(word) for word in word_list if word.lower() == word.lower()}
    print(frequency)

    if response.status_code == 200:
        after = response.json().get('after')

        # fetches posts data
        data = response.json()["data"]["children"]
        if not words_count:
            words_count = {word: 0 for word in frequency}

        # gets all titles in each slice
        if after:
            return recurse(subreddit, word_list, after, words_count, count=10)
        titles = [child['data']['title'] for child in data]
        for title in titles:
            print(title)
            for word in words_count:
                if word in title.lower():
                    occurence = title.lower().split().count(word)
                    if occurence:
                        words_count[word] += frequency[word] * occurence;
        print(words_count)
        for k, v in words_count.items():
            if v:
                print(k+':', v)
