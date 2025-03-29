n,m = map(int, input().split())
lst = list(map(int, input().split()))
a = []

for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            thr = lst[i] + lst[j] + lst[k]
            if thr > m:
                continue
            else:
                a.append(thr)
print(max(a))