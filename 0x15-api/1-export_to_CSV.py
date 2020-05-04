#!/usr/bin/python3
# export data in csv file


import csv
import requests
import sys


if __name__ == "__main__":

    usr = sys.argv[1]
    url = 'https://jsonplaceholder.typicode.com/users/{}'.format(usr)
    r = requests.get(url)
    r_json = r.json().get('username')
    url_todos = requests.get('https://jsonplaceholder.typicode.com/todos')

    with open(usr + '.csv', 'w') as f:
        w = csv.writer(f, quoting=csv.QUOTE_ALL)

        for row in url_todos.json():
            if row.get('userId') == int(usr):
                rows = [usr, r_json, row.get('completed'), row.get('title')]
                w.writerow(rows)
