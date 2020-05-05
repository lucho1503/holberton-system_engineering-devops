#!/usr/bin/python3
# export data in json file


import json
import requests
import sys


if __name__ == "__main__":

    usr = sys.argv[1]
    url = 'https://jsonplaceholder.typicode.com/users/{}'.format(usr)
    r = requests.get(url)
    r_json = r.json().get('username')
    url_todos = requests.get('https://jsonplaceholder.typicode.com/todos')
    url_todos_json = url_todos.json()
    usr_task = {}
    task_row = []

    for row in url_todos_json:
        if row.get('userId') == int(usr):
            task_com = row.get('completed')
            task_title = row.get('title')
            task = {"task": task_title,
                    "completed": task_com,
                    "username": r_json}
            task_row.append(task)

    usr_task[usr] = task_row
    with open(usr + '.json', 'w') as f:
        json.dump(usr_task, f)
