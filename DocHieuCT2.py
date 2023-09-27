from math import sqrt
def ham1(x):
    c = 0
    for j in range(1, x+1):
        if x % j == 0:
            c += j
    if c == 2*x:
        return True
    else:
        return False
a = int(input("a = "))
b = int(input("b = "))
ds = [i for i in range(a,b) if ham1(i)]
print(ds)