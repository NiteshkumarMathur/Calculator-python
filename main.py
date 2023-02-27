from sympy import sympify


s =  input('expression')
print(s)

s = sympify(s).n(2)
print(s)