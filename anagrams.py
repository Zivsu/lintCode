# !/usr/bin/env python
# coding=utf-8

from collections import Counter

# Write a method anagram(s,t) to decide if two strings are anagrams or not.
# Given s="abcd", t="dcab", return true.

def anagram1(s, t):
    # O(nlogn)
    return (sorted(s) == sorted(t))

def anagram2(s, t):
    # O(n)
    return (Counter(s) == Counter(t))

if __name__ == '__main__':
    s = "suwen"
    t = "wensu"
    assert anagram1(s, t)
    assert anagram2(s, t)
