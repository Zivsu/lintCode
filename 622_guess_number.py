def guess_number(n):
    r = n
    l = 1
    while l <= r:
        mid = l + (r - l) / 2
        rv = Guess.guess(mid)
        if rv == 0:
            return rv
        elif rv == 1:
            l = mid + 1
        else:
            r = mid -1
    return -1

