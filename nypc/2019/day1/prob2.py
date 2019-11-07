from math import sqrt

def find_y_x_in_snail(n, v):
    # 외부 코드 사용 및 수정
    # '대회 이전에 작성되었고 아무나 접근할 수 있는 곳에 공개되어 자유롭게 사용될 수 있도록 허가된 코드'로 분류
    # 출처: https://stackoverflow.com/questions/40494145/algorithm-find-number-position-in-snail-2d-array#answer-40495492
    r = 0
    span = n
    while v > span:
        v -= span
        r += 1
        span -= r%2
    d, m = divmod(r,4)
    c = n-1-d

    return [d+v-1, c, c-v, d][m] + 1, [d, d+v, c, c-v][m] + 1

n, k = [int(i) for i in input().split(' ')]
print(*find_y_x_in_snail(n, k))
