#!usr/bin/python

class HashTable(object):
    def __init__(self, size):
        self.size = size
        self._buckets = []
        # Why does 'buckets = [[]] * size' not work?
        for i in xrange(size):
            self._buckets.append([])

    def hash(self, key):
        """hashes the key to the sum of the ordinal value of each letter in the key, \
        modulo the size of the table"""
        return sum([ord(c) for c in key]) % self.size

    def set(self, key, val):
        """deposits the key-value pair into the hashval'th bucket"""
        try:
            bucket = self._buckets[self.hash(key)]
        except TypeError:
            raise TypeError("key must be a string")
        
        for key_val in bucket:
            if key_val[0] == key:
                key_val[1] = val
                return

        bucket.append((key, val))

    def get(self, key):
        """returns the value for the specified key"""
        try:
            bucket = self._buckets[self.hash(key)]
        except TypeError:
            raise KeyError(key)

        for item in bucket:
            if item[0] == key:
                return item[1]
        raise KeyError(key)
