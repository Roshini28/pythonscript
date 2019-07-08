a=int(input())
xy=a
sum=0
while a>0:
  y=a%10
  sum=sum+y*y*y
  a=a//10
if xy==sum:
  print("yes")
else:
  print("no")
