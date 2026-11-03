#!/usr/bin/python3
"""Recursively counts keywords in the hot post titles of a subreddit."""
import requests


def count_words(subreddit, word_list, after=None, counts=None):
    """Print the sorted keyword counts found in hot post titles."""
    if counts is None:
        counts = {}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "linux:alu.api_advanced:v1.0 (by /u/bahiizi11)"}
    params = {"limit": 100, "after": after}
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code != 200:
        return
    data = response.json().get("data", {})
    for post in data.get("children", []):
        title = post.get("data", {}).get("title", "")
        for token in title.lower().split():
            counts[token] = counts.get(token, 0) + 1
    after = data.get("after")
    if after is not None:
        return count_words(subreddit, word_list, after, counts)
    totals = {}
    for word in word_list:
        word = word.lower()
        if counts.get(word):
            totals[word] = totals.get(word, 0) + counts[word]
    for word, total in sorted(totals.items(), key=lambda x: (-x[1], x[0])):
        print("{}: {}".format(word, total))
