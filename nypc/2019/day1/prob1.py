def check(n, stock, recipe):
    for i in range(n):
        if (stock[i] - recipe[i] < 0):
            return False
    return True

n = int(input())
stock = [int(i) for i in input().split(' ')]
recipe = [int(i) for i in input().split(' ')]

count = 0
while True:
    if check(n, stock, recipe):
        for i in range(n):
            stock[i] -= recipe[i]
        count += 1
    else:
        break
print(count)
