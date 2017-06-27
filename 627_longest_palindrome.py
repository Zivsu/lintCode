# Given a string which consists of lowercase or uppercase letters, 
# find the length of the longest palindromes that can be built with those letters.

# This is case sensitive, for example "Aa" is not considered a palindrome here.

from collection import Counter

def longest_palindrome(s):
    m = Counter(s)
    n = odd = 0
    for _, value in m.iteritems():
        n += value
        if value % 2 == 1:
            n -= 1
            odd +=1
    return n + (odd > 0)
