str1=input("enter the first string :")
str2=input("enter the second string:")
if len(str1)!=len(str2):
    print("false")
else:
    if sorted(str1)==sorted(str2):
        print("true")
    else:
        print("not anagram")