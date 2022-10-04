q = []
print(q)

q.append(100)
print(q)

q.clear()
print(q)

q.copy()
print(q)

a = [2,4,6]
q.count(4)
print(q)

b = [3,6,9]
c = ['a','b','c']
b.extend(c)
print(b)

d = [4,8,12]
e = d.index(12)
print(e)

f = ['d','e','f']
f.insert(3, 'g')
print(f)

q.append(5)
q.pop()
print(q)

g = [5,10,15]
g.remove(4)
print(g)

h = [6,12,18]
h.reverse()
print(h)

h.sort()
print(h)
