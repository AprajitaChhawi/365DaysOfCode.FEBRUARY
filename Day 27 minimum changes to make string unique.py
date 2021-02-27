t=int(input())
while t:
    t=t-1
    n=input()
    l=len(n)
    k=len(set(n))
    print(l-k)
