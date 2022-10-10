n = []
print(n)

n.append(10)
print(n)

def recurrent(n):
  if n == 1:
    return 1
  else:
    return n * recurrent (n - 1)
print(recurrent(10))
