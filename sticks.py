#Take number for number of testcases
for i in range(int(input())):
    # Take input for number of sticks
    n=int(input())
    #Take list for length of sticks 
    a=list(map(int,input().split()))
    
    a.sort(reverse=True)
    print(a)
    dimension=[0,0]
    i=0
    j=0
    while(i<n-1 and j<2):
        if a[i]==a[i+1]:
            dimension[j]=a[i]
            i+=1
            j+=1
        i+=1
    if dimension[0]*dimension[1]>0:
        print(dimension[0]*dimension[1])
    else:
        print(-1)
    