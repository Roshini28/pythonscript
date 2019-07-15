s1=int(input())
ls=list(map(int,input().split()))[:s1]
ls.sort()
print(ls[-1])
