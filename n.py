a=[[1,2],[3,4]]
b=[[5,5],[7,8]]
result=[[0,0],[0,0]]
for i in range(len(a)):
    for j in range(len(b[0])):
        for k in range(len(b[0])):
            result[i][j]+=a[i][j]*b[k][j]