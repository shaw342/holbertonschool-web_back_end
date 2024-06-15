"""
Lifo cache module
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    Lifo Class
    """

    def __init__(self):
        """ initilize"""
        super().__init__()
        self.stack = []

    def put(self, key, item):
        """ method put value with key"""
        if key is None and item is None:
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            last_item_key = list(self.cache_data.keys())[-1]
            print(f"DISCARD: {last_item_key}")
            self.cache_data.pop(last_item_key)

        self.cache_data[key] = item

    def get(self, key):
        """ method get for get value with key"""
        return self.cache_data.get(key,None)
