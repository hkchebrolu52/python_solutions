#take input for number of testcases
t = int(input())

for i in range(t):
    #Take input for number of elements
    s = int(input())
    #Take inputs of array and split them
    list1 = input().split()
    # Covert String inputs to int
    list2 = [int(j) for j in list1]
    # Check if first element of list 2 multiplies second element of list2 is in list 2
    if list2[0] * list2[1] in list2:
        print('yes')
    else:
        print('no')