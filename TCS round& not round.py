n=20
x=[]
while(True):
    if n in x and n !=1:
        print("Not Round")
        break
    if n==1:
        print("Round")
        break
    x.append(n)
    n=sum([int(i)*int(i)for i in str(n)])
    print(x)
