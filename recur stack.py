stack = []
print(stack)

stack.append(10)
print(stack)

stack.clear()
print(stack)

stack.copy()
print(stack)

a = [1,3,5]
stack.count(5)
print(stack)

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

stack.append(5)
stack.pop()
print(stack)

g = [4,8,12]
g.remove(4)
print(g)

h = [5,10,15]
h.reverse()
print(h)

h.sort()
print(h)

def recur(i):
    if i == 1:#Base case
        return 1
    else:
        return i * recur(i-1)
print(recur(10))
