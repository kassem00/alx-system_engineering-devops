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

    # Set up API request
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "my-reddit-bot"}
    params = {"limit": 100}  # Max posts per request
    if after:
        params["after"] = after

    # Make request, disable redirects
    response = requests.get(url, headers=headers,
                            params=params, allow_redirects=False)

    # Check for invalid subreddit (404 or redirect)
    if response.status_code != 200:
        return None

    # Parse JSON
    try:
        data = response.json()
        posts = data["data"]["children"]

        # Extract titles and append to hot_list
        for post in posts:
            hot_list.append(post["data"]["title"])

        # Get next page cursor
        next_after = data["data"]["after"]

        # Base case: no more pages
        if next_after is None:
            return hot_list

        # Recursive case: fetch next page
        return recurse(subreddit, hot_list, next_after)

    except (KeyError, ValueError):
        # Invalid JSON or unexpected structure
        return None


if __name__ == "__main__":
    print(recurse("programming"))
