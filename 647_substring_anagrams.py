

def find_anagrams(s, p):
    length = len(p)
    sorted_p = sorted(p)
    result = []
    for index, _ in enumerate(s):
        if (sorted(s[index:length+index]) == sorted_p): result.append(index)
    return result

print find_anagrams("abab", "ab")
