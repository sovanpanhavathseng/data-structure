matrix = []
print(matrix)

matrix.append(10)
print(matrix)

matrix.clear()
print(matrix)

matrix.copy()
print(matrix)

a = [1,3,5]
matrix.count(5)
print(matrix)

b = [2,4,6]
c = ['a','b','c']
b.extend(c)
print(b)

d = [3,6,9]
e = d.index(9)
print(d)

f = ['d','e','f']
f.insert(3, 'g')
print(f)

matrix.append(5)
matrix.pop()
print(matrix)

g = [4,8,12]
g.remove(4)
print(g)

h = [5,10,15]
h.reverse()
print(h)

h.sort()
print(h)
