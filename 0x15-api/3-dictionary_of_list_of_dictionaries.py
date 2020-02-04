#!/usr/bin/python3
""" this script export data in json file """


import json
import requests


if __name__ == "__main__":
    user = requests.get('https://jsonplaceholder.typicode.com/users')
    user = user.json()
    todos = requests.get('https://jsonplaceholder.typicode.com/todos')
    todos = todos.json()

    user_task = {}
    lista = []

    for us in user:
        for task in todos:
            if task.get('userId') == us.get('id'):
                u = us.get('username')
                t_c = task.get('completed')
                t_t = task.get('title')

            row = {"username": u, "task": t_t, "completed": t_c}
            lista.append(row)

        user_task[us.get('id')] = lista
    with open('todo_all_employees.json', mode='w') as f:
        json.dump(user_task, f)
