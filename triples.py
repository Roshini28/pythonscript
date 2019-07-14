r1 = int(input())
m1 = list(map(int,input().split()))
p1 = 0
for c in range(r1):
    for t in range(c,r1):  
        for e in range(t,r1):
            if m1[c]<m1[t]<m1[e]:
                p1+=1
print(p1)
