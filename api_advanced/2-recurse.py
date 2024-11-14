#!/usr/bin/python3
"""Queries the Reddit API and returns the titles of all hot articles for a given subreddit"""
import requests
import sys
    
def recurse(subreddit, hot_list=[], params=None):
    """ Return all hot posts"""
    # Initialize params if None
    if params is None:
        params = {'limit': 10}

    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    headers = {'User-Agent': 'python-exercices/1.0'}

    try:
        r = requests.get(url, headers=headers, params=params, allow_redirects=False)
        if r.status_code == 200:
            data = r.json()
            newItems = data.get('data', {}).get('children', [])
            for post in newItems:
                hot_list.append(post.get('data', {}).get('title'))
            after = data.get('data', {}).get('after', None)
            if after:
                # Pass after in the next call, continue recursion
                params['after'] = after
                return recurse(subreddit, hot_list, params)  # pass params to the next recursive call
            else:
                return hot_list
        return None
    except requests.RequestException as error:
        print(None)
        return error
    
def recurse_without_params(subreddit, hot_list=[]):
    """ Return all hot posts"""

    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    headers = {'User-Agent': 'python-exercices/1.0'}

    try:
        if hot_list == []:
            params = {'limit': 10}
        else:
            params = {'limit': 10, 'after': hot_list[-1].get('data', {}).get('name')}

        r = requests.get(url, headers=headers, params=params, allow_redirects=False)
        if r.status_code == 200:
            data = r.json()
            newItems = data.get('data', {}).get('children', [])
            hot_list += newItems
            after = data.get('data', {}).get('after', None)
            if after:
                return recurse_without_params(subreddit, hot_list)
            else:
                final_list = [post.get('data', {}).get('title') for post in hot_list]
                return final_list
        return None
    except requests.RequestException as error:
        print(None)
        return error

if __name__ == "__main__":
    subreddit = 'LittleBigAdventure'
    result = recurse_without_params(subreddit)
    print(result)
