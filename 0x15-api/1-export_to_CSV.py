#!/usr/bin/python3
"""
For a given employee ID, return information about his/her TODO progress
"""
if __name__ == '__main__':
    import requests
    from sys import argv

    r = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                     .format(argv[1]))
    uname = r.json().get('username')
    r = requests.get('https://jsonplaceholder.typicode.com/todos?userId={}'
                     .format(argv[1]))
    for _ in r.json():
        print(",".join([argv[1], uname, str(_.get('completed')),
                        _.get('title')]))
