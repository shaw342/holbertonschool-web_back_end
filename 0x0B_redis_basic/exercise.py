#!/usr/bin/env python3
"""
Cache Module
"""

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
    def wrapper(self, *args, **kwargs):
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """
        method call_history decorator to store the history of
        inputs and outputs for a particular function
        """
        inputs_key = f"{method.__qualname__}:inputs"
        outputs_key = f"{method.__qualname__}:outputs"
        self._redis.rpush(inputs_key, str(args))
        result = method(self, *args, **kwargs)
        self._redis.rpush(outputs_key, str(result))
        return result
    return wrapper


class Cache:
    def __init__(self):
        """Initialize the Redis client and flush the database."""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
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

    def replay(self, method: Callable):
        """ Display the history of calls of a particular function."""

        method_name = method.__qualname__
        inputs_key = f"{method_name}:inputs"
        outputs_key = f"{method_name}:outputs"

        inputs_list = self._redis.lrange(inputs_key, 0, -1)
        outputs_list = self._redis.lrange(outputs_key, 0, -1)

        print(f"{method_name} was called {len(inputs_list)} times:")
        for input_str, output_str in zip(inputs_list, outputs_list):
            dec_input = input_str.decode('utf-8')
            dec_output = output_str.decode('utf-8')
            print(f"{method_name}(*{dec_input}) -> {dec_output}")
