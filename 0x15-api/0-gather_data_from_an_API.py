#!/usr/bin/python3
"""
using this REST API,
for a given employee ID,
returns information about his/her TODO list progress
"""
import requests
import sys

if __name__ == "__main__":
    in_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/users/{}".format(in_id)
    user = requests.get(url).json()
    todos = requests.get(url + "/todos").json()
    num_of_tasks = len(todos)
    count = 0
    completed_tasks = []

    for i in range(num_of_tasks):
        if todos[i]['completed'] is True:
            count += 1
            completed_tasks.append(todos[i]['title'])
    print("Employee {} is done with tasks({}/{}):"
          .format(user['name'], count, num_of_tasks))
    for task in completed_tasks:
        print("     " + task)
