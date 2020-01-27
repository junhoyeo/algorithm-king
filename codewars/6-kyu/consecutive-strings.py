def longest_consec(strarr, k):
  n = len(strarr)
  if n < 1 or k < 1 or k > n:
    return ''
  return sorted([''.join(strarr[i:i+k]) for i in range(n)], key=len, reverse=True)[0]
