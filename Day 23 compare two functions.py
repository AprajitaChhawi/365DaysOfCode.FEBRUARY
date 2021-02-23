#User function Template for python3


class Solution:
    def compareFrac (self, s):
        temp=""
        p=[]
        for i in s:
            if i.isdigit():
                temp+=i
            else:
                if temp!="":
                    p.append(temp)
                    temp=""
        p.append(temp)
        k=int(p[0])/int(p[1])
        k1=int(p[2])/int(p[3])
        temp=str(p[0])+'/'+str(p[1])
        temp1=str(p[2])+'/'+str(p[3])
        if k>k1:
            return temp
        elif k<k1:
            return temp1
        else:
            return "equal"
        
        # code here
        


#{ 
#  Driver Code Starts
#Initial Template for Python 3


if __name__ == '__main__': 
    ob = Solution()
    t = int (input ())
    for _ in range (t):
        s = input()
        print(ob.compareFrac(s))




# } Driver Code Ends
