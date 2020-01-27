def solution(args):
  result = []
  stack = []
  for i, this in enumerate(sorted(args)):
    if stack and this == stack[-1] + 1:
      stack.append(this)
    else:
      if len(stack) > 2:
        result.append('{}-{}'.format(stack[0], stack[-1]))
      else:
        result += stack
      stack = [this]
  if len(stack) > 2:
    result.append('{}-{}'.format(stack[0], stack[-1]))
  else:
    result += stack
  print(stack)
  return ','.join([str(i) for i in result])
