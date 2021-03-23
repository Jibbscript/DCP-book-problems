"""
Implement a DS which carries out these following ops without resizing the underlying array:
add(value): add a value to the set of values
check(value): check whether a value is in the set

the check method may return occasional false positives but no false negatives.

BloomFilter is a DS which suffices without resizing array by employing multiple hash algos on each input to yield multiple outputs to the hashtable. 
The collision of some overlapping outputs from distinct inputs allows for some false-positives to leak thru but true-positives are always accounted for.
"""

import hashlib

class BloomFilter:
    def __init__(self, n=1000, k=3):
        self.array = [False] * n
        self.hash_algortihms = [
            hashlib.md5,
            hashlib.sha1,
            hashlib.sha256,
            hashlib.sha384,
            hashlib.sha512
        ]
        self.hashes = [self._get_hash(f) for f in self.hash_algortihms[:k]]
    
    def _get_hash(self, f):
        def hash_function(value):
            h = f(str(value).encode('utf-8')).hexdigest()
            return int(h, 16) % len(self.array)
        
        return hash_function

    def add(self, value):
        for h in self.hashes:
            v = h(value)
            self.array[v] = True

    def check(self, value):
        for h in self.hashes:
            v = h(value)
            if not self.array[v]:
                return False
        return True

                    