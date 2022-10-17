def recurrent(n):
  if n == 1:
    return 1
  else:
    return n * recurrent (n - 1)
print(recurrent(10))

def c(d):
    if d == 0:
        return 0#Base case
    print(d)
    c(d-1)#recursive step
