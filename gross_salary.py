# Take input for number of testcases
for i in range(int(input())):
    # Take input for salary
    sal = int(input())
    if sal < 1500:
        print(2*sal)
    else:
        print(99*sal/50+500)
