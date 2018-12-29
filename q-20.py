'''
q-20
'''
str=input("enter a string")
list1=list(str)
i=0
while(i<len(list1)):
    if(list1[i]=="a"):
        list1[i]="#"
    i+=1
print(' '.join(list1))
