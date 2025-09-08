n=[5,2,9,1,5,6]
for i in range(len(n)):
    for j in range(len(n)):
        if j==len(n)-1:
            break
        elif n[j]>n[j+1]:
            n[j],n[j+1]=n[j+1],n[j]
print(n)
        
        
