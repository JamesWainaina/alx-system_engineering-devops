#!/usr/bin/python3
"""
script to fetch data from url and transport as json
"""
import json
import requests
from sys import argv

if __name__ == "__main__":
    user_dict = {}
    user_list = []
    user_url = "https://jsonplaceholder.typicode.com/users/" + argv[1]
    tasks_url = "https://jsonplaceholder.typicode.com/todos"
    user_id = int(argv[1])
    filename = argv[1] + ".json"

    user_name = (requests.get(user_url)).json().get("username")
    tasks = requests.get(tasks_url)

    with open(filename, "w", encoding='utf-8') as f:
        for task in tasks.json():
            if (task.get("userId") == user_id):
                title = task.get("title")
                status = task.get("completed")
                user_dict = {"task": title, "completed": status,
                             "username": user_name}
                user_list.append(user_dict)
        f.write(json.dumps({argv[1]: user_list}))
        