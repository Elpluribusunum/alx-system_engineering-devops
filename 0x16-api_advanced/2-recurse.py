#!/usr/bin/python3
"""
A recursive function that pulls up a list of all the popular article titles
for a specific subreddit from a Reddit API query.
The function should return None if the specified subreddit yields no results.
"""

import requests


def recurse(subreddit, hot_list=[], after=""):
    """
    requests a list of all the popular articles for a specific
    subreddit from the Reddit API.

    - Return None if the subreddit is invalid.
    """
    req = requests.get(
        "https://www.reddit.com/r/{}/hot.json".format(subreddit),
        headers={"User-Agent": "Custom"},
        params={"after": after},
    )

    if req.status_code == 200:
        for get_data in req.json().get("data").get("children"):
            dat = get_data.get("data")
            title = dat.get("title")
            hot_list.append(title)
        after = req.json().get("data").get("after")

        if after is None:
            return hot_list
        else:
            return recurse(subreddit, hot_list, after)
    else:
        return None
