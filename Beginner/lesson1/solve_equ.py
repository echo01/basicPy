# from sympy import symbols, Eq, solve
from sympy import *
import math

x, y, z = symbols('x y z')

# init_session()
eq1 = Eq(5*x+7*y,50)
eq2 = Eq(7*x+5*y,46)

# sol = eq2.subs(y,2).subs(x, 3)

# eq3=input("Type Eq (x,y,z)")
# eq1 = x**2+9*x+18
# eq2 = eq1*(x+1)
sol = solve([eq1, eq2], (x, y))
# print(expand(eq2))
# print(factor(eq2))
print(sol)

# print(factor_list(eq3))
# print(factor(eq3))




