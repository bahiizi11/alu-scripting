#!/usr/bin/python3
"""Recursively collects the titles of all hot posts of a subreddit."""
import requests


def recurse(subreddit, hot_list=None, after=None):
    """Return all hot post titles, or None if the subreddit is invalid."""
    if hot_list is None:
        hot_list = []
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "linux:alu.api_advanced:v1.0 (by /u/alu_student)"}
    params = {"limit": 100, "after": after}
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code != 200:
        return None
    data = response.json().get("data", {})
    for post in data.get("children", []):
        hot_list.append(post.get("data", {}).get("title"))
    after = data.get("after")
    if after is None:
        return hot_list
    return recurse(subreddit, hot_list, after)
