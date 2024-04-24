#!/usr/bin/python3
"""
using this REST API,
for a given employee ID,
returns information about his/her TODO list progress
"""
import csv
import requests
import sys

if __name__ == "__main__":
    in_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/users/{}".format(in_id)
    user = requests.get(url).json()
    todos = requests.get(url + "/todos").json()
    num_of_tasks = len(todos)
    count = 0
    _tasks = []

    for i in range(num_of_tasks):
        _tasks.append(todos[i]['title'])

    with open(f"{in_id}.csv", 'w') as fp:
        sw = csv.writer(fp, delimiter=',',
                        quotechar='"', quoting=csv.QUOTE_ALL)
        for i in range(len(_tasks)):
            sw.writerow([in_id, user['name'],
                         todos[i]['completed'], _tasks[i]])
