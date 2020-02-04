#!/usr/bin/python3
""" this script retrieves information about the progress of a list """


import requests
import sys

if __name__ == "__main__":

    req = 'https://jsonplaceholder.typicode.com/users/{}'.format(sys.argv[1])
    response = requests.get(req)
    resp_json = response.json()['name']

    url_todos = requests.get('https://jsonplaceholder.typicode.com/todos')
    to_dos = url_todos.json()
    total_task = []
    num_task = 0
    completed_task = 0

    for ta in to_dos:
        if ta.get('userId') == int(sys.argv[1]):
            num_task += 1

            if ta.get('completed'):
                total_task.append(ta['title'])
                completed_task += 1

    print("Employee {} is done with tasks({}/{}):".
          format(resp_json, num_task, completed_task))
    for ta in total_task:
        print("\t {}".format(ta))
