# !/usr/bin/env python
# coding=utf-8

# Given a string containing just the characters '(', ')', '{', '}',
# '[' and ']', determine if the input string is valid.

def is_valid_parentheses(s):
    match = { ")":"(","]":"[", "}":"{"}
    stack = []
    for char in s:
        if char in match.keys():
            if len(stack) == 0:
                # Temporary stack is null
                return False
            if stack.pop() != match[char]:
                return False
        else:
            stack.append(char)
    return False if len(stack) != 0 else True

# Given n pairs of parentheses, write a function to generate
# all combinations of well-formed parentheses.

def generate_parenthesis(n):
    def parenthesis(s, n, parentheses_set):
        if len(s) == 2 * n:
            parentheses_set.append(s)
            return

        combine_str = combine_left_parenthesis(s, n)
        if combine_str is not None:
            parenthesis(combine_str, n, parentheses_set)

        combine_str = combine_right_parenthesis(s)
        if combine_str is not None:
            parenthesis(combine_str, n, parentheses_set)

    def combine_left_parenthesis(s, n):
        return s+"(" if s.count("(") < n else None

    def combine_right_parenthesis(s):
        s = s + ")"
        return s if s.count(")") <= s.count("(") else None

    parentheses_set = []
    parenthesis("(", n, parentheses_set)
    print parentheses_set

if __name__ == "__main__":
    generate_parenthesis(10)
