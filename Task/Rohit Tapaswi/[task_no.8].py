input_list=[]
number=int(input("entered the number of element :"))
for j in range(number):
 input_list.append(int(input("enter the element:")))
print(input_list)
d=dict()
for i in input_list:
 if i in d:
  d[i]=d[i]+1
 else:
  d[i]=1
print(d)  