
a={
    "Loyality":"Devotion ",
    "Forest":"Wood",
    "Constant":"Regular"
    
    }
print("Select the words\n",a.keys())
x=input("Enter the word in English:  ")
# This command give an error in we put wrong 
# choice which is not present in the dictionary
# print("The meaning of the world is",a[x])
print("The meaning of the world is: ",a.get(x))
