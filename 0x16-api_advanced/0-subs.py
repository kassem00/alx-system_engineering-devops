#!/usr/bin/python3
"""Querying the Reddit API to return the number of subscribers for a given subreddit"""

import requests

def number_of_subscribers(subreddit):
    """Read Reddit API and return the number of subscribers"""
    headers = {'User-Agent': 'Python:reddit.subscriber.counter:v1.0 (by /u/yourusername)'}
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            return data['data']['subscribers']
        else:
            return 0
    except requests.RequestException:
        return 0

if __name__ == '__main__':
    import sys
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        print("{:d}".format(number_of_subscribers(sys.argv[1])))
