#Take input for number of testcases
for i in range(int(input())):
    # Take input of 3 integers and conver string to int and split them
    a,b,c=map(int,input().split())
    #change value of a if c%2 
    if c%2: 
        a*=2
    print(max(a,b)//min(a,b))