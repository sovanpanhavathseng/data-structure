class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


myNode = Node(10)
print("The data in the node is:", myNode.data)
print("The next attribute in the node is:", myNode.next)


def direct(myNode):
    if myNode == 1:#Base case
        return 1
    else:
        return myNode * direct(myNode-1)
print(direct(5))


def tail(b):
    if b > 0:#Base case
        print(b,end="")
        tail(b-1)#resive step
tail(5)


def head(c):
    if c > 0:#Base case
        head(c-1)#recursive step
        print(c,end="")
head(10)


def tree(d):
    if d > 0:#Base case
        tree(d-1)#recursive step
        tree(d-1)#recursive step
tree(15)


def nested(e):
    if e > 100:#Base case
        return e-10
    return nested(nested(e+11))
nested(20)


def A(n):
    if n > 0:#Base case
        print(n,end="")
        # A is colling B
        B(n-1)#recursive step
def B(n):
    if n > 1:#Base case
        print(n,end="")
        # B colling A
        A(n//1)#recursive step
A(20)
