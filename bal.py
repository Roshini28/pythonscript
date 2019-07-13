m,p=input().split()
r1=abs(len(p)-len(m))
for k in range(len(m)):
  if(len(p)==1 and p[k] in m):
    break
  if(m[k]!=p[k]):
    r1=r1+1
print(r1)
