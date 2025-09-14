n=int(input())
decimal=0
while n>0:
    if n==3 | n==2:
        reminder=n%2
        value=n//2
        decimal=decimal*100+reminder*10+value
    else:
        remi=n%2
        n=n//2
        decimal=decimal*10+remi
r=str(decimal)
rotated=r[::-1]
print("binary value is",rotated)
print("rotated binary value is",r)
if rotated==r:
    print("it is palindrome")
else:
    print("it is not palindrome")
    
