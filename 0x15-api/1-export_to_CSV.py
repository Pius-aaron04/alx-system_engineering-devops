#!/usr/bin/python3

""" Gather data from a REST API. """

import csv
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
    with open('{}.csv'.format(user['id']), 'w', encoding='utf-8') as csv_file:
        writer = csv.writer(csv_file, quotechar='"', quoting=csv.QUOTE_ALL)
        for task in todo:
            if task['userId'] == user['id']:
                writer.writerow([user['id'], user['username'],
                                task['completed'], task['title']])


if __name__ == '__main__':
    main()
