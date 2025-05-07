import sys

x=int(sys.stdin.readline())
S=set()

for i in range(x):
    nums=list(sys.stdin.readline().split())


    if nums[0]=="add":
            S.add(int(nums[1]))
    elif nums[0]=="remove":
            S.discard(int(nums[1]))
    elif nums[0]=="check":
        if int(nums[1]) in S: print(1)
        else: print(0)
    elif nums[0]=="toggle":
        if int(nums[1]) in S: S.remove(int(nums[1]))
        else: S.add(int(nums[1]))
    elif nums[0]=="all":
            S={i for i in range(1,21)}
    elif nums[0]=="empty":
          S=set()