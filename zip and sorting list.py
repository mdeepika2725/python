names=["GILL","SARA","ALI","DHONI","RAJU"]
age=[30,29,48,32,26]
res=list(zip(age,names))
res1=sorted(res,reverse=True)
for i in range(5):
   print("{}.{}-{}yrs old".format(i+1,res1[i][1],res1[i][0]))
    
   
