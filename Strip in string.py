def remove_and_split(string,word):
    newstr=string.replace(word,"")
    return newstr.strip()

this = "    How are you     "
n=remove_and_split(this,"How")
print(n)

# print(this.strip())# it is used to remove spaces in string from start and end