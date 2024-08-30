#!/usr/bin/env python3
"""redis module"""
import redis
from typing import Union
import uuid


class Cache:
    """Cache class"""
    def __init__(self) -> None:
        """initialize redis client"""
        self.__redis = redis.Redis()
        self.__redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """takes data as arg and store it with key generated
        by uuid and return key"""
        key: str = str(uuid.uuid4())
        self.__redis.set(key, data)
        return key
