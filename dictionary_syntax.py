from turtle import update


myDic = {
    "Key" : "My name is Touseef Abbas",
    "fast" : "typing fast",
    "Start": "Keep typing",
    "Marks": [0,1,2],
    1:2,
    "Anotherdic":{"Hello":"players"}
}
# dictionary is unordered 
# it is editable or mutable
#duplicate keys not allowed
# it is indexed
print(myDic["Key"])
print(myDic["Start"])
print(myDic["fast"])
myDic["Marks"]=[56,89,45]
print(myDic["Marks"])
print(myDic["Anotherdic"]['Hello'])
print(myDic[1])
# Dictionary Method 
print(myDic.keys()) # print all keys in the dictionary
print(type(myDic.keys()))#print type of dictionary
print(myDic.values()) # print all values in the dictionary
print(myDic.items()) # print all content(key and values) in the dictionary
# update the dictionary by adding new pairs of key and value
print(myDic)
updateDic = {
    'Name':"Touseef Abbas ",
    'Roll no': 525,
    'Key' : "A programmer"
}
myDic.update(updateDic)
print(myDic)
# 
print(myDic.get("Name"))# print the value associated with "Name"
print(myDic["Name"])# print the value associated with "Name" 
#  the differnce between .get and [] syntax in dictionaries
print(myDic.get("Name1")) # display none if not value pressent
print(myDic["Name1"]) # throw when value not present
