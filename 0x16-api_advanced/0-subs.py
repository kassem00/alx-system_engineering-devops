#!/usr/bin/python3
"""
Querying the Reddit API to return the number of subscribers for a given
subreddit
"""
import requests
import sys


def number_of_subscribers(subreddit):
    """Read Reddit API and return the number of subscribers"""
    headers = {'User-Agent': 'Python: reddit.subscriber.counter: v1.0 \
    (by /u/kaa)'}
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code != 200:
            return 0
        data = response.json()
        return data['data']['subscribers']

    except requests.RequestException:
        return 0


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        print("{:d}".format(number_of_subscribers(sys.argv[1])))
