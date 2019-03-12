def valid(i,j,row,col):
        pos = [[i,j],[i-1,j],[i+1,j],[i,j+1],[i,j-1]]
        print(pos)
        if i-1 < 0:
            pos.remove([i-1,j])
        if j-1 < 0:
            pos.remove([i,j-1])
        if i+1 >= row:
            pos.remove([i+1,j])
        if j+1 >= col:
            pos.remove([i,j+1])
        return pos
a = valid(3,3,4,5)
for each in a:
    print(each)
    for ele in each:
        print(ele)
print(a)