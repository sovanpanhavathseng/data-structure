queue = []
print(queue)

queue.append(10)
print(queue)

queue.clear()
print(queue)

queue.copy()
print(queue)

a = [1,3,5]
queue.count(5)
print(queue)

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

queue.append(5)
queue.pop()
print(queue)

g = [4,8,12]
g.remove(4)
print(g)

h = [5,10,15]
h.reverse()
print(h)

h.sort()
print(h)

def recur(i):
    if i == 0:#Base case
        return 0
    print(i)
    recur(i-1)#recursive step
