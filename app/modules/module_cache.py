import fnmatch

cache = {}

def all_cache():
    return cache

def set_cache(key, value):
    cache[key] = value

def get_cache(key):
    return cache[key] if key in cache else None

def query_cache(key):
    return [k for k in cache.keys() if fnmatch.fnmatch(k, key)]
