#User function Template for python3

def rev(q):
    l=[]
    while(not q.empty()):
        l.append(q.queue[0])
        q.get()
    while(len(l)!=0):
        q.put(l[-1])
        l.pop()
    return q
        
    #add code here



#{ 
#  Driver Code Starts
#Initial Template for Python 3

from queue import Queue
if __name__=='__main__':
    t=int(input())
    for i in range(t):
        n=int(input())
        a=list(map(int,input().split()))
        q=Queue(maxsize=n+1)
        for j in a:
            q.put(j)
        q=rev(q)
        for i in range(0,n):
            print(q.get(),end=" ")
        print()
# } Driver Code Ends
