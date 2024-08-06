#!/usr/bin/env python3
"""
Cache Module
"""
from more_itertools import count_cycle
import redis
import uuid
from typing import Union, Optional, Callable
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """
    method count how many times methods of
    the Cache class are called
    """
    @wraps(method)
    def wrapper(*args, **kwargs):
        key = method.__qualname__
        self._redis.incr(key)
        return method(*args, **kwargs)
    return wrapper


class Cache:
    def __init__(self):
        """Initialize the Redis client and flush the database."""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Store the input data in Redis using a random key."""
        key = str(uuid.uuid4())
        self._redis.set(name=key, value=data)
        return key

    def get(self, key: str, fn: Optional[Callable]
            = None
            ) -> Union[str, int, float, bytes]:
        """
        methode get return without argument
        """
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
