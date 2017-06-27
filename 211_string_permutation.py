# Given two strings, write a method to decide if one is a permutation of the other.

def string_permutation(A, B):
    return (sorted(A) == sorted(B))
