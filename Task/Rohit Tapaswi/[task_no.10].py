m=int(input("enter no of rows:"))
n=int(input("enter no of columns:"))
matrix=[]
for i in range(1,m+1):
    row=[]
    for j in range(1,n+1):
        element=int(input("enter element:"))
        row.append(element)
    matrix.append(row)
print("the enter matrix is:")
print(matrix)
transposematrix=[[0,0],
                 [0,0],
                 [0,0]]
for i in range(len (matrix)):
    for j in range(len(matrix[0])):
        transposematrix[j][i]=matrix[i][j]
print("the transpose matrix is :")
print(transposematrix)