#!/usr/bin/python3
import requests


def number_of_subscribers(subreddit):
    # Reddit API endpoint subreddit information
    url = f'https://sww.reddit.com/r/{subreddit}/about.json'

    # set a custom User-Agent to avoid Too Many Requests errors
    headers = {'User-Agent': 'YourAppName/1.0'}

    try:
        # Make a GET request to the Reddit API
        response = requests.get(url, headers=headers)
        # Check if the request was succeeesful (status code 200)
        if response.status_code == 200:
            # Parse the JSON response
            data = response.json()

            # Extract and return the number of subscribers
            return data['data']['subscribers']
        # Check if the subreddit is invalid (status code 404)
        elif response.status_code == 404:
            print(f"Subreddit '{subreddit}' not found.")
            return 0
        else:
            # Handle other status codes if needed
            print(f"Error:{response.status_code}")
            return 0
    except Exception as e:
        print(f"An error occurred: {e}")
        return 0
