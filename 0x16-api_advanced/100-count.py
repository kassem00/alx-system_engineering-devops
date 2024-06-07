#!/usr/bin/python3
"""
Querying the Reddit API to return the number of subscribers a given subreddit
"""

import sys
import requests


def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of subscribers for a given
    subreddit.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        int: The number of subscribers to the subreddit, or 0 if not subreddit.
    """
    headers = {'User-Agent': 'ka_reddit'}
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        return (0)
    return (response.json().get("data").get("subscribers"))
