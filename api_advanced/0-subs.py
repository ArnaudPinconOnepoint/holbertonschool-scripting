#!/usr/bin/python3
"""Queries the Reddit API and returns the number of subscribers for a given subreddit"""
import requests
import sys

def number_of_subscribers(subreddit):
    """Returns the number of subscribers for a given subreddit"""
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    headers = {'User-Agent': 'python-exercices/1.0'}

    try:
        r = requests.get(url, headers=headers,  allow_redirects=False)
        if r.status_code == 200:
            print(r.status_code)
            data = r.json()
            subscribers = data.get('data', {}).get('subscribers', 0)
            active_users = data.get('data', {}).get('accounts_active', 0)
            return (subscribers, active_users)
        else:
            return None
    except requests.RequestException as error:
        print(error)
        return None

if __name__ == "__main__":
    # subreddit = sys.argv[1]
    subreddit = 'LittleBigAdventure'
    print(number_of_subscribers(subreddit))