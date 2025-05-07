T=int(input())
for i in range(T):
    R, S=input().split()
    gongback=''
    for j in range(len(S)):
        gongback+=S[j]*int(R)
    print(gongback)