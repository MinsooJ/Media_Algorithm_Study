
arr_u = [[3,2,1],[0,4,1]] #[2][3]
arr_l = [[2,3],[1,0],[2,1]]  #[3][2]
arr_map=[[0,0,0],[0,0,0],[0,0,0]]
arr_dir=[["","",""],["","",""],["","",""]]

for i in range(1,3):
    arr_map[i][0]= arr_map[i-1][0]+arr_u[i-1][0]
    arr_dir[i][0]= arr_dir[i-1][0]+"d"

for j in range(1,3):
    arr_map[0][j]= arr_map[0][j-1]+arr_l[0][j-1]
    arr_dir[0][j]= arr_dir[0][j-1]+"r"

for i in range(1,3):
    for j in range(1,3):
        if(arr_map[i-1][j]+arr_u[i-1][j]>=arr_map[i][j-1]+arr_l[i][j-1]):
            arr_map[i][j] = arr_map[i-1][j]+arr_u[i-1][j]
            arr_dir[i][j] = arr_dir[i-1][j]+"d"
        else:
            arr_map[i][j] = arr_map[i][j-1]+arr_l[i][j-1]
            arr_dir[i][j] = arr_dir[i][j-1]+"r"


print(arr_dir[2][2])
print(arr_map[2][2])