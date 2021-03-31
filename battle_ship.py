# Take input for number of testcases
for i in range(int(input())):
    # Take string as input
    k=input()
    # Covert character to lowercase
    t=k.lower()
    if(t=="b" ):
        print("BattleShip")
    elif(t=="c"):
        print("Cruiser")
    elif(t=="d" ):
        print("Destroyer")
    elif(t=="f" ):
        print("Frigate")