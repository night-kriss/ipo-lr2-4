import math
x=float(input("enter x"))
y=float(input("enter y"))
z=float(input("enter z"))
numerator = x**(y+1) + math.exp(y-1)
denominator = 1 + x * abs(y - math.tan(z))
term1 = numerator / denominator
term2 = 1 + abs(y-x)
term3 = term1*term2
term4 = abs((y - x**2) / 2)
term5 = abs((y - x**3)/3)
h = term3 + term4-term5
print("h = ", h)
