sents = []
while 1:
  tmp = input()
  if tmp == '0':
    break
  sents.append(tmp)

data = [input(), input(), input()]
for s in sents:
  tmp = s
  for idx, field in enumerate(['WHO', 'WHERE', 'WHERE']):
    tmp = tmp.replace(field, data[idx])
  print(tmp)
