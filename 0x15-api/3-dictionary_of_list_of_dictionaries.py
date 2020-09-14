#!/usr/bin/python3
"""For all employees, export information about his/her TODO progress"""
import json
import requests
from sys import argv


users = requests.get('https://jsonplaceholder.typicode.com/users')
output = {}
for user in users.json():
    data = requests.get(
        'https://jsonplaceholder.typicode.com/todos?userId={}'
        .format(user.get('id')))
    tasks = [{"task": _.get('title'), "completed": _.get('completed'),
              "username": user.get('username')} for _ in data.json()]
    output[user.get('id')] = tasks

with open('todo_all_employees.json', 'w') as outfile:
    json.dump(output, outfile)
