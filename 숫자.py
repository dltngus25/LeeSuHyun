'''a, b=map(int,input().split())

if a>b:
    a,b=b,a

print(b-a-1)
print((a+1,b))'''

import sys

a, b=map(int, sys.stdin.readline().split())

if a>b:
    a,b=b,a

number_between = b-a-1
print(number_between)

if number_between:
    print(' '.join(map(str, range(a+1,b))))