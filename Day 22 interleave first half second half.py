from queue import Queue
def interleave(q):
    stack=[]
    n=q.qsize()
    mid=n//2
    for i in range(mid):
        stack.append(q.queue[0])
        q.get()
    while(len(stack)!=0):
        q.put(stack[-1])
        stack.pop()
    for i in range(mid):
        q.put(q.queue[0])
        q.get()
    for i in range(mid):
        stack.append(q.queue[0])
        q.get()
    while len(stack)!=0:
        q.put(stack[-1])
        stack.pop()
        q.put(q.queue[0])
        q.get()
t=int(input())
while t:
    n=int(input())
    l=list(map(int,input().split()))
    q=Queue()
    for i in range(len(l)):
        q.put(l[i])
    interleave(q)
    length=q.qsize()
    for i in range(length):
        print(q.get(),end=" ")
        
