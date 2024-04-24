#!/usr/bin/python3
"""
This script fetches tasks for all employees
from a REST API and outputs the data
in a JSON file named todo_all_employees.json.
The format includes user
ID keys with arrays of task information objects.
"""
import json
import requests


def fetch_all_users():
    """Fetches all users from the API."""
    response = requests.get("https://jsonplaceholder.typicode.com/users")
    return response.json()


def fetch_user_todos(user_id):
    """Fetches todos for a specific user ID."""
    response = requests.get(
        f"https://jsonplaceholder.typicode.com/users/{user_id}/todos")
    return response.json()


def main():
    users = fetch_all_users()
    all_tasks = {}

    for user in users:
        user_id = user['id']
        todos = fetch_user_todos(user_id)
        all_tasks[user_id] = [{
            "username": user['username'],
            "task": todo['title'],
            "completed": todo['completed']
        } for todo in todos]

    with open('todo_all_employees.json', 'w') as f:
        json.dump(all_tasks, f, indent=4)

    print("Data for all employees has been written to todo_all_employees.json")


if __name__ == "__main__":
    main()
