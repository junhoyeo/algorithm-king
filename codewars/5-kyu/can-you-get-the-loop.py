def loop_size(node):
    visit = {}
    while 1:
      if node not in visit:
        visit[node] = 0
      elif node in visit:
        if visit[node] > 1:
          return sum(int(bool(i)) for i in visit.values())
        else:
          visit[node] += 1
      node = node.next
