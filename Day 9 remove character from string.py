#User function Template for python3

class Solution:
    def removeChars (ob, string1, string2):
        d={}
        k=""
        for i in string2:
            d[i]=True
        for i in string1:
            if i not in d:
                k=k+i
        return k
        # code here 



#{ 
#  Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        string1=input()
        string2=input()
        
        ob = Solution()
        print(ob.removeChars(string1,string2))
# } Driver Code Ends
