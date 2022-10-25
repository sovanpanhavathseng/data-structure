g = {}
print(g)

g.update()
print(g)

def head(g):
    if g > 0:#Base case
        (g-1)#recursive step
        print(g,end="")
head(5)

def tail(n):
    if n > 0:#Base case
        print(n,end="")
        (n-1)#recursivr step
tail(10)
