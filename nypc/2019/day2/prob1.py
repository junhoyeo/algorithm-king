# pypy2
from functools import reduce

# https://stackoverflow.com/questions/6800193/what-is-the-most-efficient-way-of-finding-all-the-factors-of-a-number-in-python
def factors(n):    
    return len(set(reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0))))

a, b = [int(i) for i in raw_input().split(' ')]
count = 0
for n in range(a, b+1):
    count += factors(n)
print(count)
