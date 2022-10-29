def tree(a):
    if a > 0:#Base case
        print(a,end="")
        tree(a-1)#recursive step
        tree(a-1)#recursive step
tree(3)

def tree(b):
    if b > 0:#Base case
        print(b,end="")
        tree(b-1)#recursive step
        tree(b-1)#recursive step
tree(4)

def tree(c):
    if c > 0:#Base case
        print(c,end="")
        tree(c-1)#recursive step
        tree(c-1)#recursive step
tree(5)

def tree(d):
    if d > 0:#Base case
        print(d,end="")
        tree(d-1)#recursive step
        tree(d-1)#recursive step
tree(6)

def tree(e):
    if e > 0:#Base case
        print(e,end="")
        tree(e-1)#recursive step
        tree(e-1)#recursive step
tree(7)










def nested(f):
    if f > 100:#Base case
        return f-10
    return nested(nested(f+11))
nested(3)

def nested(g):
    if g > 100:#Base case
        return g-10
    return nested(nested(g+11))
nested(4)

def nested(h):
    if h > 100:#Base case
        return h-10
    return nested(nested(h+11))
nested(5)

def nested(i):
    if i > 100:#Base case
        return i-10
    return nested(nested(i+11))
nested(6)

def nested(g):
    if g > 100:#Base case
        return g-10
    return nested(nested(g+11))
nested(7)
