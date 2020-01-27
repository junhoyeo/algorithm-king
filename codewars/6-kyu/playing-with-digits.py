def dig_pow(n, p):
    s = sum([num ** (p + i) for i, num in enumerate([int(i) for i in str(n)])])
    return s / n if s % n == 0 else -1
