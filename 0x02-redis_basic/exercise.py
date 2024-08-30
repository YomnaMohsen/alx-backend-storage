#!/usr/bin/env python3
"""redis module"""
import redis
from typing import Union
import uuid


class Cache:
    """Cache class"""
    def __init__(self) -> None:
        """initialize redis client"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """takes data as arg and store it with key generated
        by uuid and return key"""
        key: str = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
