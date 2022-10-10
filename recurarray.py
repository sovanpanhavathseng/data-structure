x = []
print(x)

x.append(10)
print(x)

def recur(x):
    if x == 1:
        return 1
    else:
        return x * recur(x-1)
    recur(10)
    print(recur(10))
