#!/usr/bin/python3
"""Function that queries the Reddit API and returns
the number of subscribers(not active users, total subscribers)"""
import requests


def number_of_subscribers(subreddit):
    """Retrieving the number of subscribers of a given subreddit"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
                "User-Agent": "MyCustomUserAgent/1.0"}
    response = requests.get(url, headers=headers, allow_redirects=False)

    data = response.json()

    try:
        return data['data']['subscribers']
    except Exception:
        return 0
