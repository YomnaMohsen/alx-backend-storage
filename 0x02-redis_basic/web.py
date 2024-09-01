#!/usr/bin/env python3
"""redis module"""
import redis
from functools import wraps
import requests


def get_page(url: str) -> str:
    """uses the requests module
    to obtain the HTML content of a particular URL
    and returns it"""
    key = f"count:{url}"
    r = redis.Redis()
    count = r.incr(key)
    # checks if result already cached
    cached = r.get(f"{url}")
    if cached:
        return cached.decode("utf-8")
    resp = requests.get(url)
    r.set(f"{url}", resp.text, 10)
    return resp.text
