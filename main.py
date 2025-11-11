def make_set(m):
    return [[] for _ in range(m)]

def _hash(s, key):
    return sum(ord(c) for c in key) % len(s)

def add(s, key):
    i = _hash(s, key)
    bucket = s[i]
    if key in bucket:
        return False
    bucket.append(key)
    return True

def contains(s, key):
    i = _hash(s, key)
    return key in s[i]

def remove(s, key):
    i = _hash(s, key)
    bucket = s[i]
    if key in bucket:
        bucket.remove(key)
        return True
    return False

def size(s):
    return sum(len(b) for b in s)
