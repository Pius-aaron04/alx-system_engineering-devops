#!/usr/bin/python3

""" Gather data from a REST API. """

import requests
import json


def main():
    """ starts the program. """

    users = requests.get('https://jsonplaceholder.typicode.com/users').json()
    all_tasks = {}
    for user_ in users:
        all_tasks[str(user_['id'])] = []

    todo = requests.get('https://jsonplaceholder.typicode.com/todos').json()
    for task in todo:
        user_id = task['userId']
        task_info = {
                "username": users[user_id - 1]['username'],
                "task": task['title'],
                "completed": task['completed']
                    }
        all_tasks[str(task['userId'])].append(task_info)
    with open('todo_all_employees.json', 'w', encoding='utf-8') as json_file:
        json.dump(all_tasks, json_file)


if __name__ == '__main__':
    main()
