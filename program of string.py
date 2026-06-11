d={'A':11,'B':12,'c':13,'d':14}
s="aa bb cc dd"
sum=0
for i in s:
    if i in d.keys():
        sum =sum+d[i]
print(sum)
