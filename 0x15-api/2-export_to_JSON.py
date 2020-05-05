#!/usr/bin/python3
"""export data in the JSON format"""
import json
import requests
import sys


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"

    user = "{}users/{}".format(url, sys.argv[1])
    req = requests.get(user)

    user_json = req.json()
    name = user_json.get('username')

    todo = "{}todos?userId={}".format(url, sys.argv[1])
    req = requests.get(todo)

    task = req.json()
    task_list = []

    for todo in task:
        task_dict = {"task": todo.get('title'),
                     "completed": todo.get('completed'),
                     "username": name}
        task_list.append(task_dict)

    task_json = {str(sys.argv[1]): task_list}
    json_name = "{}.json".format(sys.argv[1])

    with open(json_name, 'w') as json_file:
        json.dump(task_json, json_file)
