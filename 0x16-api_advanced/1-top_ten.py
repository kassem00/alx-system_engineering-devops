#!/usr/bin/python3
"""
Querying the Reddit API to return the number of subscribers for a given
subreddit
"""
import requests


def top_ten(subreddit):
    """Read Reddit API and return the number of subscribers"""
    headers = {'User-Agent': 'ka'}
    url = 'https://www.reddit.com/r/{}/top.json'.format(subreddit)

    try:
        response = requests.get(url,
                                headers=headers,
                                allow_redirects=False,
                                params={"limit": 10}
                                )
        if response.status_code != 200:
            print("Error: Status code", response.status_code)
            return

        try:
            data = response.json()
        except ValueError:
            print("Error: Invalid JSON response")
            return

        for data_list in data.get("data", {}).get("children", []):
            print(data_list.get("data", {}).get("title"))
    except requests.RequestException as e:
        print("Error: Request exception", str(e))
