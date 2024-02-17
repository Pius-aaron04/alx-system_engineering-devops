#!/usr/bin/python3

""" Gather data from a REST API. """

import requests
import sys


def main():
    """ starts the program. """

    users = requests.get('https://jsonplaceholder.typicode.com/users').json()
    user = None

    for user_ in users:
        if eval(sys.argv[1]) == user_['id']:
            user = user_
            break
    if user is None:
        return
    todo = requests.get('https://jsonplaceholder.typicode.com/todos').json()
    completed = 0
    task_titles = []
    total = 0
    for task in todo:
        if task['userId'] == user['id']:
            total += 1
            if task['completed']:
                completed += 1
                task_titles += [task['title']]

    print('Employee {} is done with task({}/{})'.format(user['name'],
          completed, total))

    for title in task_titles:
        print('\t {}'.format(title))


if __name__ == '__main__':
    main()
