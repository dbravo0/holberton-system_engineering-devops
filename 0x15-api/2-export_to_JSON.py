#!/usr/bin/python3
"""export data in the JSON format"""
import json
import requests
from sys import argv


if __name__ == "__main__":
    todo = requests.get("https://jsonplaceholder.typicode.com/todos?userId={}"
                        .format(argv[1])).json()
    user = requests.get("https://jsonplaceholder.typicode.com/users/{userID}"
                        .format(userID=argv[1])).json()
    username = user.get('username')
    task_dict = {}
    task_list = []

    for task in todo:
        task_dict = {}
        task_dict["task"] = task.get('title')
        task_dict["completed"] = task.get('completed')
        task_dict["username"] = username
        task_list.append(task_dict)

    task_dict[argv[1]] = task_list

    with open("{}.json".format(argv[1]), 'w') as jsonfile:
        json.dump(task_dict, jsonfile)
