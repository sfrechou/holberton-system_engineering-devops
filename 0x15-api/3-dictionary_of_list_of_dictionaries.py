#!/usr/bin/python3
"""Script to export data in the JSON format"""
import json
import requests
from sys import argv

if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/'
    m = requests.get(url + 'users')
    n = m.json()
    json_dict = {}

    for users in range(len(n)):
        USER_ID = n[users].get('id')
        USERNAME = n[users].get('username')
        o = requests.get(url + 'todos?userId=' + str(USER_ID))
        p = o.json()

        task_list = []
        for tasks in range(len(p)):
            new_dict = {}
            new_dict["task"] = p[tasks].get('title')
            new_dict["completed"] = p[tasks].get('completed')
            new_dict["username"] = USERNAME
            task_list.append(new_dict)
        json_dict[USER_ID] = task_list
    filename = 'todo_all_employees.json'
    with open(filename, 'w') as outfile:
        json.dump(json_dict, outfile)
