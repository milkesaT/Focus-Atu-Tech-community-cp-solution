n,h=list(map(int,input().split()))
arr1=list(map(int,input().split()))
sum=0
for i in range(n):
    if(arr1[i]<=h):
      sum+=1
    else :
       sum+=2
print(sum)
