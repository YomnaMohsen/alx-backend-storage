#!/usr/bin/env python3
"""redis module"""
import redis
from typing import Union, Callable
import uuid
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """decorator that takes a single method
    Callable argument and returns a Callable"""

    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """conserve the original function’s name"""
        self._redis.inc(key)
        return method(self, *args, **kwargs)
    return wrapper


class Cache:
    """Cache class"""
    def __init__(self) -> None:
        """initialize redis client"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """takes data as arg and store it with key generated
        by uuid and return key"""
        key: str = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Callable = None):
        """convert the data back to the desired format"""
        value = self._redis.get(key)
        if fn:
            return fn(value) if value else None
        else:
            return value

    def get_str(self, key: str):
        """automatically parametrize Cache.get with the correct
        conversion function"""
        return self.get(key, lambda d: d.decode("utf-8"))

    def get_int(self, key: int):
        """automatically parametrize Cache.get with the
        correct conversion function"""
        return self.get(key, lambda d: int(d))
