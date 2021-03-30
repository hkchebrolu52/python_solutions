#Take input for number of test cases
for t in range(int(input())):
    #Take input for number of minutes
    n=int(input())
    #take input for string inputs of either cookie or milk
    s=input()
    
    if ("cookie" in s):
        if (("cookie cookie" in s) or ("cookie milk" not in s) or s[-1]=="cookie"):
            print("NO")
        else:
            print("YES")
    else:
        print("YES")
    