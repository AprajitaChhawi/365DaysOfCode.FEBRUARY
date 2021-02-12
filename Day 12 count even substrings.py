t=int(input())
while t:
    t=t-1
    k=input()
    count=0
    for i in range(len(k)):
        temp=int(k[i])
        if(temp%2==0):
            count=count+len(k[:i+1])
    print(count)
