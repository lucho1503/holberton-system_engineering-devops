#!/usr/bin/python3
""" this script export data to format csv """


import json
import requests
import sys


if __name__ == "__main__":

    req = 'https://jsonplaceholder.typicode.com/users/{}'
    user_id = sys.argv[1]

    user = requests.get(req.format(user_id))
    url_todos = requests.get('https://jsonplaceholder.typicode.com/todos')
    url_todos = url_todos.json()
    user_task = {}
    task_row = []

    for row in url_todos:
        if row.get('userId') == int(user_id):
            us = user.json().get('username')
            t_c = row.get('completed')
            t_t = row.get('title')

            task = {"task": t_t, "completed": t_c, "username": us}
            task_row.append(task)

    user_task[user_id] = task_row
    with open(sys.argv[1]+'.json', mode='w') as f:
        json.dump(user_task, f)
