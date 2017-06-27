# http://www.lintcode.com/en/problem/first-position-unique-character/
# Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

# Example
# Given s = "lintcode", return 0.
# Given s = "lovelintcode", return 2.

from collections import OrderedDict

def first_uniq_char1(s):
    mapping = OrderedDict()
    for c in s:
       mapping[c] = mapping.get(c, 0) + 1
    
    for key, value in mapping.iteritems():
        if value == 1: return s.index(key)
    return -1

    # Total Runtime: 200-400 ms

def first_uniq_char2(s):
    for index, c in enumerate(s):
        if s.count(c) == 1: return index
    return -1
    
    # Total Runtime: > 1100 ms


def first_uniq_char3(s):
    mapping = Counter(s)
    for index, c in enumerate(s):
        if mapping[c] == 1: return index
    return -1
    # Total Runtime: 200 - 400 ms

