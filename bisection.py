import math

__version__= '1.0.0'
__author__= 'Mark Jethro Cortejo'

a = 1.0
b = 2.0
iterations = 50
for iter in range(iterations):
    if (b - a) < 1e-4: break
    p = (a + b) / 2
    eq = lambda x : math.pow(x, 3) + 4 * math.pow(x, 2) - 10
    if eq(p) == 0.0: break
    if eq(p) > 0: b = p
    else: a = p
    print("iter = {}\ta = {:.6f}\tb = {:.6f}\tc = {:.6f}\tfn(c) = {:.6f}\ttol = {}".format(iter+1, a, b, p, eq(p), (b - a)))
