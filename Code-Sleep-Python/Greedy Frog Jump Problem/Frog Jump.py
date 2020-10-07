#Program to find the number of min jump requre for frog to reach the destination
arr = list(map(int,input().split()))
k = int(input())
flag,i = 1,0
jump =  0
while(i<len(arr)):
    if(arr[i]>k):
        print("Not Possible")
        flag = 0
    else:
        jump+=1
        dis = 0
        p = 0
        while(i<len(arr) and dis + arr[i]<=k):
            p = 1
            dis +=arr[i]
            i+=1
    if(p==0):
        i+=1
if(flag):
    print(jump)
