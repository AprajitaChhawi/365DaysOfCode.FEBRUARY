#User function Template for python3

class MyQueue:
    def __init__(self):
        self.que=[]
        self.rear=None
        self.front=None
        self.size=0
    
    def push(self, x):
        self.que.append(x)
        if self.front==None:
            self.front=self.rear=0
        else:
            self.rear=self.size
        self.size+=1
        
        
         
         #add code here
     
    def pop(self):
        if self.size==0:
            return -1
        temp=self.que.pop(0)
        self.size=self.size-1
        if self.size==0:
            self.front=self.rear=None
        else:
            self.rear=self.size-1
        return temp
        
         
         # add code here



#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for i in range(t):
        s=MyQueue()
        q=int(input())
        q1=list(map(int,input().split()))
        i=0
        while(i<len(q1)):
            if(q1[i]==1):
                s.push(q1[i+1])
                i=i+2
            elif(q1[i]==2):
                print(s.pop(),end=" ")
                i=i+1
            elif(s.isEmpty()):
                print(-1)
                i=i+1
        print()   

# } Driver Code Ends
