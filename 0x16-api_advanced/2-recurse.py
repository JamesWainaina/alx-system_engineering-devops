#!/usr/bin/python3
"""
Recursive fucntion that returns all hot articles for a given subredit
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    if hot_list is None:
        hot_list = []
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0'}

    params = {'limit': 100}
    if after:
        params['after'] = after
    response = requests.get(
        url, headers=headers, params=params, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()['data']
        hot_list += [post['data']['title'] for post in data['children']]
        """
        Rercursively call the function
        """
        if data['after']:
            recurse(subreddit, hot_list, after=data['after'])
        return hot_list
    elif response.status_code == 404:
        return None
    else:
        raise Exception("Request failed with status code {}".format(
            response.status_code
        ))
