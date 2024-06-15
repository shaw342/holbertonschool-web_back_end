#!/usr/bin/env python3
""" cache module """

from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """ lru cache class """
    def __init__(self):
        super().__init__()
        self.access_order = []

    def put(self, key, item):
        """ put item in cache """
        if key is None or item is None:
            return

        # Check if the cache is full
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            # Find and remove the least recently used item
            lru_key = self.access_order.pop(0)
            del self.cache_data[lru_key]
            print(f"DISCARD: {lru_key}")

        # Add the new item to the cache
        self.cache_data[key] = item
        self.access_order.append(key)

    def get(self, key):
        """Get the item from the cache """
        if key is None or key not in self.cache_data:
            return None

        # Update the access order to indicate recent use
        self.access_order.remove(key)
        self.access_order.append(key)

        return self.cache_data[key]
