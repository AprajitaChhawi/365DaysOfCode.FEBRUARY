t=int(input())
while t:
    t=t-1
    s=input()
    for i in range(len(s),0,-1):
        print(s[:i])
    
