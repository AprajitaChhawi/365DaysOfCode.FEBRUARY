t=int(input())
while t:
    t=t-1
    n,k=map(int,input().split(" "))
    l=list(map(int,input().split()))
    a=[]
    s1=0
    for i in range(0,n*n,n):
        a1=l[i:i+n]
        s1=s1+a1.count(1)
        a.append(a1)
    for i in a:
        print(i)
        if k!=0:
            for j in range(len(i)):
                if i[j]==1:
                    i[j]==0
                    print(i)
                    k=k-1
                    print(k)
    print(a)
                    
