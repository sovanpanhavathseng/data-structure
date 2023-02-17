1
a = 5
b = 3
c = a + b
d = a - b
print(c) # Output: 8
print(d) # Output: 2

2
a = 5
b = 3
c = a * b
d = a / b
print(c) # Output: 15
print(d) # Output: 1.6666666666666667

3
a = 5
b = 3
c = a ** b
print(c) # Output: 125

4
import math
a = 25
b = math.sqrt(a)
print(b) # Output: 5.0

5
from sympy import symbols, solve
x, y = symbols('x y')
eq1 = x + y - 4
eq2 = 2*x - y - 1
sol = solve((eq1, eq2), (x, y))
print(sol) # Output: {x: 1, y: 3}
