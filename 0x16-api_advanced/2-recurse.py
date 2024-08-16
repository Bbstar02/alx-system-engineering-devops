#!/usr/bin/python3
import requests

def recurse(subreddit, hot_list=[], after=None):
    """Recursively queries the Reddit API and returns a list of all hot article titles for a given subreddit."""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "custom_user_agent"}
    params = {"after": after, "limit": 100}
    response = requests.get(url, headers=headers, params=params, allow_redirects=False)
    if response.status_code == 200:
        data = response.json().get("data", {})
        children = data.get("children", [])
        for child in children:
            hot_list.append(child.get("data", {}).get("title"))
        after = data.get("after")
        if after is not None:
            return recurse(subreddit, hot_list, after)
        return hot_list
    return None
