import math
c2,l2=map(int,input().split())
m2=[]
k2=list(map(int,input().split()))
for j in range(0,l2):
    p2,q2=map(int,input().split())
    m2.append([p2,q2])
for j in m2:
    x2=j[0]-1
    y2=j[1]-1
    print(math.gcd(k2[x2],k2[y2]))
