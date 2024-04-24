#!/usr/bin/python3
"""
using this REST API,
for a given employee ID,
returns information about his/her TODO list progress
"""
import json
import requests
import sys

if __name__ == "__main__":
    in_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/users/{}".format(in_id)
    user = requests.get(url).json()
    todos = requests.get(url + "/todos").json()
    num_of_tasks = len(todos)
    tasks_output = {in_id: []}

    for todo in todos:
        tasks_output[in_id].append({
            "task": todo['title'],
            "completed": todo['completed'],
            "username": user['username']
        })

    file_name = f"{in_id}.json"
    with open(file_name, 'w') as fp:
        json.dump(tasks_output, fp)
