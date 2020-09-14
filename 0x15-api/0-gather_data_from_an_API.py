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
    print("Employee {} is done with tasks({}/{})".format(
        name, [_.get('completed') for _ in r.json()].count(True),
        len(r.json())))
    for _ in r.json():
        if _.get('completed'):
            print("".join(["\t ", _.get('title')]))
