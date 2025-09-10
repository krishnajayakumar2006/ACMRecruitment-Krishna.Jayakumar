string='amritamalayalamabba' #string initialised
l=[]                        #empty string
for i in range(len(string)):       #checking if any substring is in palindrome 
    for j in range(len(string)):
        string1=string[i:len(string)-j]
        if string1[::-1]==string1:
            l.append(string1)
largest=0             
index=0
for k in l:                         # checking for the largest palindrome
    if len(k)>largest:          # and saving its index value
        largest=len(k)
        index=l.index(k)
print(l[index])             #printing palindrome using index
        
            
