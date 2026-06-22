import time
import sys
h = 10
m = 45
s = 0
while True:
    sys.stdout.write("\r {:02d} : {:02d} : {:02d}" .format (h,m,s))
    sys.stdout.flush()
    time.sleep(1)
    s = s+1
    if s == 60:
        m = m+1
        s = 0
    if m == 60:
        m = 0
        h = h+1
        s = 0
    if h == 13:
        h = 1
