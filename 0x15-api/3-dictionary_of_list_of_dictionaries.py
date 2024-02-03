#!/usr/bin/python3
"""
returning a dictionary representation of data from apis
"""

import json
import requests


if __name__ == "__main__":
    user_dict = {}
    users_list = []
    all_users = {}
    users_url = "https://jsonplaceholder.typicode.com/users"
    tasks_url = "https://jsonplaceholder.typicode.com/todos"
    filename = "todo_all_employees.json"

    users = requests.get(users_url)
    tasks = requests.get(tasks_url)

    with open(filename, "w", encoding='utf-8') as f:
        for user in users.json():
            user_name = user.get("username")
            user_id = user.get("id")
            for task in tasks.json():
                if (task.get("userId") == user_id):
                    title = task.get("title")
                    status = task.get("completed")
                    user_dict = {"username": user_name, "task": title,
                                 "completed": status}
                    users_list.append(user_dict)
            all_users[str(user_id)] = users_list
            users_list = []
        f.write(json.dumps(all_users))
