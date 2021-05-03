#!/usr/bin/python3
"""Script to export data in the JSON format"""
import json
import requests
from sys import argv

if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/'
    USER_ID = argv[1]
    m = requests.get(url + 'users?id=' + USER_ID)
    n = m.json()
    USERNAME = n[0].get('username')

    o = requests.get(url + 'todos?userId=' + USER_ID)
    p = o.json()

    json_dict = {}
    task_list = []
    for tasks in range(len(p)):
        new_dict = {}
        new_dict["task"] = p[tasks].get('title')
        new_dict["completed"] = p[tasks].get('completed')
        new_dict["username"] = USERNAME
        task_list.append(new_dict)
    json_dict[USER_ID] = task_list
    filename = USER_ID + '.json'
    with open(filename, 'w') as outfile:
        json.dump(json_dict, outfile)
