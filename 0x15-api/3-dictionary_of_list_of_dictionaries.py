#!/usr/bin/python3
# this script export data in format json


import json
import requests


if __name__ == "__main__":

    usr = requests.get('https://jsonplaceholder.typicode.com/users')
    usr_json = usr.json()
    todos = requests.get('https://jsonplaceholder.typicode.com/todos')
    todos_json = todos.json()
    usr_task = {}
    task_list = []

    for u in usr_json:
        for task in todos_json:
            if task.get('userId') == u.get('id'):
                user = u.get('username')
                task_com = task.get('completed')
                task_title = task.get('title')

            row = {"task": task_title, "username": user, "completed": task_com}
            task_list.append(row)

        usr_task[u.get('id')] = task_list
    with open('todo_all_employees.json', mode='w') as f:
        json.dump(usr_task, f)
