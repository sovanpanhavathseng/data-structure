a = [[]]
print(a)

a.append(100000000)
print(a)

a.clear()
print(a)

a.copy()
print(a)

b = ['a','b','c']
a = b.count('c')
print(a)

c = ['d','e','f']
d = ['g','h','i']
c.extend(d)
print(c)

e = ['j','k','l']
f = e.index('l')
print(f)

g = ['m','n','o']
g.insert(2, 'p')
print(g)

h = ['q','r','s']
h.pop(2)
print(h)

i = ['t','u','v']
i.remove('v')
print(i)

j = ['w','x','y','z']
print(j)
j.reverse()
print(j)

j.sort()
print(j)
