n=100
sumsq=0
sqsum=0
for i in range(1,n+1):
    sumsq+=i**2
for j in range(1,n+1):
    sqsum+=j
print((sqsum**2)-sumsq)
