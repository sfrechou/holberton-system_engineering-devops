#!/usr/bin/python3
"""
Function that queries the Reddit API and prints the titles of
the first 10 hot posts listed for a given subreddit
"""
import requests


def top_ten(subreddit):
    """Queries the Reddit API and prints titles of the first 10 hot posts"""
    url = "https://www.reddit.com/r/" + subreddit + "/hot.json" + "?limit=10"
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        posts = response.json()['data']['children']
        for title in posts:
            print(title['data']['title'])
    else:
        print(None)
