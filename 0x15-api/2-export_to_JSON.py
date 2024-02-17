#!/usr/bin/python3

""" Gather data from a REST API. """

import json
import requests
from sys import argv


def main():
    """ starts the program. """

    users = requests.get('https://jsonplaceholder.typicode.com/users').json()
    user = None

    for user_ in users:
        if eval(argv[1]) == user_['id']:
            user = user_
            break
    if user is None:
        return
    todo = requests.get('https://jsonplaceholder.typicode.com/todos').json()
    user_tasks = {str(user['id']): []}
    for task in todo:
        if task['userId'] == user['id']:
            task_info = {
                    "task": task['title'],
                    "completed": task['completed'],
                    "username": user['username']
                    }
            user_tasks[str(user['id'])].append(task_info)
    with open('{}.json'.format(user['id']), 'w',
              encoding='utf-8') as json_file:
        json.dump(user_tasks, json_file)


if __name__ == '__main__':
    main()
