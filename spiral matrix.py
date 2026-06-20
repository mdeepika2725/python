a=[[81,82,83,84,85,86],[10,11,12,13,14,15],[21,22,23,24,25,26],[31,32,33,34,35,36],[41,42,43,44,45,46]]
top=0
bottom=len(a)-1
left=0
right=len(a[0])-1
while(top<=bottom and left<=right):
    for i in range(left,right+1):
        print(a[top][i],end=" ")
    top=top+1
    for i in range(top,bottom+1):
        print(a[i][right],end=" ")
    right=right-1
    if top< right:
        for i in range(right,left-1,-1):
            print(a[bottom][i],end=" ")
        bottom=bottom-1
    if left <right:
        for i in range(bottom,top-1,-1):
             print(a[i][left],end=" ")
        left=left+1
