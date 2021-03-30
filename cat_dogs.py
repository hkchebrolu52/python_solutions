# Take input for number of test cases
t=int(input())
for i in range(t):
     # take three integers as input and split them
    c,d,l=map(int,input().split())
    # Calculate Value 
    if((l<=(d+c)*4) and l%4==0):
        if(c/2<=d and l>=d*4):
            print("yes")
        elif(c/2>d and l>=((c-d*2)+d)*4):
            print("yes")
        else:
            print("no")
    else:
        print("no")