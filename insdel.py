r1,k1=map(str,input().split())
m1=0
if len(r1)>len(k1):
	r1,k1=k1,r1
t1=0
while t1<len(r1):
	  m1+=(ord(k1[t1])-ord(r1[t1]))
	  t1+=1
for t1 in range(t1,len(k1)):
	  m1+=ord(k1[t1])-ord('a')+1
print(m1)
