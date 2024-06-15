'''
basic cache
'''
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ Basic cache class """
    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """ Put a key/value pair """
        if key is None or item is None:
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            last_item_key = list(self.cache_data.keys())[-1]
            print(f"DISCARD: {last_item_key}")
            del self.cache_data[last_item_key]

        self.cache_data[key] = item

    def get(self, key):
        """ Get a key/value pair """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
