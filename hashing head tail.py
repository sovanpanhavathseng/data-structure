h = {}
print(h)

h.update()
print(h)

def head(h):
    if h > 0:#Base case
        (h-1)#recursive step
        print(h,end="")
head(5)

def tail(n):
    if n > 0:#Base case
        print(n,end="")
        (n-1)#recursivr step
tail(10)
