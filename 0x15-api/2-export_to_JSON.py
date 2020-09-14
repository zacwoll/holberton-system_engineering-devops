#!/usr/bin/python3
"""
For a given employee ID, export information about his/her TODO progress
"""
if __name__ == '__main__':
    import json
    import requests
    from sys import argv


    r = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                     .format(argv[1]))
    uname = r.json().get('username')
    r = requests.get('https://jsonplaceholder.typicode.com/todos?userId={}'
                     .format(argv[1]))
    output = {}
    tasks = [{"task": _.get('title'), "completed": _.get('completed'), "username":
             uname} for _ in r.json()]
    output = {argv[1]: tasks}

    with open('{}.json'.format(argv[1]), 'w') as outfile:
        json.dump(output, outfile)
