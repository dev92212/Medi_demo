
str_mini = "   Too much happening here in this world.   "
str2 = "Tomorrow will be better!"

print(str_mini[1:10])
print(str_mini + '\t\t' + str2)
print(str_mini + '\n' + str2)

str3 = "happen"
print(str3 in str_mini)     #will print boolean true/false

if str3 in str_mini:
    print("Present")

split_str = str_mini.split("i")
print(split_str)
print(split_str[1].capitalize())
split_str.insert(2, 22)
print(split_str)

print(str_mini)
print(str_mini.lstrip())
print(str_mini.strip())