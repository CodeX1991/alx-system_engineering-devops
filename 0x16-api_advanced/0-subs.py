#!/usr/bin/python3
"""
Queries the Reddit API abd return the number of subscribers
(not active users, total subscribers) for a given subreddit.

If not a valid subriddit, return 0
"""

import requests


def number_of_subscribers(subreddit):
    """Return the total number of subscribers
    for a given subreddit
    """
    # Set the Default URL strings
    home_page_url = "https://www.reddit.com"
    api_uri = "{}/r/{}/about.json".format(home_page_url, subreddit)

    # Set an User-Agent
    user_agent = {'User-Agent': 'Python/requests'}

    # Get the Response of the Reddit API
    res = requests.get(api_uri, headers=user_agent, allow_redirects=False)

    # Checks if the subreddit is invalid
    if res.status_code in [302, 404]:
        return 0

    # Return total subscribers of the subreddit
    return res.json().get('data').get('subscribers')
