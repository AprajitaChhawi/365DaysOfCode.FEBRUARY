def perform(val1,val2,o):
    if o=='+':
        return int(val1+val2)
    elif o=='-':
        return int(val2-val1)
    elif o=='*':
        return int(val2*val1)
    else:
        return int(val1//val2)
    
t=int(input())
while t:
    t=t-1
    exp=input()
    op=[]
    opr=[]
    prec={}
    prec['+']=2
    prec['-']=2
    prec['*']=3
    prec['/']=3
    prec['(']=1
    for i in exp:
        if i in '0123456789':
            opr.append(i)
        elif i=='(':
            op.append(i)
        elif i in '+/*-':
            if(len(op)==0):
                op.append(i)
            else:
                if(prec[i]>=prec[op[-1]]):
                    op.append(i)
                else:
                    while(prec[i]<prec[op[-1]]):
                        o=op.pop()
                        val1=opr[-1]
                        opr.pop()
                        val2=opr[-1]
                        opr.pop()
                        k=perform(int(val1),int(val2),o)
                        opr.append(k)
        elif i==')':
            while(op[-1]!='('):
                o=op.pop()
                val1=opr[-1]
                opr.pop()
                val2=opr[-1]
                opr.pop()
                k=perform(int(val1),int(val2),o)
                opr.append(k)
            op.pop()
    while(len(op)!=0):
        o=op.pop()
        val1=opr[-1]
        opr.pop()
        val2=opr[-1]
        opr.pop()
        k=perform(int(val1),int(val2),o)
        opr.append(k)
    print(opr[0])
        
            
                
            
        
