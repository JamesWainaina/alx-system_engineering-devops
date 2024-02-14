#!/usr/bin/python3
"""Functio that queries the Reddit API and returns
the number of subscribers(not active users, total subscribers)"""
import requests


def number_of_subscribers(subreddit):
    """Retrieving the number of subscribers of a given subreddit"""
    url = "https://www.reddit.com/r/" + subreddit + "/about.json"
    header = {"User-Agent": "MyUser"}
    response = requests.get(url, allow_redirects=False, headers=header)
    if response.status_code == 404:
        return (0)
    if response.status_code == 200:
        req = int(response.json().get("data").get("subscribers"))
        return (req)
