from operator import length_hint
from unicodedata import name


cotation = "God help those who help themselves"
# String Function 
# To Find length of the String we use length Function
print(len(cotation))
#it check the ends of string if match it print true otherwise false
print(cotation.endswith("s"))
#it is used to count words and characters in a string which we checks
print(cotation.count("e"))
#captalize the string character of start
print(cotation.capitalize())
#To find the word in string if a word repeating in string it only tell 
# the most first value index
print(cotation.find("those"))
# it replace the words in the string
print(cotation.replace("who", "whose"))