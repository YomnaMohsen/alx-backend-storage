#!/usr/bin/env python3
"""redis module"""
import redis
from functools import wraps
import requests
from typing import Callable


def track_pages(method: Callable) -> Callable:
    """track how many times a particular URL
    was accessed in the key "count:{url}"""

    @wraps(method)
    def wrapper(url: str) -> str:
        key = f"count:{url}"
        r = redis.Redis()
        r.incr(key)
        # checks if result already cached
        cached = r.get(f"{url}")
        if cached:
            return cached.decode("utf-8")
        response = method(url)
        r.set(f"{url}", response, 10)
        return response
    return wrapper


@track_pages
def get_page(url: str) -> str:
    """ obtain the HTML content of
    a particular URL and returns it"""
    resp = requests.get(url)
    return resp.text
