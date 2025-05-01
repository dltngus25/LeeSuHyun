A = int(input())
fw = list(input())
fwl = len(fw)
             
for i in range(A - 1):
    other_words = list(input())
    for j in range(fwl):
        if fw[j] != other_words[j]:
            fw[j] = '?'

print(''.join(fw))