def reverse_string(string):
    new_string=""
    for i in range(1,len(string)+1):
        new_string=new_string+string[-i]
    print(new_string)
string="hello world"
reverse_string(string)
