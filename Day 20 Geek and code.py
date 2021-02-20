import math
t=int(input())
while t:
    t=t-1
    n=int(input())
    c=0
    b=bin(n)
    c=b.count('1')
    print(c)
