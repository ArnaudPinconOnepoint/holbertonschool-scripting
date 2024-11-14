#!/usr/bin/python3
"""Queries the Reddit API and returns the number of subscribers for a given subreddit"""
import requests
import sys

def number_of_subscribers(subreddit):
    """Returns the number of subscribers for a given subreddit"""
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    headers = {'User-Agent': 'python-exercices/1.0'}

    try:
        r = requests.get(url, headers=headers)
        if r.status_code == 200:
            print(r.status_code)
            data = r.json()
            subscribers = data.get('data', {}).get('subscribers', 0)
            active_users = data.get('data', {}).get('accounts_active', 0)
            return (subscribers, active_users)
    except requests.RequestException as error:
        return error
    
def top_ten(subreddit):
    """ Return top ten hot posts"""
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    headers = {'User-Agent': 'python-exercices/1.0'}
    payload = {'limit': 10}
    try:
        r = requests.get(url, headers=headers, params=payload, allow_redirects=False)
        if r.status_code == 200:
            data = r.json()
            top_ten = data.get('data', {}).get('children', [])
            for post in top_ten:
                print(post.get('data', {}).get('title'))
        else:
            print(None)
        return
    except requests.RequestException as error:
        print(None)
        return error

if __name__ == "__main__":
    # subreddit = sys.argv[1]
    subreddit = 'LittleBigAdventure'
    top_ten(subreddit)








