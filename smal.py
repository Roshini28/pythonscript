RR,k=input().strip().split()
k=int(k)
i=0
while i<len(RR)-1 and k:
 if(RR[i]>RR[i+1]):
  k-=1
  RR=RR[:i]+RR[i+1:]
  if(i!=0):
   i-=1
 else:
  i+=1
mp=RR[:len(RR)-k]
print(mp)
