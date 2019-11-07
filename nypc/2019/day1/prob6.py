import math
import random
import itertools

def dist(a, b):
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)

# n, k, c = 13, 15, 5
n, k, c = 2, 5, 5
kinds = []
for i in range(k):
    for j in range(k):
        if (i, j) not in kinds:
            kinds.append((i, j))

combs = itertools.combinations(kinds, n)
print(list(combs))
for idx, com in enumerate(combs):
    print(f'{idx}/{l}')
    dots = com
    flag = 0
    for i in range(n):
        others = dots[:i] + dots[(i + 1):]
        dot_1 = dots[i]
        for dot_2 in others:
            if dist(dot_1, dot_2) >= c:
                flag += 1
        else:
            continue
        break
    if flag == n:
        print(dots)
        exit(0)
