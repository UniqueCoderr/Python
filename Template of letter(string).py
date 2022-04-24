from unicodedata import name


letter= '''Dear <|Name|>,
Have a great day  ahead!
you are selected!

Thanks and Regard
from Administrator
Date: <|Date|>
'''
name = input("ENTER YOUR NAME: ")
date = input("ENTER THE DATE: ")
letter=letter.replace('<|Name|>',name)
letter=letter.replace('<|Date|>',date)
print('\n\n')

print(letter)