n = int(input())
scores = [input() for i in range(n)]
for idx, s in enumerate(scores):
  tmp = s
  for field in ['0', '6', '9']:
    tmp = tmp.replace(field, '9')
  tmp = int(tmp)
  scores[idx] = tmp if tmp <= 100 else 100
print(round(sum(scores) / n))
# FIXME
