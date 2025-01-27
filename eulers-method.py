import math
import cmath


def dydxeval(dydx, x, y):
    dydx = dydx.replace("x", str(x))
    dydx = dydx.replace("y", str(y))
    return eval(dydx)


dydx = input("dy/dx: ")
start = int(input("Lower Bound (x value): "))
final = int(input("Upper Bound (x value): "))
if input("Step Size or Number of Steps (True for former, False for latter): ") == "True":
    dx = int(input("Step Size (Delta x): "))
    stepnum = (final - start) / dx
else:
    stepnum = int(input("Number of Steps: "))
    dx = (final - start) / stepnum

initialx = int(input("Initial Condition (x value): "))
initialy = int(input("Initial Condition (y value): "))

dydx = dydx.replace("^", "**")
dydx = dydx.replace("e", "math.e")
dydx = dydx.replace("sqrt", "math.sqrt")

x = initialx
y = initialy
m = dydxeval(dydx,initialx,initialy)

table = [[y, m, m*dx+y]]

for i in range(stepnum-1):
    

