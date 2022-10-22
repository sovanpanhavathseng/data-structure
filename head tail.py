def head(n):
    if n > 0:#Base case
        head(n-1)#recursive step
        print(n,end="")

head(5)

def tail(x):
    if x > 0:#Base case
        print(x,end="")
        tail(x-1)
tail(6)
