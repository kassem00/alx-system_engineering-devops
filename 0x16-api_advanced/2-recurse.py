#!/usr/bin/python3
"""
Recursive function to query Reddit API for hot article titles.
"""

import requests


def recurse(subreddit, hot_list=None, after=None):
    """
    Recursively fetch all hot article titles from a subreddit.

    Args:
        subreddit (str): The subreddit to query.
        hot_list (list): List to store titles (default None, initialized as []).
        after (str): Pagination cursor (default None).

    Returns:
        list: Titles of all hot articles, or None if subreddit is invalid.
    """
    # Initialize hot_list on first call
    if hot_list is None:
        hot_list = []

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "my-reddit-bot"}
    params = {"limit": 100}
    if after:
        params["after"] = after

    response = requests.get(url, headers=headers,
                            params=params, allow_redirects=False)

    if response.status_code != 200:
        return None

    try:
        data = response.json()
        posts = data["data"]["children"]

        for post in posts:
            hot_list.append(post["data"]["title"])

        next_after = data["data"]["after"]

        if next_after is None:
            return hot_list

        return recurse(subreddit, hot_list, next_after)

    except (KeyError, ValueError):
        return None


if __name__ == "__main__":
    print(recurse("programming"))
