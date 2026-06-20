s=input("Enter any password:")
up=0
sm=0
dg=0
sp=0
if len(s)>7:
    for i in s:
        if i.isupper():
            up=up+1
        elif i.islower():
            sm=sm+1
        elif i.isdigit():
            dg=dg+1
        else:
            sp=sp+1
    if dg>0 and sp>0 and sm>0 and up>0:
        print(STRONG)
    else:
        print(WEAK)
else:
    print("WEAK DUE TO LESS")
        
