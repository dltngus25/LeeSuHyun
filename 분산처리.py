Test_case=int(input())

for i in range(Test_case):
    a, b=map(int,input().split())
    Last_pc=pow(a,b,10)
    if Last_pc==0:
        print(10)
    else:
        print(Last_pc)