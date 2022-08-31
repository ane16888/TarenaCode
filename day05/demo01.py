l = [5,8,4,6,2,9]
for i in range(len(l)-1):
    for c in range(i+1,len(l)):
        if l[i] < l[c]:
            l[i],l[c] = l[c],l[i]
print(l)
