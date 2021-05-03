#!/usr/bin/python3
"""Script to export data in the CSV format"""
import csv
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
    status = []
    titles = []
    for content in range(len(p)):
        status.append(p[content].get('completed'))
        titles.append(p[content].get('title'))
    filename = USER_ID + '.csv'
    with open(filename, mode='w') as file_:
        task = csv.writer(file_, delimiter=',',
                          quotechar='"', quoting=csv.QUOTE_ALL)
        for q in range(len(status)):
            task.writerow([USER_ID, USERNAME, status[q], titles[q]])
