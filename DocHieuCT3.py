from math import sqrt
def ham2(x):
    c = 0
    for j in range(1, x+1):
        if x % j == 0:
            c += j
    if c == 2*x:
        return 1
    else:
        return 0
a = int(input("a = "))
b = int(input("b = "))
ds = [i for i in range(a,b) if ham2(i) == 1]
print(ds)