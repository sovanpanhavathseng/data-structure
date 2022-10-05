graph = [[]]
print(graph)

graph.append(1000000)
print(graph)

graph.clear()
print(graph)

graph.copy()
print(graph)

A = [2,4,6]
graph.count(6)
print(graph)

B = [1,3,5]
C = ['a', 'b', 'c']
B.extend(C)
print(B)

D = [3,6,9]
E = D.index(9)
print(E)

F = ['d', 'e', 'f', 'g']
F.insert(4, 'h')
print(F)

graph.append(100)
graph.pop()
print(graph)

graph = [4, 8, 12]
graph.remove(8)
print(graph)

graph = ['i', 'j', 'k', 'l']
graph.reverse()
print(graph)

graph.sort()
print(graph)
