import math
#Ask input for number of strips
for i in range(int(input())):
    #Ask for input to get length 
    n=int(input())
    #Ask input for height of sticks 
    #Covert string input into integer and split them and store it to list l
    l=list(map(int,input().split()))

    if n%2==1 and l[0]==1 and l[n-1]==1:
        f=1
        for i in range(n//2):
            if l[i]!=l[n-1-i] or l[i]!=l[i+1]-1:
                f=0
                break
        if f==0:    
            print("no")
        else:  
             print("yes")
    else:  
         print("no")
