t=int(input())
while t:
    t=t-1
    n=input()
    flag="Yes"
    c=0
    k=''.join(reversed(n))
    for i in set(n):
        if(n.count(i)%2!=0):
            c=c+1
    if(c>1):
        flag="No"
    print(flag)
            
