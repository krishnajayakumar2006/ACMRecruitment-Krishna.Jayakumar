#binary string
n="1011001"  
# number of steps
k=4
s=n[k-1::-1]#rotating the binary string k steps
q=int(s)
w=int(n)
c=len(n)-k     # getting the count of balance elements
p=w%(10**c)     #getting the balance element
q=q*(10**c)+p    #adding p to s
string=str(q)
decimal_v=int(string,2)
print(decimal_v)
   

    
