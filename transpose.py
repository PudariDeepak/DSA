#transpose of a matrix
def transpose(mat):
    row_len=len(mat)
    col_len=len(mat[0])
    result=[]
    for i in range(col_len):
        row=[]
        for j in range(row_len):
            row.append(0)
        result.append(row)
    for i in range(row_len):
        for j in range(col_len):
            result[j][i]=mat[i][j]
    return result
mat=[[1,2,3],[4,5,6]]
print(transpose(mat))
