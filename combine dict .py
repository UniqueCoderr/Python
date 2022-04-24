dic= {}
# When all names are unique with various language
a=input("Enter your favourite language Ali ")
dic["Ali"]=a
b=input("Enter your favourite language Raza ")
dic["Raza"]=b
c=input("Enter your favourite language Ahmad ")
dic["Ahmad"]=c 
d=input("Enter your favourite language Sajjad ")
dic["Sajjad"]=d 

print(dic)

# When name is repeat with various language
# if name is repeated hen it modified the list instead of separate write
# if we repeat language not effect in dictionary due to depend upon key
a=input("Enter your favourite language Ali ")
dic["Ali"]=a
b=input("Enter your favourite language Raza ")
dic["Raza"]=b
c=input("Enter your favourite language Ali ")
dic["Ali"]=c 
d=input("Enter your favourite language Sajjad ")
dic["Sajjad"]=d 
print(dic)

# Question: Can you change the values inside the list 
# which is contained in set s
# s={2,6,7,"Touseef",[1,3]}
# Answer: Firstly we cannot add list in set it throws error
# and Secondly tuple ca be add to set which cannot change



