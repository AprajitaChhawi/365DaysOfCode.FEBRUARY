n=input()
k=len(n)
stack=[]
for i in range(k):
    if(len(stack)==0):
        stack.append(n[i])
    elif(stack[-1]!=n[i]):
        stack.append(n[i])
    elif(stack[-1]==n[i]):
        stack.pop()
print(stack)
