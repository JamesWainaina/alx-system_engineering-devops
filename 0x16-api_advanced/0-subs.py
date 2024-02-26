import requests

def number_of_subscribers(subreddit):
    # Reddit API endpoint for subreddit information
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    
    # Set a custom User-Agent to avoid Too Many Requests errors
    headers = {'User-Agent': 'YourAppName/1.0'}

    try:
        # Make a GET request to the Reddit API
        response = requests.get(url, headers=headers)
        
        # Raise an exception for bad responses (status codes other than 200)
        response.raise_for_status()

        # Parse the JSON response
        data = response.json()
        
        # Extract and return the number of subscribers
        return data['data']['subscribers']
    
    except requests.exceptions.HTTPError as http_err:
        # Handle HTTP errors (e.g., 404 Not Found)
        print(f"HTTP error occurred: {http_err}")
        return 0
    
    except requests.exceptions.RequestException as req_err:
        # Handle other request-related errors
        print(f"Request error occurred: {req_err}")
        return 0

# Example usage:
subreddit_name = 'python'
subscribers_count = number_of_subscribers(subreddit_name)
print(f"The number of subscribers in r/{subreddit_name} is: {subscribers_count}")
