x=[12,29,33,37,4,7,11,13,44,17,19,137,202,304]
y=list()
for i in x:
    k=0
    for j in range(1,i+1):
        if (i%j==0):
            k=k+1
        if(k==2):
            y.append(i)
r=max(y)
t=min(y)
print("max:min is:")
print(r,t)
print("The absolute difference bet r and t is:")
print(r-t)