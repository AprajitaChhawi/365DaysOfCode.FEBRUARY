#User function Template for python3

class Solution:
    def deleteMid(self, s, sizeOfStack):
        if(len(s)==0 or len(s)==1):
            return s
        k=[]
        mid=((sizeOfStack)//2)
        while(mid):
            mid=mid-1
            if(s):
                temp=s[-1]
                s.pop()
                k.append(temp)
        k.reverse()
        s.pop()
        s.extend(k)
        return s
        # code here



#{ 
#  Driver Code Starts
#Initial Template for Python 3

def main():
    t=int(input())
    while(t>0):
        sizeOfStack=int(input())
        myStack=[int(x) for x in input().strip().split()]
        ob = Solution()
        ob.deleteMid(myStack,sizeOfStack)
        while(len(myStack)>0):
            print(myStack[-1],end=" ")
            myStack.pop()
        print()
        t-=1


if __name__=="__main__":
    main()
    
    
# } Driver Code Ends
