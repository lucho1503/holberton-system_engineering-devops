#!/usr/bin/python3
""" this script export data to format csv """


import csv
import requests
import sys


if __name__ == "__main__":

    req = 'https://jsonplaceholder.typicode.com/users/{}'.format(sys.argv[1])
    response = requests.get(req)
    resp_json = response.json().get('username')

    url_todos = requests.get('https://jsonplaceholder.typicode.com/todos')
    with open(sys.argv[1]+'.csv', "w") as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)

        for row in url_todos.json():
            if row.get('userId') == int(sys.argv[1]):
                rows = [sys.argv[1], resp_json, row.get('completed'),
                        row.get('title')]
                writer.writerow(rows)
