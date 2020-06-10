import json
import hashlib
from collections import OrderedDict

def hash_string_256(string):
    return hashlib.sha256(string).hexdigest()

def hash_block(block):
    blocked = block.__dict__.copy()     
    hash = hashlib.sha256(json.dumps(blocked,sort_keys=True).encode())
    return hash.hexdigest()
