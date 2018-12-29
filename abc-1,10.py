'''
'''
q-10
'''

str=input("enter a string\n")
list1=list(str)
for x in list1:
    if x in "aeiou":
        list1.remove(x)

result = ''.join(list1)
print(result)


'''
q-1
'''

x=int(input("enter the number"))
if(x%2==0):
      print("the number is even")
else:
      print("the number is odd")
'''
