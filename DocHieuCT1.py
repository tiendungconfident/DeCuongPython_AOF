from math import sqrt
def ham1(x):
    for j in range(2,int(sqrt(x))+1):
        if x%j == 0:
            return False
    return True
ds = [i for i in range (2,10000) if ham1(i)]
print(ds)