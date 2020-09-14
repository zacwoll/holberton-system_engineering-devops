#!/usr/bin/python3
"""
For a given employee ID, return information about his/her TODO progress
"""

if __name__ == '__main__':
    import requests
    from sys import argv

    r = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                     .format(argv[1]))
    name = r.json().get('name')

    r = requests.get('https://jsonplaceholder.typicode.com/todos?userId={}'
                     .format(argv[1]))
    data = r.json()
    completed = total = 0
    for task in data:
        total += 1
        if task.get('completed'):
            total += 1

    print('Employee {} is done with tasks({}/{}):'
          .format(name, completed, total))
    for task in data:
        if task.get('completed'):
            print('\t {}'.format(task.get('title')))
