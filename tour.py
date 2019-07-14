m1=int(input())
c1=[]
p1=0
for k in range (0,m1+1):
    p1=abs((2**k)-m1)
    c1.append(p1)
print(min(c1))
