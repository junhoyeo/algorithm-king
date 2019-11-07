n, m, t = [int(i) for i in input().split(' ')]
buildings = (n + 1) * [0]
current = t
count = 0
for i in range(m):
    b, r = [int(j) for j in input().split(' ')]
    if r:
        if buildings[current] > 0:
            buildings[current] -= 1
            buildings[b] += 1
        else:
            count += 1
            buildings[b] += 1
    current = b
print(count)
