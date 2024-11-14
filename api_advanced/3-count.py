#!/usr/bin/python3
"""Queries the Reddit API and returns the titles of all hot articles for a given subreddit"""
import requests
import sys
    
def count_words(subreddit, word_list, word_count=None, after=None):
    """ Return count of key words for all hot posts"""

    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    headers = {'User-Agent': 'python-exercices/1.0'}

    # Initialize word count dictionary
    if word_count is None:
        word_count = {word.lower(): 0 for word in word_list}

    try:
        if after is None:
            params = {'limit': 10}
        else:
            params = {'limit': 10, 'after': after}

        r = requests.get(url, headers=headers, params=params, allow_redirects=False)

        if r.status_code == 200:
            data = r.json()
            hot_topic = data.get('data', {}).get('children', [])
            after = data.get('data', {}).get('after', None)

            # Count occurrences of words in titles
            for post in hot_topic:
                title = post.get('data', {}).get('title', '').lower()
                for word in word_list:
                    word_lower = word.lower()
                    word_count[word_lower] += title.split().count(word_lower)

            if after is not None:
                count_words(subreddit, word_list, word_count, after)  # Recursive call with updated 'after'
            else:
                # Sort words by count (descending), then alphabetically (ascending)
                sorted_words = sorted(word_count.items(), key=lambda x: (-x[1], x[0]))
                for word, count in sorted_words:
                    if count > 0:
                        print(f"{word} {count}")

    except requests.RequestException as error:
        print(None)
        return error    

if __name__ == "__main__":
    subreddit = 'LittleBigAdventure'  # Example subreddit
    word_list = ['zoe', 'Twinsen', 'sendell', 'grobo']  # Example word list
    result = count_words(subreddit, word_list)
