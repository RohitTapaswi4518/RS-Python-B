str1=input("enter the string:")
lowercount=0
uppercount=0
specialcount=0
for character in str1:
    if character.isupper():
        uppercount+=1
    elif character.islower():
        lowercount+=1
    else:
        specialcount+=1
print("lowercase",lowercount)
print("uppercase",uppercount)
print("specialcharacter",specialcount)
list=[]
for i in range(0,len(str1)):
   list.append(str1[i])
for i in range (0,len(str1)):
   for j in range(0,len(str1)):
      if list[i]<list[j]:
         list[i],list[j]=list[j],list[i]
print(list)
d=dict()
for i in list:
 if i in d:
  d[i]=d[i]+1
 else:
  d[i]=1
print(d)