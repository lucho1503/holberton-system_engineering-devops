#!/usr/bin/python3
""" this script return a information about a employee by id passed as argument
"""

import sys
import requests

if __name__ == "__main__":
    """ get the name by user id passed as argument """
    url = 'https://jsonplaceholder.typicode.com/users/{}'.format(sys.argv[1])
    res = requests.get(url)
    res_json = res.json()['name']

    url_todos = requests.get('https://jsonplaceholder.typicode.com/todos')
    todos_json = url_todos.json()
    total_task = []
    num_task = 0
    task_com = 0

    for task in todos_json:
        if task.get('userId') == int(sys.argv[1]):
            num_task += 1

            if task.get('completed'):
                total_task.append(task['title'])
                task_com += 1

    print("Employee {} is done with task({}/{}):".
          format(res_json, task_com, num_task))

    for task in total_task:
        print("\t{}".format(task))
