try:
    t=int(input())
    while t:
        n=input()
        count=0
        for i in n:
            if i.isalpha():
                count=count+1
        print(count)
except Exception:
    pass;
