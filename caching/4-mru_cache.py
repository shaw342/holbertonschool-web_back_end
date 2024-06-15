#!/usr/bin/env python3
""" cache module """

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """ mru cache class """
    def __init__(self):
        super().__init__()
        self.accessed_items = {}
        self.access_counter = 0

    def put(self, key, item):
        """ put a key/value pair into the cache """
        if key is None or item is None:
            return

        if len(self.cache_data) >= self.MAX_ITEMS:
            mru_key = max(self.accessed_items, key=self.accessed_items.get)
            del self.cache_data[mru_key]
            print(f"DISCARD: {mru_key}")

        self.accessed_items[key] = self.access_counter
        self.cache_data[key] = item
        self.access_counter += 1

    def get(self, key):
        """ get a key/value pair """
        if key is None or key not in self.cache_data:
            return None

        self.accessed_items[key] = self.access_counter
        self.access_counter += 1
        return self.cache_data[key]
