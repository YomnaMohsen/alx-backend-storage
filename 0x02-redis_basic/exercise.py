#!/usr/bin/env python3
"""redis module"""
import redis
from typing import Union, Callable
import uuid
from functools import wraps


def call_history(method: Callable) -> Callable:
    """store the history of inputs and
    outputs for a particular function"""
    key = method.__qualname__
    key_input = key + ":inputs"
    key_output = key + ":outputs"

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        data = method(self, *args, **kwargs)

        self._redis.rpush(key_input, str(args))
        self._redis.rpush(key_output, data)
        return data
    return wrapper


def count_calls(method: Callable) -> Callable:
    """decorator that takes a single method
    Callable argument and returns a Callable"""

    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


def replay(fn: Callable):
    """display the history of calls of a particular function"""
    key = fn.__qualname__
    r = redis.Redis()
    count = int(r.get(key))
    print(f"{key} was called {count} times:")
    list1 = r.lrange("{}:inputs".format(key), 0, -1)
    list2 = r.lrange("{}:outputs".format(key), 0, -1)
    for (item1, item2) in (zip(list1, list2)):
        print("{}(*{}) -> {}".format(key, item1.decode("utf-8"),
                                     item2.decode("utf-8")))


class Cache:
    """Cache class"""
    def __init__(self) -> None:
        """initialize redis client"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
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
