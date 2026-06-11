d={'A':1,'B':10,'C':100,'D':1000,'E':10000}
S="AAABBCDEH"
sum=0
for i in S:
    if i in d.keys():
        sum=sum+d[i]
print(sum)
