t=int(input())
while t:
    t=t-1
    l=list(map(int,input().split()))
    mid=len(l)//2
    if l[mid]==l[mid+1]:
        print(l[mid])
    else:
        print(l[mid-1])
