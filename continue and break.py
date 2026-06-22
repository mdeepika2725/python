for i in range(10,100):
    if i%2==0 or i%3==0:
        continue
    if i%7==1:
        break
    print(i,end=" ")
    
