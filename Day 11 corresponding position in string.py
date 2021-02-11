t=int(input())
while t:
    t=t-1
    s1=input()
    s2=input()
    s1=s1.lower()
    s2=s2.lower()
    count=0
    for i in range(len(s1)):
        if(s1[i]==s2[i]):
            count=count+1
    print(count)
