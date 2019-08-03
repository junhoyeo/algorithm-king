t = int(input())
for repeat in range(t):
    n = int(input())
    doors = [0] * 100
    for round in range(1, n+1): # 라운드
        for door in range(1, 101): # 문 번호
            if (door % round == 0):
                doors[door - 1] = not doors[door - 1] # 반전
    print(sum(doors[:n])) # 열린 문 수
