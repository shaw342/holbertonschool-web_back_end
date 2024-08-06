#!/usr/bin/env python3
"""
Cache Module
"""
import redis
import uuid
from typing import Union, Optional, Callable


class Cache:
    def __init__(self):
        """Initialize the Redis client and flush the database."""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Store the input data in Redis using a random key."""
        key = str(uuid.uuid4())
        self._redis.set(name=key, value=data)
        return key

    def get(self, key: str, fn: Optional[Callable]
            ) -> Union[str, int, float, bytes]:
        value = self._redis.get(key)
        if value is not None and fn:
            return fn(value)
        return value

    def get_int(self, key: str) -> int:
        """ methode get_int return in integer"""
        return self._redis.get(key, fn=lambda d: int(d.decode("utf-8")))

    def get_str(self, key: str) -> str:
        """methode get_str return str"""
        return self._redis.get(key, fn=lambda d: d.docode("utf-8"))
