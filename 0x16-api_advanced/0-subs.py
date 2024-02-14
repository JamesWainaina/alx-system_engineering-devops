#!/usr/bin/python3
"""Function that queries the Reddit API and returns
the number of subscribers(not active users, total subscribers)"""
import requests


def number_of_subscribers(subreddit):
    """Retrieving the number of subscribers of a given subreddit"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
            "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
        }
    response = requests.get(url, headers=headers, allow_redirects=False)
    try:
        if response.status_code == 404:
            return 0
        results = response.json().get("data")
        return results.get("subscribers")
    except Exception:
        return 0
        

