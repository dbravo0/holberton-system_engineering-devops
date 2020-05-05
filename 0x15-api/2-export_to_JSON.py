#!/usr/bin/python3
"""export data in the JSON format"""
import json
import requests
import sys


if __name__ == "__main__":
    todo = requests.get("https://jsonplaceholder.typicode.com/todos?userId=" +
                        sys.argv[1])
    user = requests.get("https://jsonplaceholder.typicode.com/users/" +
                        sys.argv[1])

    json_todo = todo.json()
    json_user = user.json()

    task_dict = {}
    task_list = []

    for task in json_todo:
        task_dict = {}
        task_dict["task"] = task.get('title')
        task_dict["completed"] = task.get('completed')
        task_dict["username"] = json_user['username']
        task_list.append(task_dict)

    task_dict[sys.argv[1]] = task_list

    with open(sys.argv[1] + '.json', 'w') as json_file:
        json.dump(task_dict, json_file)
