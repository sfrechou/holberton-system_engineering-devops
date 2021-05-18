#!/usr/bin/python3
"""
Function that queries the Reddit API and returns the number of subscribers
"""
import requests


def number_of_subscribers(subreddit):
    """Queries the Reddit API and returns the number of subscribers"""
    url = "https://www.reddit.com/r/" + subreddit + "/about.json"
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.json()['data'].get('subscribers')
