#Take number of testcases
t=int(input())
while(t>0):
    #take input for size of array
    n=int(input())
    # Take input of integers and convert string to int and split them
    a=list(map(int,input().split()))
    print(min(a)*(n-1))
    t=t-1