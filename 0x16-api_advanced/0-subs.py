#!/usr/bin/python3
"""
This function asks the Reddit API how many subscribers there are for a certain
subreddit (not the total number of users, active users).
In case the function receives an invalid subreddit, it ought to return 0.
"""

import requests


def number_of_subscribers(subreddit):
    """
    Function that makes Reddit API queries: return 0 if the subreddit
    is invalid.
    """
    req = requests.get(
        "https://www.reddit.com/r/{}/about.json".format(subreddit),
        headers={"User-Agent": "Custom"},
    )

    if req.status_code == 200:
        return req.json().get("data").get("subscribers")
    else:
        return 0
