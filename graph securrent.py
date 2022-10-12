graph = []
print(graph)

graph.append(10)
print(graph)

def recurrent(graph):
  if graph == 1:
    return 1
  else:
    return graph * recurrent(graph - 1)
print(recurrent(10))
