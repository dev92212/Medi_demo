print("Sup!")
a = 11
b = 1
print("Value is:",a, ", and value of b is:", b)

c = 100+3j
print(type(c))

### LIST OPERATIONS

#cc = 2,3,4,5
#print(type(cc))
#print(cc)

cc = [2, 3, 4, 11, 111, 5]
#print(type(cc))
print(cc)
cc.insert(1, 22)
print(cc)
x = cc.index(5, 3, 17)
print(cc)
print(x)

### TUPLE OPERATIONS

cc = (2,3,4,5)
print(type(cc))


### DICTONARY OPERATIONS

dictonary_My = {1: "Dev", 2: "Who", "Address": "Home", "uu": {"DD": "12", "MM": '08', "YY": '1993'}}
print(dictonary_My.values())
print(dictonary_My.keys())

second_dict = {}
second_dict[22] = "Indian"
dictonary_My[22] = "Indian"

print(second_dict)
print(dictonary_My)

second_dict["Indian"] = 22
dictonary_My["Indian"] = 22

print(second_dict)
print(dictonary_My)

second_dict.update({22: "Indian"})
print(second_dict)
