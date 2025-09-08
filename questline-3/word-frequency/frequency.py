string=input().split()
dic={}
for i in string:
    dic[i]=string.count(i)
    string.remove(i)
dict_sort = dict(sorted(dic.items(), key=lambda item: item[1], reverse=True))
for j in dict_sort:
    print(j,"->",dict_sort[j])
