stack = []
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
print(e)

f = ['d','e','f']
f.insert(3, 'g')
print(f)

stack.append(5)
stack.pop()
print(stack)

i = [4,8,12]
i.remove(4)
print(i)

j = [5,10,15]
j.reverse()
print(j)

j.sort()
print(j)
