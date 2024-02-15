import requests
import json

# Datadog API and Application keys
api_key = '840726aac542c206e70c9a308d5234b4'
app_key = '6aef409419af360c8fb1ee5e2190701c0e13bde8'

# Datadog API endpoint for getting hosts
api_url = 'https://api.datadoghq.com/api/v1/hosts'

# Headers for authentication
headers = {
    'Content-Type': 'application/json',
    'DD-API-KEY': api_key,
    'DD-APPLICATION-KEY': app_key
}

# Get the list of hosts from Datadog
response = requests.get(api_url, headers=headers)

# Check if the host exists
host_to_check = 'web-01'
hosts = response.json().get('host_list', [])

if any(host['host_name'] == host_to_check for host in hosts):
    print(f'The host "{host_to_check}" exists in Datadog.')
else:
    print(f'The host "{host_to_check}" does not exist in Datadog.')

