#!/usr/bin/python3
# this script export data format CSV file


import sys
import requests
import csv


if __name__ == "__main__":
    usr = sys.argv[1]
    url = 'https://jsonplaceholder.typicode.com/users/{}'.format(usr)
    res = requests.get(url)
    res_json = res.json()['username']
    url_todos = requests.get('https://jsonplaceholder.typicode.com/todos')
    with open(usr+'.csv', 'w') as f:
        w = csv.writer(f, quoting=csv.QUOTE_ALL)

        for row in url_todos.json():
            if row.get('userId') == int(usr):
                rows = [usr, res_json, row.get('completed'), row.get('title')]
                w.writerow(rows)
