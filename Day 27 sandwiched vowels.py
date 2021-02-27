#User function Template for python3

  
def Sandwiched_Vowel(s):
    vowel='aeiou'
    k=""
    if len(s)==1:
        return s
    k=s[0]
    temp=len(s)
    for i in range(1,temp-1,1):
        if ((s[i]  not in vowel) or (s[i-1] in vowel) or (s[i+1] in vowel)):
            k=k+s[i]
    k=k+s[temp-1]
    return k
        
    #Complete the function
 

#{ 
#  Driver Code Starts
#Initial Template for Python 3


   

for _ in range(0,int(input())):
    s = input()
    v = Sandwiched_Vowel(s)
    print(v)
    
# } Driver Code Ends
