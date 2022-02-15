#!/usr/bin/python3
""" Query subs on Reddit """
import json
import requests


def number_of_subscribers(subreddit):
    more = {"User-Agent": "Rodrigo Zarate Query subs"}
    request = requests.get("https://www.reddit.com/r/{}/about.json"
                           .format(subreddit), headers=more)
    if request.status_code == 200:
        return request.json().get("data").get("subscribers")
    else:
        return 0
