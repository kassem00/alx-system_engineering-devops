#!/usr/bin/python3
"""
Querying the Reddit API to return the number of subscribers for a given
subreddit
"""
import requests


def top_ten(subreddit):
    """
    Read Reddit API and return the titles of
    the top 10 hot posts for a given subreddit
    """
    headers = {'User-Agent': 'ka'}
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)

    try:
        response = requests.get(url,
                                headers=headers,
                                allow_redirects=False,
                                params={"limit": 10}
                                )

        if response.status_code == 302 or response.status_code == 404:
            print("None")
            return
        if response.status_code != 200:
            print("None")
            return

        data = response.json()
        posts = data.get("data", {}).get("children", [])
        if not posts:
            print("None")
            return

        for post in posts:
            print(post.get("data", {}).get("title", "None"))
    except requests.RequestException:
        print("None")

if __name__ == '__main__':
    import sys
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        top_ten(sys.argv[1])
