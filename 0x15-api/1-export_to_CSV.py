#!/usr/bin/python3
"""
For a given employee ID, return information about his/her TODO progress
"""
if __name__ == '__main__':
    import csv
    import requests
    from sys import argv

    r = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                     .format(argv[1]))
    uname = r.json().get('username')
    r = requests.get('https://jsonplaceholder.typicode.com/todos?userId={}'
                     .format(argv[1]))
    with open('{}.csv'.format(argv[1]), mode='w') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=',', quotechar='"',
                                quoting=csv.QUOTE_ALL)
        for _ in r.json():
            csv_writer.writerow([argv[1], uname, _.get('completed'),
                                 _.get('title')])
