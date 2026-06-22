s="h"
up=0
lo=0
while(s not in"AEIOUaeiou"):
    s=input("Enter the char=")
    if s in "AEIOUaeiou":
        break
    if s.isupper():
        up=up+1
    else:
        lo=lo+1
print(up)
print(lo)
