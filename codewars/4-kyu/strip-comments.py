def solution(string,markers):
    result = []
    for line in string.split('\n'):
      for marker in markers:
        line = line.split(marker)[0]
      result.append(line.strip())
    return '\n'.join(result)
