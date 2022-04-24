age =int(input("Enter the age: "))
if(age>=1 or age<12):
    print('child')
elif(age>=13 and age<20):
     print('teenage')
elif(age>=20 and age<35):
     print('Young')
elif(age>=35 and age<50):
    print('Adult')
elif(age>=50 and age<70):
   print('Old man')
elif(age>=80 and age<100):
    print('Lucky Person')
