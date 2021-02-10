def insertAtBottom(l,temp):
    if(len(l)==0):
        l.append(temp)
    else:
        item=l.pop()
        insertAtBottom(l,temp)
        l.append(item)
def reverselist(l):
    if len(l)!=0:
        temp=l.pop()
        reverselist(l)
        insertAtBottom(l,temp)
t=int(input())
while t:
    t=t-1
    n=int(input())
    l=list(map(int,input().split()))
    reverselist(l)
    print(l)
