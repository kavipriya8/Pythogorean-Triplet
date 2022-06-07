import math
from math import sqrt
from decimal import Decimal
l=list(map(int,input().split()))
m=str(l)
n=len(l)
for i in range(0,n):
    for j in range(i,n):
        a=l[i]*l[i]
        b=l[j]*l[j]
        c=a+b
        r=(math.sqrt(c))
        s = str(Decimal(r))
        k=(s.rstrip('0').rstrip('.') if '.' in s else s)
        if k in m:
            print(l[i],l[j],k)