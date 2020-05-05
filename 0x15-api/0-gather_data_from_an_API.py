#!/usr/bin/python3
"""returns information about his/her TODO list progress using the ID"""
import requests
import sys


if __name__ == "__main__":
    user = requests.get('https://jsonplaceholder.typicode.com/todos?userId=' +
                        sys.argv[1])
    name = requests.get('https://jsonplaceholder.typicode.com/users/' +
                        sys.argv[1])

    json_user = user.json()
    json_name = name.json()

    task_total = 0
    task_completed = 0

    task_done = []
    for task in json_user:
        task_total += 1
        if task["completed"] is True:
            task_completed += 1
            task_done.append(task["title"])

    print("Employee {} is done with tasks({}/{}):"
          .format(json_name["name"], task_completed, task_total))

    for task_tittle in task_done:
        print('\t {}'.format(task_tittle))
