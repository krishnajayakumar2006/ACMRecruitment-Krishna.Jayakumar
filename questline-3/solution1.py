# multiples of 3 or 5
limit=1000
sums=0
for num in range(1,limit):
    if num%3==0 or num%5==0:
        sums+=num
print(sums)
