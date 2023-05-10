#!/usr/bin/python3
"""Count subscribers"""
import requests


def number_of_subscribers(subreddit):
    """Returns number of subscribers in a reddit"""

    api = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'User-Agent': 'siyo12'}
    response = requests.get(api, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        record = response.json().get('data')
        return record.get('subscribers')
    return 0
