x,y=map(int,input().split())
for i in range(x+1,y):
    p=0
    a=i
    while(a>0):
        q=a%10
        p+=q**3
        a//=10
    if(i==p):
            print(i,end=" ")
