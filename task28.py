import random
a = int(random.randrange(0,10))
b = int(random.randrange(0,10))
print(a,b)
def sum(a,b):
    if a != 0:
         a = a - 1
         return 1 + sum(a,b)
    if b != 0:
        b = b - 1
        return 1 + sum(a,b)
    if a==0 and b==0:
        return 0
print(sum(a,b))