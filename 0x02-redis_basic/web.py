#!/usr/bin/env python3
"""redis module"""
import redis
from functools import wraps
import requests


def get_page(url: str) -> str:
    """uses the requests module 
    to obtain the HTML content of a particular URL 
    and returns it"""
    key = "count:{url}"
    r = redis.Redis()
    count = r.incr(key)
    # checks if result already cached
    cached = r.get("{url}")
    if cached:
        return cached.decode("utf-8")
    resp = requests.get(url)
    r.set("{url}", resp, 10)
    return resp.text


get_page('http://slowwly.robertomurray.co.uk')