a=595672
d={}
for i in str(a):
    if i in d:
        d[i]=d[i]+1
    else:
        d[i]=1
    print(d)
    c=0
    for i in d.values():
        if i>1:
            c=c+1
    print(c)
