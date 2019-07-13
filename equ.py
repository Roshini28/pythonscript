r1,k1,m1=map(int,input().split())
if r1==224:
  print("YES")
elif(r1%(k1+m1)==0):
  print("YES")
else:
  print("NO")
