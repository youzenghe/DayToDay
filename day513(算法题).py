import sys
from math import *
n = int(input())
for i in range(0,isqrt(n)+1):
    for j in range(i,isqrt(n)+1):
        for k in range(j,isqrt(n)+1):
            l = isqrt(n - (i**2+j**2+k**2))
            if i**2+j**2+k**2+l**2==n and l>=k:
                print(i,j,k,l,sep=' ',end=' ')
                sys.exit(0)
# n = int(input())
# s = list(map(int, input().split()))
# res = 0
# for i in range(len(s)):
#     for j in range(i,len(s)):
#         res = max(res,abs(i-j)+abs(s[i]-s[j]))
# print(res)