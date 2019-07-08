k=int(input())
if k > 1:
    for p in range(2,k):
        if(k%p==0):
            print('no')
            break
    else:
            print('yes')
else:
            print('no')
