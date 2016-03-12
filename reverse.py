# !/usr/bin/env python
# coding=utf-8

# Given an input string, reverse the string word by word.

def reverse_words(s):
    return " ".join(s.strip().split(" ")[::-1])

