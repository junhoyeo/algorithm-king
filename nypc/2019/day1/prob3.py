hp, t = [int(i) for i in input().split(' ')]
logs = []
for i in range(t):
    logs.append([int(i) for i in input().split(' ')])
for l in logs:
    if l[0] == 3:
        hp += l[1]
        break
    elif l[0] == 2:
        hp += l[1]
    else:
        hp -= l[1]
print(hp)
