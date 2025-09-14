binary=str(input())
k=int(input())
rotated=binary[-k:]+binary[:-k]
decimal=int(rotated,2)
print(decimal)
