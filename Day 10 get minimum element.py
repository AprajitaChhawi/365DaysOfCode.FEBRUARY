#User function Template for python3

class stack:
    def __init__(self):
        self.s=[]
        self.minEle=[]
        
    def push(self,x):
        self.s.append(x)
        if len(self.minEle)==0:
            self.minEle.append(x)
        elif self.minEle[-1]>x:
            self.minEle.append(x)
        else:
            self.minEle.append(self.minEle[-1])
        #CODE HERE

    def pop(self):
        if(len(self.s)==0):
            return -1
        temp=self.s.pop()
        self.minEle.pop()
        return temp
        #CODE HERE
        

    def getMin(self):
        if self.minEle:
            return self.minEle[-1]
        else:
            return -1
        #CODE HERE



#{ 
#  Driver Code Starts
#contributed by RavinderSinghPB
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        q = int(input())

        arr = [int(x) for x in input().split()]

        stk=stack()  

        qi = 0
        qn=1
        while qn <= q:
            qt = arr[qi]

            if qt == 1:
                stk.push(arr[qi+1])
                qi+=2
            elif qt==2:
                print(stk.pop(),end=' ')
                qi+=1
            else:
                print(stk.getMin(),end=' ')
                qi+=1
            qn+=1
        print()

# } Driver Code Ends
