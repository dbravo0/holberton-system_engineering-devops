#!/usr/bin/python3
"""export data in the JSON format"""
import json
import requests


if __name__ == '__main__':
    user_url = "https://jsonplaceholder.typicode.com/users"
    todo_url = "https://jsonplaceholder.typicode.com/todos"

    user_req = requests.get(user_url).json()
    todo_req = requests.get(todo_url).json()

    user_dict = {}
    username_dict = {}

    for user in user_req:
        user_id = user.get("id")
        user_dict[user_id] = []
        username_dict[user_id] = user.get("username")

    for task in todo_req:
        task_dict = {}
        user_id = task.get("userId")
        task_dict["task"] = task.get('title')
        task_dict["completed"] = task.get('completed')
        task_dict["username"] = username_dict.get(user_id)
        user_dict.get(user_id).append(task_dict)

    with open("todo_all_employees.json", 'w') as json_file:
        json.dump(user_dict, json_file)
