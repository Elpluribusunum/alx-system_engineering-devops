#!/usr/bin/python3
"""
This function prints the titles of the top 10 popular posts for a given
subreddit after requesting information from the Reddit API.
"""

import requests


def top_ten(subreddit):
    """
    Function that makes Reddit API queries: print None
    if the subreddit isn't valid.
    """
    req = requests.get(
        "https://www.reddit.com/r/{}/hot.json".format(subreddit),
        headers={"User-Agent": "Custom"},
        params={"limit": 10},
    )

    if req.status_code == 200:
        for get_data in req.json().get("data").get("children"):
            dat = get_data.get("data")
            title = dat.get("title")
            print(title)
    else:
        print(None)
