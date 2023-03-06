import random
a = int(random.randrange(0,10))
b = int(random.randrange(1,10))
print(a,b)
def pip(a,b):
    if a in (0,1) or b==1:
        return a
    return a*pip(a,b-1)
print(pip(a,b))