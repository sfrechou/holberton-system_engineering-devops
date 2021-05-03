#!/usr/bin/python3
"""Script that returns information about given employee's todo list progress"""
import requests
from sys import argv

if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/users?id='
    u_id = argv[1]
    m = requests.get(url + u_id)
    n = m.json()
    EMPLOYEE_NAME = n[0].get('name')

    o = requests.get('https://jsonplaceholder.typicode.com/todos?userId=' + u_id)
    p = o.json()
    TOTAL_NUMBER_OF_TASKS = len(p)
    NUMBER_OF_DONE_TASKS = 0
    for content in range(len(p)):
        for key, value in p[content].items():
            if key == 'completed':
                if value is True:
                    NUMBER_OF_DONE_TASKS += 1

    print("Employee {} is done with tasks({}/{}):".format(EMPLOYEE_NAME,
                                                        NUMBER_OF_DONE_TASKS,
                                                        TOTAL_NUMBER_OF_TASKS))
    for content in range(len(p)):
        for key, value in p[content].items():
            if key == 'completed' and value is True:
                print("\t{}".format(p[content].get('title')))
