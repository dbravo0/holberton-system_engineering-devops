#!/usr/bin/python3
"""export data in the CSV format"""
import csv
import requests
from sys import argv


if __name__ == "__main__":
    todo = requests.get("https://jsonplaceholder.typicode.com/todos?userId={}"
                        .format(argv[1])).json()
    user = requests.get("https://jsonplaceholder.typicode.com/users/{userID}"
                        .format(userID=argv[1])).json()

    with open("{userID}.csv".format(userID=argv[1]), 'w') as csv_file:
        writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        for task in todo:
            writer.writerow([int(argv[1]), user.get('username'),
                             task.get('completed'), task.get('title')])
