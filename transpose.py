#Program to transpose a matrix
matrix=[
    [1,3,5,3],
    [3,6,7,4],
    [4,8,3,6],
]
transposed=[]
for i in range(4):
    transposed.append([row[i] for row in matrix])
print(transposed)