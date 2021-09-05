# #reverse a string
# import txt as txt
#
# s = "hello world man".split()
# d = &#39; &#39;.join(reversed(s))
# print(d)
#
# #multiply list and display the last two digits
# a = [22, 31, 44, 27, 37, 43]
# mul = 1
# for i in range (len(a)):
#     mul = mul*a[i]
#     last = mul%100
# print(last)
# print(mul)
#
# #add list to get given output and display the index
# nums = [2,7,11,15]
# n = 9
# f = [(i, i+1) for i in range (0, len(nums)-1) if nums[i]+nums[i+1] == n]
# print(f)
#
# #first non repeating character
# a = &quot;ggggeksfforgeeks&quot;
# d = {k:a.count(k) for k in a}.items()
# print(d)
# for key,value in d:
#     if value==1:
#         print(key,value)
#         break
#
# #reverse string word for word
# a= &quot;hello my world of gaurav&quot;
# s = a.split()
# d = &#39; &#39;.join(reversed(s))
# print(d)
#
# #add the numbers
# a = 1345
# sum=0
# while a&gt;0:
#     sum = sum+(a%10)
#     a = a//10
#     print(sum)
#
# #sum of squares:
# n= 5
# sum = 0
# for i in range(1,n+1):
#     sum = sum+ (i*i)
#     print(sum)
#
# #to print even length of string:
# s = &quot;This is a python language&quot;
# c= s.split()
# for i in c:
# if len(i)%2==0:
# print(i)
#
# #check if number is prime or not:
# n = 20
# for i in range (2,n):
# if n%i==0:
# print(&quot;number is not prime&quot;)
#
# break
# else:
# print(&quot;number is prime&quot;)
# break
#
# #to display largest word in string:
# a = &quot;hello gauravs world of fun&quot;
# s = a.split()
# word = &#39;&#39;
# count = 0
# for i in s:
# if len(i)&gt;count:
# count = len(i)
# word = i
# print(word)
#
# #display count of vowel
# a = &quot;hello gauravs world of fun&quot;
# count = 0
# for i in a:
# if i in [&#39;a&#39;, &#39;e&#39;, &#39;i&#39;, &#39;o&#39;, &#39;u&#39;]:
# count = count+1
# print(count)
#
# #to display smallest word in string:
# a = &quot;hello gauravs world of fun&quot;
# b=a.split()
# count = 51
# word = &#39;&#39;
# for i in b:
# if len(i)&lt; count:
# word = i
# count = len(i)
# print(word)
#
# #Printing string in reverse
# s= &quot;DEVELOPERS&quot;
# r= s[::-1]
# # r = &#39;&#39;
# # size = len(s)
# # for i in range(size-1,-1,-1):
# # r = r+s[i]
# print(r)
# # n = input(&quot;enter word&quot;)
# # reverse = &#39;&#39;
# # for i in range(len(n)-1, -1, -1):
# # reverse = reverse+n[i]
# # print(reverse)
# # if reverse==n:
# # print(&quot;is palindrome&quot;)
# # else:
# # print(&quot;is not palindrome&quot;)
#
# #write a program that returns a list that contains only the elements that are common between the lists
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# c = []
# for i in b:
#     if i in a and i not in c:
#         c.append(i)
# print(c)
#
# #to return a string without any white spaces at beginning or end
# txt = &quot; Hello World &quot;
# x = txt.strip()
# print(x)