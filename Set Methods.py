a = {"a", "b", "c"}
a.add("d")
print(a)

b = {1, 2, 3}
b.clear()
print(b)

c = {"e", "f", "g"}
d = {4, 5, 6}
e = c.difference(d)
print(e)

f = {"h", "i", "j"}
g = {7, 8, 9}
f.difference_update(g)
print(f)

h = {"k", "l", "m"}
i = {10, 11, 12}
j = h.intersection(i)
print(j)

k = {"n", "o", "p"}
l = {13, 14, 15}
k.intersection(l)
print(k)

m = {"q", "r", "s"}
n = {16, 17, 18}
t = m.isdisjoint(n)
print(t)

u = {"a", "b", "c"}
v = {"f", "e", "d", "c", "b", "a"}
w = u.issubset(v)
print(w)

x = {"f", "e", "d", "c", "b", "a"}
y = {"a", "b", "c"}
z = x.issuperset(y)
print(z)
z1 = {"t", "u", "v"}
z1.pop()
print(z1)

z2 = {"w", "x", "y"}
z2.remove("x")
print(z2)

z3 = {"z", "z1", "z2"}
z4 = {19 , 20, 21}
z5 = z3.symmetric_difference(z4)
print(z5)

z6 = {"z3", "z4", "z5"}
z7 = {22, 23, 24}
z6.symmetric_difference_update(z7)
print(z6)

z8 = {"z6", "z7", "z8"}
z9 = {25, 26, 27}
z10 = z8.union(z9)
print(z10)

x1 = {"z9", "z10", "x1"}
x2 = {28, 29,30}
x1.update(x2)
print(x1)
