#!/usr/bin/python3
""" this script export data to format csv """


import json
import requests
import sys


if __name__ == "__main__":

    req = 'https://jsonplaceholder.typicode.com/users/{}'.format(sys.argv[1])
    response = requests.get(req)
    url_todos = requests.get('https://jsonplaceholder.typicode.com/todos')
    to_dos = url_todos.json()
    user_task = {}
    task_row = []

    for row in to_dos:
        if row.get('userId') == int(sys.argv[1]):
            us = response.json().get('username')
            t_c = row.get('completed')
            t_t = row.get('title')

            task = {"task": t_t, "completed": t_c, "username": us}
            task_row.append(task)

    user_task[sys.argv[1]] = task_row
    with open(sys.argv[1]+'.json', "w") as f:
        json.dump(user_task, f)
